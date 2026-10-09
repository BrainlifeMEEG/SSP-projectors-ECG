# Compute ECG Artifact SSP Projectors

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.672-blue.svg)](https://doi.org/10.25663/brainlife.app.672)

## Description

This Brainlife.io app computes SSP (signal-space projection) vectors targeting ECG (cardiac) artifacts in continuous MEG/EEG data, using MNE-Python's `mne.preprocessing.compute_proj_ecg` function. ECG events are detected directly from the data (via an ECG channel or, if none is found, a proxy channel), the data are epoched around the detected heartbeats and averaged, and SSP projectors are derived from the resulting ECG-locked evoked response.

The app generates:
- SSP projectors for the detected ECG artifact
- A topomap plot of the ECG projectors
- ECG-evoked joint plot figures (butterfly + topomap)
- An HTML report summarizing the projectors and ECG-evoked response

## Inputs

- **`mne`** (`neuro/meeg/mne/raw`): continuous MEG/EEG data to compute ECG SSP projectors from (required)

## Outputs

- **`out_dir/proj.fif`** (`neuro/meeg/mne/projection`): computed ECG SSP projectors
- **`out_figs/ecg_projectors.png`** (`generic/image/png`): topomap plot of the ECG SSP projectors
- **`out_figs/ecg_*.png`** (`generic/image/png`): ECG-evoked joint plot figures (one or more, per `evoked.plot_joint()`)
- **`out_report/report.html`** (`report/html`): QC report with the projector topographies and ECG-evoked plots

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `tmin` | float | `-0.2` | Time before the detected ECG event, in seconds. |
| `tmax` | float | `0.4` | Time after the detected ECG event, in seconds. |
| `n_grad` | int | `2` | Number of SSP vectors for gradiometers. |
| `n_mag` | int | `2` | Number of SSP vectors for magnetometers. |
| `n_eeg` | int | `2` | Number of SSP vectors for EEG. |
| `l_freq` | float | `1.0` | Filter low cut-off frequency for the data channels, in Hz. |
| `h_freq` | float | `35.0` | Filter high cut-off frequency for the data channels, in Hz. |
| `average` | bool | `true` | Compute SSP after averaging the ECG-locked epochs. |
| `filter_length` | string | `"10s"` | Length of the FIR filter applied to the data channels (e.g. a duration string such as `"10s"`). |
| `ch_name` | string | `""` | Channel to use for ECG detection. Required if no ECG channel is found in the data; empty lets MNE pick automatically. |
| `avg_ref` | bool | `false` | Add an EEG average-reference projector. |
| `no_proj` | bool | `false` | Exclude the SSP projectors already present in the input file before computing the new ones. |
| `event_id` | int | `999` | Event ID to assign to the detected ECG events. |
| `ecg_l_freq` | float | `5` | Low cut-off frequency applied to the ECG channel for event detection, in Hz. |
| `ecg_h_freq` | float | `35` | High cut-off frequency applied to the ECG channel for event detection, in Hz. |
| `tstart` | float | `0.0` | Start artifact detection only after `tstart` seconds into the recording. |
| `qrs_threshold` | string | `"auto"` | QRS detection threshold between 0 and 1, or `"auto"` to pick a threshold that yields a plausible heart rate (40-160 beats/min). |
| `filter_method` | string | `"fir"` | Filtering method used for ECG detection: `"fir"` or `"iir"`. |
| `iir_params` | string | `""` | Parameters for IIR filtering (used only when `filter_method` is `"iir"`); see `mne.filter.construct_iir_filter()`. Empty uses a default 4th-order Butterworth filter. |
| `meg` | string | `"separate"` | Whether to compute MEG projectors `"separate"`ly for magnetometers and gradiometers, or `"combined"` (requires `n_mag == n_grad`). |

## Usage

### Running on Brainlife.io

1. Upload or select your continuous MEG/EEG data file in MNE format (`.fif`)
2. Select the SSP-projectors-ECG app
3. Configure the ECG detection and SSP computation parameters as needed (defaults are reasonable for typical MEG recordings)
4. Submit the task
5. Review the computed projectors and the QC report (topomaps and ECG-evoked plots) once the task completes

### Local Testing

```bash
# Update config.json with your data path and parameters
# Then run:
python main.py
```

## Authors
- Saeed ZAHRAN (saeedzahranutc@gmail.com)
- Maximilien Chaumon (maximilien.chaumon@icm-institute.org)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
