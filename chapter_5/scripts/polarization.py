#! /usr/bin/bash python

"""
A script to quickly extract the pol. degree and angle from the 3C 279 results.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.subplot.hspace': 0,
    'figure.subplot.wspace': 0,
    'figure.subplot.top': 0.99,
    'figure.subplot.bottom': 0.05,
    'figure.subplot.left': 0.05,
    'figure.subplot.right': 0.99,
})
fig, ax = plt.subplots(2, 1, sharex=True)

FOLDER = Path("/media/justin/Transcend/Masters_20-24/Reduced/3C_279/")
WIDTH = 2**6

print(
    "3C 279\n"
    f"{'=' * WIDTH}\n"
    "DATE     LAMP  POLARIZATION DEGREE (%)  POLARIZATION ANGLE (deg)\n"
    "                   (mean ± std, sigma)       (mean ± std, sigma)\n"
    f"{'-' * WIDTH}"
)


for folder in FOLDER.glob("20*"):
    date, lamp = folder.name.split("_")
    print(f"{date} {lamp:<4} ", end="| ")

    if any(Path(folder / "sci_salt").iterdir()):
        folder /= "sci_salt"
    else:
        folder /= "sci_backup"

    file = list(folder.glob("3C279*_c*stokes_unbin.txt"))[0]

    try:
        wav, P, PA, P_err, PA_err = np.genfromtxt(
            file,
            skip_header=4,
            # delimiter=(11, 12, 10, 9, 9, 9, 9, 9, 8, 9),
            usecols=(0, 6, 7, 8, 9),
            unpack=True,
        )
    except ValueError:
        wav, P, PA, P_err, PA_err = np.genfromtxt(
            file,
            skip_header=4,
            delimiter=(11, 12, 10, 9, 9, 9, 9, 9, 8, 9),
            usecols=(0, 6, 7, 8, 9),
            unpack=True,
        )

    # Mask
    mask = (wav > 3800) & (wav < 9200)
    wav, P, PA, P_err, PA_err = wav[mask], P[mask], PA[mask], P_err[mask], PA_err[mask]

    # Averages
    print(
        f"{np.mean(P):6.3f} ± {np.mean(P_err):5.3f}, {np.std(P):6.3f}  | "
        f"{np.mean(PA):6.3f} ± {np.mean(PA_err):5.3f}, {np.std(PA):6.3f} |"
        f"\t{file}"
    )

    # Trends
    # m_P = np.polyfit(wav, P, 1)[0]
    # m_PA = np.polyfit(wav, PA, 1)[0]
    # print(f"{m_P:.2e}, {m_PA:.2e}")

    # Plot
    ax[0].errorbar(wav, P, yerr=P_err, fmt="|", alpha=0.5, label=f"{date} {lamp}")
    ax[1].errorbar(wav, PA, yerr=PA_err, fmt="|", alpha=0.5, label=f"{date} {lamp}")

print(f"{'-' * WIDTH}")
ax[0].legend()
ax[1].legend()
ax[0].set_ylabel("Polarization Degree ($\\%$)")
ax[1].set_ylabel("Polarization Angle ($\\degree$)")
ax[1].set_xlabel("Wavelength ($\\AA$)")
plt.show()

# 3C 279
# ================================================================
# DATE     LAMP  POLARIZATION DEGREE (%)  POLARIZATION ANGLE (deg)
#                    (mean ± std, sigma)       (mean ± std, sigma)
# ----------------------------------------------------------------
# 20170328 Ar   | 13.364 ± 1.985,  2.379  | 53.318 ± 4.306,  5.057 |
# 20170328 Ne   | 13.020 ± 1.102,  1.106  | 51.792 ± 2.466,  2.510 |
# 20170328 ThAr | 13.384 ± 1.985,  2.616  | 53.181 ± 4.295,  5.119 |
# 20170331 Ne   |  8.652 ± 0.849,  0.866  | 63.283 ± 2.728,  3.101 |
# 20170331 ThAr |  9.655 ± 1.397,  1.509  | 61.782 ± 4.150,  4.746 |
# 20170517 Ar   | 21.068 ± 0.713,  1.089  | 77.674 ± 0.975,  1.833 |
# 20170517 Ne   | 21.213 ± 0.782,  0.903  | 76.712 ± 1.145,  1.161 |
# 20170517 ThAr | 21.113 ± 1.240,  1.424  | 76.503 ± 1.671,  2.567 |
# 20170521 Ar   | 19.077 ± 0.686,  1.606  | 76.391 ± 1.070,  2.595 |
# 20180605 Ar   | 17.899 ± 0.363,  0.886  | 43.833 ± 0.534,  1.726 |
# ----------------------------------------------------------------
