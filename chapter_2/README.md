# Chapter 2 - README <br/> =================

## Spectroscopy - in depth

- &#9745; Origin and history
- &#9744; How it works - MOST IMPORTANT
    - components
    - for different wavelength ranges
    - Key concepts - I.E. what frames, traces, etc. are.
- &#9744; Uses
    - Analysis of substances in chemistry
    - Radial velocity
- &#9744; First use in Astrophysics
    - Any major contributions to astrophysics pointed out
- &#9744; Current uses in Astrophysics
- &#9744; How I use it


## Polarimetry - in depth
- origin ( history - maybe? )
- how it works - MOST IMPORTANT
    - Key concepts - I.E. what stokes parameters, wollaston prisms,
        HWP's, etc. are.
- uses
- first use in Astrophysics
    - Any major contributions to astrophysics pointed out
- current uses in Astrophysics
- how I use it


## Spectropolarimetry - in depth
- origin ( history - maybe? )
- how it works - MOST IMPORTANT
    - Key concepts - I.E. what frames, traces, etc. are.
    - How spectroscopy and polarimetry were combined
- uses
- first use in Astrophysics
    - Any major contributions to astrophysics pointed out
- current uses in Astrophysics
- how I use it


## SALT - basics
- Location
- Telescopes on site
    - Basic summary of other telescopes and something that makes them interesting
        - Some interesting use or aspect for each
        - Instruments on board each
    - Main focus on SALT
        - Some interesting use or aspect
            - The payload movement for example, can't flux calibrate
        - Instruments on board
            - not in depth, RSS discussed in the next section
        - Current uses


## RSS - basics
- (More than just the basic information but not a user guides worth)
- Development and latest developments
- Spectral ranges for gratings
- Modes and uses
    - Focus on spectropolarimetry mode
        - Include how observations are planned


## SpecPol reductions - in depth
- How spectropolarimetry reductions differ from both
    spectroscopy and polarimetry reductions

### General reduction process
- How reductions would be done in general and through pure IRAF
- Frames observed
    - flat
    - bias
    - arc
    - multiple targets
    - ( any others ? )
- Corrections
    - flat fielding
    - bias subtraction (eq from obs. astro)
    - ( any others ? )
- Calibrations
    - wavelength
    - flux
    -shifting (trace to centre)
    - ( any others ? )
- Extraction
    - spectral extraction
- Stokes parameter calculations
- Post processing
    - Displaying
    - saving
    - comparing results

### POLSALT
- Installation instructions of polsalt % To share the pain
- (In depth but not a users guide, more focus on purpose than the parameters)
    (I.E. why each step is necessary and draw comparison to general reduction)
    (and why polsalt works without any major need for concern.)
"All steps except for the wavelength calibration and spectral extraction
    run with no user input. The spectral extraction is not a calibration
    but a simple check to make sure the entire trace is included in the window
    and also that the background regions do not contain any other objects lying
    on the frame or include the trace."

- Raw image reductions
    - All processes run
    - files created
    - PURPOSE!
- Wavelength calibration
    - All processes run
    - files created
    - PURPOSE!
    - Heavy focus since supplementary pipeline replaces this step
- Spectral extraction
    - All processes run
    - files created
    - PURPOSE!
- Raw Stokes calculations
    - All processes run
    - files created
    - PURPOSE!
- Final Stokes calculations
    - All processes run
    - files created
    - PURPOSE!
- Post processing analysis % All 'script.py' steps in the BASH reduction
    - PURPOSE
    - Data Culling (BASH)
    - Flux Calibrations (BASH and errors in GUI)
    - saving plot and text pipeline results (BASH and GUI)
    - Synthetic Filtering (BASH)

- Mention bash script and GUI versions and differences,
    as well as what SALT's preferred method is
