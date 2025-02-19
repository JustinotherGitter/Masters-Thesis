#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for analyzing the sky lines of a wavelength calibrated image.
"""

# MARK: Imports
import sys
import logging
from pathlib import Path
from importlib.resources import files

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
from astropy.io import fits as pyfits
from scipy import signal

from STOPS.utils.SharedUtils import find_files, get_arc_lamp
from STOPS.utils.Constants import SAVE_SKY, FIND_PEAK_PARAMS
import STOPS.data
import STOPS.utils
import STOPS.data.RSS_arc


# print(
#  [logging.getLogger(name) for name in logging.root.manager.loggerDict]
# )
mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.INFO)
pil_logger = logging.getLogger('PIL')
pil_logger.setLevel(logging.INFO)


# MARK: Skylines Class
class Skylines:
    """
    Class representing the Skylines object.

    Parameters
    ----------
    data_dir : Path
        The directory containing the data files.
    filenames : list[str]
        The list of filenames to be processed.
    beam : str, optional
        The beam mode, by default "OE".
    plot : bool, optional
        Flag indicating whether to plot the continuum, by default False.
    save_prefix : Path | None, optional
        The prefix for saving the data, by default None.
    **kwargs
        Additional keyword arguments.

    Attributes
    ----------
    data_dir : Path
        The directory containing the data files.
    fits_list : list[str]
        The list of fits file paths.
    beams : str
        The beam mode.
    can_plot : bool
        Flag indicating whether to plot the continuum.
    save_prefix : Path | None
        The prefix for saving the data.
    wav_unit : str
        The unit of wavelength.

    Methods
    -------
    checkLoad(self, path1: str) -> np.ndarray:
        Checks and loads the data from the given path.
    transform(self, wav_sol: np.ndarray, spec: np.ndarray) -> np.ndarray:
        Transforms the input wavelength and spectral data based on
        the given wavelength solution.
    rmvCont(self) -> np.ndarray:
        Removes the continuum from the spectrum.
    process(self) -> None:
        Placeholder method for processing the data.

    See Also
    --------
    matplotlib custom style:
        https://matplotlib.org/stable/users/explain/customizing.html

    Notes
    -----
    Constants imported (see utils.Constants):
        SAVE_SKY:
            The default save name for the skylines plot.
        FIND_PEAK_PARAMS:
            The default parameters for finding peaks in the spectrum.
    """

    # MARK: Skylines init
    def __init__(
            self,
            data_dir: Path,
            filenames: list[str],
            beams: str = "OE",
            split_ccd: bool = False,
            cont_ord: int = 11,
            plot: bool = False,
            transform: bool = True,
            save_prefix: Path | None = None,
            **kwargs,
    ) -> None:
        self.data_dir = data_dir
        self.fits_list, self.arc_list = find_files(
            data_dir=self.data_dir,
            filenames=filenames,
            prefix="wmxgbp",  # t[o|e]beam
            ext="fits",
            sep_arc=True,
        )
        if self.arc_list:
            self.arc_lamp = get_arc_lamp(self.arc_list[0])

        self._beams = None
        self.beams = beams
        self.ccds = 1
        if split_ccd:
            # See cross_correlate for initial implementation
            self.ccds = 3

        self.cont_ord = cont_ord
        self.can_plot = plot
        self.must_transform = transform

        self.save_prefix = save_prefix
        # Handle directory save name
        if self.save_prefix and self.save_prefix.is_dir():
            self.save_prefix /= SAVE_SKY
            logging.warning((
                f"Skylines save name resolves to a directory. "
                f"Saving under {self.save_prefix}"
            ))

        self.max_difference = 5

        self.wav_unit = "$\\AA$"

        logging.debug(f"__init__\n{repr(self)}")

        return

    # MARK: Skylines repr
    def __repr__(self) -> str:
        template = (
            "Skylines(\n"
            f"\tdata_dir={self.data_dir},\n"
            f"\tfits_list=[\n\t\t{"\n\t\t".join(
                map(str, self.fits_list)
            )}\n\t],\n"
            f"\tbeams={self.beams},\n"
            f"\tplot={self.can_plot},\n"
            f"\tsave_prefix={self.save_prefix},\n"
            f"\twav_unit={self.wav_unit}\n"
            ")\n"
        )

        return template

    # MARK: Beams property
    @property
    def beams(self) -> str:
        return self._beams

    @beams.setter
    def beams(self, mode: str) -> None:
        if mode not in ['O', 'E', 'OE']:
            err_msg = f"Correlation mode '{mode}' not recognized."
            logging.error(err_msg)
            raise ValueError(err_msg)

        self._beams = mode

        return

    # MARK: Find Peaks
    def find_peaks(
            self,
            spec: np.ndarray,
            axis: int | None = None,
            min_height: float = 0.5,
            **kwargs,
    ) -> tuple[list[np.ndarray], list[dict]]:
        """
        Finds the peaks in the given spectral data.

        Parameters
        ----------
        spec : np.ndarray
            The spectral data.
        axis: int | None, optional
            The axis along which the peaks are found.
        min_height : float, optional
            The minimum height of the peaks, by default 0.5.

        Returns
        -------
        peaks, properties : tuple[list[np.ndarray], list[dict]]
            The peaks and their properties.
        """
        peaks = []
        props = []
        row_means = []

        for ext in range(len(self.beams)):
            row_mean = spec[ext] if axis is None else np.mean(
                spec[ext], axis=axis
            )

            peak, prop = signal.find_peaks(
                row_mean,
                prominence=min_height * np.max(row_mean),
                width=0,
                **kwargs,
            )
            peaks.append(peak)
            props.append(prop)
            row_means.append(row_mean)

        if self.can_plot:
            fig, axs = plt.subplots(2, 1)
            for ext in range(len(self.beams)):
                axs[ext].plot(
                    row_means[ext],
                    label=f"{'E' if ext else 'O'}"
                )
                axs[ext].plot(
                    peaks[ext],
                    row_means[ext][peaks[ext]],
                    "x",
                    label=f"{'E' if ext else 'O'} peaks"
                )
                axs[ext].legend()
            plt.show()

        logging.debug(f"find_peaks - peaks: {[len(i) for i in peaks]}")
        # logging.debug(
        #     f"find_peaks - props: {[key for key in props[0].keys()]}"
        # )

        return peaks, props

    # MARK: Min. of Diff. Matrix
    @staticmethod
    def min_diff_matrix(
            a: np.ndarray,
            b: np.ndarray,
            max_diff: int = 100
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Find the minimum difference between the elements of two arrays.

        Parameters
        ----------
        a : np.ndarray
            The first 1d array.
        b : np.ndarray
            The second 1d array.
        max_diff : int, optional
            The maximum difference allowed, by default 100.

        Returns
        -------
        a : np.ndarray (len(a))
            The elements of the first array.
        min_vals : np.ndarray (len(a))
            The minimum difference between the elements of the two arrays.
        min_idxs : np.ndarray (len(a))
            The indices of the minimum difference between
            the elements of the two arrays.
        """
        # Compute the difference matrix using transpose
        diff = a - b[:, np.newaxis]

        # Find the minimum value in each row (A) of `diff`
        min_idxs = np.abs(diff).argmin(axis=0)

        min_vals = np.array([diff[j, i] for i, j in enumerate(min_idxs)])
        # TODO: Recalculate min_val after selecting best min_val and
        # TODO: removing the corresponding row/column

        logging.debug(
            f"min_diff_matrix - min_vals=\n{np.round(min_vals, 2).astype(int)}"
        )
        logging.debug(f"min_diff_matrix - min_idxs=\n{min_idxs}")

        max_mask = (min_vals <= max_diff) & (min_vals >= -1 * max_diff)

        return a[max_mask], min_vals[max_mask], min_idxs[max_mask]

    # MARK: Load File Data
    def load_file_data(
            self,
            filename: Path
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Loads the data from the given file.

        Parameters
        ----------
        filename : Path
            The path to the file to be loaded.

        Returns
        -------
        spec, wav, bpm : tuple[np.ndarray, np.ndarray, np.ndarray]
            The wavelength, spectral, and bad pixel mask data.
        """
        # Load data from self.beams extension
        with pyfits.open(filename) as hdul:
            exts = [0, 1]
            if len(self.beams) != 2:
                exts = 0 + int(self.beams == 'E')

            spec2d = np.atleast_3d(hdul["SCI"].data[exts])
            wav2d = np.atleast_3d(hdul["WAV"].data[exts])
            bpm2d = np.atleast_3d(hdul["BPM"].data[exts].astype(bool))

            logging.info(
                f"load_file_data - {filename.name} - shape: {spec2d.shape}"
            )

            return spec2d, wav2d, bpm2d

    # MARK: Load Sky or Arc Lines
    @staticmethod
    def load_lines(
            filename: str | Path | None = None,
            dtype: list[tuple] = [('wav', float), ('flux', float)],
            skip_header: int = 3,
            skip_footer: int = 1
    ) -> np.ndarray:
        """
        Loads the sky or arc lines from the given file.

        Parameters
        ----------
        filename : str | Path | None, optional
            The path to the file to be loaded.
            Defaults to loading the skylines from `data/sky.salt`
        dtype : list[tuple], optional
            The data type of the sky lines.
            (Default is [('wav', float), ('flux', float)])
        skip_header : int, optional
            The amount of lines to skip of the `filenames` header.
            (Default is 3)
        skip_footer : int, optional
            The amount of lines to skip of the `filename`s footer.
            (Default is 1)

        Returns
        -------
        sky_lines : np.ndarray['wav', 'flux']
            The sky lines from the file.
        """
        lines: np.ndarray = None

        usecols = None
        if filename:
            filename = files(STOPS.data.RSS_arc).joinpath(filename)
            usecols = (0, 1)
        else:
            filename = files(STOPS.data).joinpath('sky.salt')

        lines = np.genfromtxt(
            filename,
            dtype=dtype,
            skip_header=skip_header,
            skip_footer=skip_footer,
            usecols=usecols
        )

        logging.debug(
            f"load_lines - {filename.name} - shape: {lines.shape}"
        )

        return lines

    # MARK: Mask Traces
    def mask_traces(
            self,
            spec: np.ndarray,
            bpm: np.ndarray,
            max_traces: int = 1,
            tr_pad: int = 5,
            bg_margin: int = 10,
            lr_margins: list[int] = [10, 10],
            h_min: float = 0.5,
            h_rel: float = 1 - 0.05,
    ) -> np.ndarray:
        """
        Masks the traces in the bad pixel mask.

        Parameters
        ----------
        spec : np.ndarray
            The spectral data.
        bpm : np.ndarray
            The bad pixel mask.
        max_traces : int, optional
            The maximum number of traces to be masked.
            (Default is 1)
        tr_pad : int, optional
            The amount to pad traces by.
            (Default is 5)
        bg_margin : int, optional
            The margin size for the background.
            (Default is 10)
        lr_margins : list[int, int], optional
            The left and right background margins at the spectrum edge.
            (Default is [10, 10])
        h_min: float, optional
            The minimum height of a detected peak.
            (Default is 0.5)
        h_rel: float, optional
            The relative height for the properties of a detected peak.
            (Default is 1)

        Returns
        -------
        bpm : np.ndarray
            The updated bad pixel mask.
        """
        # Base mask
        bpm[:, :bg_margin] = True
        bpm[:, -bg_margin:] = True
        bpm[:, :, :lr_margins[0]] = True
        bpm[:, :, -lr_margins[1]:] = True

        # Get the traces
        traces, tr_props = self.find_peaks(
            spec,
            axis=1,
            min_height=h_min,
            rel_height=h_rel
        )

        for ext in range(len(self.beams)):
            # Mask the traces
            for i in range(len(traces[ext][:max_traces])):
                lb = max(
                    0,
                    int(tr_props[ext]['left_ips'][i]) - tr_pad
                )
                ub = min(
                    spec.shape[-1],
                    int(tr_props[ext]['right_ips'][i]) + tr_pad
                )
                bpm[ext, lb: ub] = True
                # TODO: Relocate targets after initial masking

        logging.info(
            f"mask_traces - {min(max_traces, len(traces))} " +
            f"of {len(traces)} traces masked."
        )

        return bpm

    # MARK: Transform Spectra
    def transform(
            self,
            spec: np.ndarray,
            wav_sol: np.ndarray,
            row_max: int | None = None,
            res_plot: bool = False,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Transforms the input wavelength and spectral data
        based on the given wavelength solution.

        Parameters
        ----------
        spec : np.ndarray
            The spectral data.
        wav_sol : np.ndarray
            The wavelength solution.
        row_max : int, optional
            The row along which the spectral data is to be transformed.
            (Default is None)
        res_plot : bool, optional
            Flag indicating whether to plot the results.
            (Default is False)

        Returns
        -------
        spec, wav : np.ndarray
            The transformed wavelength and spectral data.

        """
        # Create arrays to return
        cs = np.zeros_like(spec)
        cw = np.zeros_like(wav_sol.mean(axis=1))

        for ext in range(len(self.beams)):

            if row_max:
                avg_max = row_max
            else:
                # Get middle row (to interpolate the rest of the rows to)
                avg_max = np.mean(spec[ext], axis=1).argmax()

            # Correct extensions based on wavelength
            # Get wavelength values at row with most trace
            cw[ext] = wav_sol[ext, avg_max]

            # Spec ext
            for row in range(cs.shape[1]):
                cs[ext, row] = np.interp(
                    cw[ext],
                    wav_sol[ext, row],
                    spec[ext, row]
                )
                # f_2d = interpolate.interp2d(
                #     wav_sol[ext, row],
                #     np.arange(rows),
                #     spec[ext],
                # )
                # cs[ext] = f_2d(cw[ext, row], np.arange(rows))

        # Plot results
        if res_plot:
            fig, axs = plt.subplots(2, 1, figsize=[20, 4])
            for ext in range(len(self.beams)):
                axs[ext].imshow(
                    cs[ext],
                    vmax=cs[ext].mean() + 2 * cs[ext].std(),
                    vmin=cs[ext].mean() - 2 * cs[ext].std()
                )

                logging.debug(
                    f"{'E' if ext else 'O'} Average continuum = " +
                    f"{np.median(np.median(cs[ext], axis=0)):4.3f}"
                )

                axx = axs[ext].twinx()
                axx.hlines(
                    np.median(np.median(cs[ext], axis=0)),
                    0,
                    cs[ext].shape[-1],
                    colors='black'
                )
                axx.plot(
                    cs[ext].mean(axis=0),
                    "k",
                    label=f"mean {'E' if ext else 'O'}"
                )
                axx.plot(
                    np.median(cs[ext], axis=0),
                    "r",
                    label=f"median {'E' if ext else 'O'}"
                )
                axx.legend()
            plt.show()

        logging.info(f"transform - {cs.shape} transformed.")

        return cs, cw

    # MARK: Plot
    def plot(
            self,
            spectra,
            wavelengths,
            peaks,
            properties,
            arc: bool = False,
    ) -> None:
        plt.style.use([
            files(STOPS.utils).joinpath('STOPS.mplstyle'),
            files(STOPS.utils).joinpath('STOPS_skylines.mplstyle'),
        ])
        plt.rcParams['figure.subplot.hspace'] *= len(self.beams)

        def norm(vals):
            return (vals - np.min(vals)) / (np.max(vals) - np.min(vals))

        # Load known lines
        if arc:
            lines = self.load_lines(filename=self.arc_lamp)
        else:
            lines = self.load_lines()

        # noinspection PyTypeChecker
        lines = lines[
            (lines['wav'] > wavelengths[1][0][0].min()) &
            (lines['wav'] < wavelengths[1][0][0].max())
            ]

        # Create plot for results
        fig, axs = plt.subplots(2, self.ccds, sharex='col', sharey='row')

        # Convert axs to a 2D array if ccd count is 1
        if self.ccds == 1:
            # noinspection PyTypeChecker
            axs: np.ndarray[matplotlib.axes.Axes] = np.swapaxes(
                np.atleast_2d(axs),
                0,
                1
            )

        for fl in range(len(self.arc_list if arc else self.fits_list)):

            # set color cycle
            # private deprecated
            # color = next(axs[0, 0]._get_lines.prop_cycler)['color']
            color = axs[0, 0]._get_lines.get_next_color()

            for ext in range(len(self.beams)):

                ccdrange = spectra[1][fl][ext].shape[-1] // self.ccds
                for ccd in range(self.ccds):
                    # MARK: plot spectrum
                    # (transformed)
                    axs[0, ccd].plot(
                        wavelengths[1][fl][ext][
                            ccdrange * ccd:ccdrange * (ccd + 1)
                        ],
                        norm(spectra[1][fl][ext][
                            ccdrange * ccd:ccdrange * (ccd + 1)
                        ]) * 100 + 10 * ext + 30 * fl,
                        color=color,
                        linestyle='dashed' if ext else 'solid',
                        label=f"${{{self.beams[ext]}}}_{{{fl + 1}}}^{{+ {10 * ext + 30 * fl}}}$" if ccd == 0 else None,
                    )

                    # MARK: plot dev
                    # noinspection PyTypeChecker
                    sky_wavs, dev, peak_idx = self.min_diff_matrix(
                        lines['wav'],
                        wavelengths[1][fl][ext][peaks[1][fl][ext]],
                        max_diff=self.max_difference,
                    )

                    # # MARK: width/width_init
                    # width = properties[1][fl][ext]['widths'][peak_idx]
                    # width_i = np.zeros_like(width)

                    # sky_i, i_dev, i_idx = self.min_diff_matrix(
                    #     lines['wav'],
                    #     wavelengths[0][fl][ext][peaks[0][fl][ext]],
                    #     max_diff=self.max_difference,
                    # )

                    # width_i = np.array([
                    #     properties[0][fl][ext]['widths'][
                    #         np.where(wav == sky_i)[0][0]
                    #     ]
                    #     if wav in sky_i else 1000
                    #     for wav in sky_wavs
                    # ])
                    # width_ratio = (width / width_i) - 1
                    # width_ratio[width_ratio < 0] = 0

                    # ylolims = width_ratio > self.max_difference
                    # width_ratio[
                    #     width_ratio > self.max_difference
                    # ] = self.max_difference // 2

                    ok = np.where(
                        (sky_wavs >= wavelengths[1][fl][ext].data[
                            ccdrange * ccd
                        ]) &
                        (sky_wavs <= wavelengths[1][fl][ext].data[
                            ccdrange * (ccd + 1)
                        ])
                    )
                    axs[1, ccd].plot(
                        sky_wavs[ok],
                        dev[ok],
                        # yerr=(width_ratio[ok] * 0, width_ratio[ok]),
                        # lolims=ylolims[ok],
                        "." if ext else "x",
                        # fmt="." if ext else "x",
                        alpha=0.8,
                        color=color,
                        # markeredgecolor='white',
                        # markeredgewidth=0.5,
                        # label=f"${self.beams[ext]}_{{{fl + 1}}}$",
                    )

                    logging.debug(
                        f"plot - RMS: {np.sqrt(np.mean(dev[ok] ** 2)):2.3f}"
                    )

        for ccd in range(self.ccds):
            ccdrange = spectra[1][0][0].shape[-1] // self.ccds

            # spectrum
            # noinspection PyTypeChecker
            ok = np.where(
                (lines['wav'] >= wavelengths[1][0][0].data[ccdrange * ccd]) &
                (lines['wav'] <= wavelengths[1][0][0].data[ccdrange * (ccd+1)])
            )
            # noinspection PyTypeChecker
            axs[0, ccd].plot(
                lines['wav'][ok],
                lines['flux'][ok] * 0,
                'x',
                color='C4',
                label="\\textsc{salt}\nModel" if ccd == 0 else None,
            )
            # noinspection PyTypeChecker
            for x in lines['wav'][ok]:
                axs[0, ccd].axvline(x, ls='dashed', c='0.7')

        axs[0, 0].set_ylabel("Rel. Intensity ($\\%$)")
        axs[1, 0].set_ylabel(
            "Closest Peak ($\\Delta\\lambda$)"
        )
        # for ax in axs[:, 0]:
        #     ax.legend(loc='upper left', ncols=(fl + 1) * (ext + 1) + 1)
        leg = fig.legend(
            loc='center',
            ncol=min(8, len(spectra[0]) + 1),
            columnspacing=0.5,
            bbox_to_anchor=(
                np.mean((
                    plt.rcParams['figure.subplot.left'],
                    plt.rcParams['figure.subplot.right']
                )),
                np.mean((
                    plt.rcParams['figure.subplot.bottom'],
                    plt.rcParams['figure.subplot.top']
                ))
            ),
        )
        leg.set_draggable(True)
        for ax in axs[1, :]:
            ax.grid(axis='y')

        axs[-1, 0 if self.ccds == 1 else 1].set_xlabel(
            f"Wavelength ({self.wav_unit})"
        )

        # plt.tight_layout()

        plt.show()

        # Save results
        if self.save_prefix:
            fig.savefig(fname=self.save_prefix)

        return

        # MARK: Process all listed images

    def process(self, arc: bool = False) -> None:
        files = self.fits_list
        if arc:
            files = self.arc_list

        logging.info(f"Processing '{self.beams}' lines.")

        spectra = [[], []]
        wavs = [[], []]
        peaks = [[], []]
        peak_props = [[], []]

        for fl in files:
            # Load data
            spec2d, wav2d, bpm2d = self.load_file_data(fl)

            # Mask traces in BPM
            bpm2d = self.mask_traces(
                spec2d,
                bpm2d,
                max_traces=0,
                bg_margin=15,
                h_min=0.05
            )
            m_spec2d = np.ma.masked_array(spec2d, mask=bpm2d)  # spec2d
            m_wav2d = np.ma.masked_array(wav2d, mask=bpm2d)  # wav2d

            # Initial spectra
            spec_i = np.mean(m_spec2d, axis=-2)
            wav_i = np.mean(m_wav2d, axis=-2)

            # Transform data
            t_spec2d, t_wav = self.transform(
                m_spec2d,
                m_wav2d,
                res_plot=self.can_plot
            )

            # Final spectra
            spec_f = np.mean(t_spec2d, axis=-2)
            wav_f = t_wav

            # Find peaks
            peaks_i, props_i = self.find_peaks(
                spec_i,
                **FIND_PEAK_PARAMS
            )
            peaks_f, props_f = self.find_peaks(
                spec_f,
                **FIND_PEAK_PARAMS
            )

            spectra[0].append([*spec_i])
            spectra[1].append([*spec_f])
            wavs[0].append([*wav_i])
            wavs[1].append([*wav_f])
            peaks[0].append([*peaks_i])
            peaks[1].append([*peaks_f])
            peak_props[0].append([*props_i])
            peak_props[1].append([*props_f])

        # Plot results
        self.plot(spectra, wavs, peaks, peak_props, arc=arc)

        if arc:
            return
        elif self.arc_list:
            self.process(arc=True)

        return


# MARK: Main function
def main(argv) -> None:
    """main function."""

    return


if __name__ == "__main__":
    main(sys.argv[1:])
