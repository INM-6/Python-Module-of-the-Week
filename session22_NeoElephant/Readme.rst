Introduction to Elephant
========================

1) [Neo](https://neo.readthedocs.io/en/0.7.0/)
2) [Elephant](http://neuralensemble.org/elephant/)

Additional Packages
- [Quantities](https://pypi.org/project/quantities/)

Material
- [Snakemake Elephant Tutorial](https://github.com/JuliaSprenger/snakemake_elephant_demo)

Structure
- Neo
    - Why do we need it? File format zoo (proprietary/open; nestio!), standardized representation to build upon
    - Structure and objects
    - The usage of quantities
- Elephant
    - Scope: Analysis requiring spiketrains and/or LFPs
    - submodules
        - core (conversion, binning, filtering, instantaneous phase, kernel (convolution))
        - artificial data generation (ground truth, surrogates, ...)
        - basic statistical measures (isi, mean firing rate, cv, lv, ...)
        - common analyses (STA, spike triggered phase, CSD, change point detection, ...)
        - complex analysis (ASSET, SPADE, UE, CUBIC, CAD, ...)
        - ...to be extended by you!
