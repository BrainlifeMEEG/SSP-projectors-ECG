

# SSP projectors ECG


[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.672-blue.svg)](https://doi.org/10.25663/brainlife.app.672)

Brainlife App to compute SSP (signal-space projection) vectors for ECG artifacts using `mne.preprocessing.compute_proj_ecg` function.



1) Input file is:
    * `meg/fif` meg data file
    
2) Input parameters are:
* 
* `tmin` Time before event in seconds.

* `tmax`Time after event in seconds.

* `n_grad`Number of SSP vectors for gradiometers.

* `n_mag` Number of SSP vectors for magnetometers.

* `n_eeg` Number of SSP vectors for EEG.

* `l_freq` Filter low cut-off frequency for the data channels in Hz.

* `h_freq` Filter high cut-off frequency for the data channels in Hz.

* `average` Compute SSP after averaging. Default is True.

* `filter_length` Number of taps to use for filtering.

* `n_jobs` The number of jobs to run in parallel. If -1, it is set to the number of CPU cores. Requires the joblib package. None (default) is a marker for ‘unset’ that will be interpreted as n_jobs=1 (sequential execution) unless the call is performed under a joblib.parallel_backend() context manager that sets another value for n_jobs.

* `ch_name` Channel to use for ECG detection (Required if no ECG found).

* `reject` Epoch rejection configuration.

* `flat` Epoch flat configuration (see Epochs).

* `bads` List with (additional) bad channels.

* `avg_ref` Add EEG average reference proj.

* `no_proj` Exclude the SSP projectors currently in the fiff file.

* `event_id` ID to use for events.

* `ecg_l_freq` Low pass frequency applied to the ECG channel for event detection.

* `ecg_h_freq` High pass frequency applied to the ECG channel for event detection.

* `tstart` Start artifact detection after tstart seconds.

* `qrs_threshold` Between 0 and 1. qrs detection threshold. Can also be “auto” to automatically choose the threshold that generates a reasonable number of heartbeats (40-160 beats / min).

* `filter_method` Method for filtering (‘iir’ or ‘fir’).

* `iir_params`Dictionary of parameters to use for IIR filtering. See mne.filter.construct_iir_filter for details. If iir_params is None and method=”iir”, 4th order Butterworth will be used.

* `copy` If False, filtering raw data is done in place. Defaults to True.

* `return_drop_log` If True, return the drop log.

* `meg` Can be ‘separate’ (default) or ‘combined’ to compute projectors for magnetometers and gradiometers separately or jointly. If ‘combined’, n_mag == n_grad is required and the number of projectors computed for MEG will be n_mag.

3) Ouput files are:
    * `ECG projectors`
    * a plot of the ECG projectors
    * a html report
   

## Authors
- Saeed ZAHRAN(saeedzahranutc@gmail.com)
- Maximilien Chaumon (maximilien.chaumon@icm-institute.org)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


Copyright (c) 2026 MEEG Brainlife team

This project is licensed under the AGPL-3.0 License - see [license.txt](license.txt) for details.

## Citation

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
