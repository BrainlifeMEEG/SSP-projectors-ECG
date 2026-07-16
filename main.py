"""
Compute ECG artifact SSP projectors.

This app loads raw MEG/EEG data and computes SSP projectors targeting
ECG artifacts via mne.preprocessing.compute_proj_ecg, saving the
projectors and a QC report.

Inputs:
    - mne: Path to MNE raw .fif file
    - tmin, tmax, n_grad, n_mag, n_eeg, l_freq, h_freq, average,
      filter_length, ch_name, avg_ref, no_proj, event_id, ecg_l_freq,
      ecg_h_freq, tstart, qrs_threshold, filter_method, iir_params, meg:
      Parameters forwarded to mne.preprocessing.compute_proj_ecg

Outputs:
    - out_dir/proj.fif: ECG SSP projectors
    - out_figs/ecg_projectors.png: Projector topomap plot
    - out_figs/ecg_*.png: ECG-evoked joint plot figures
    - out_report/report.html: QC report with projectors and ECG-evoked plots
    - product.json: Metadata about the computed projectors
"""

# Copyright (c) 2026 brainlife.io

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne
import matplotlib.pyplot as plt

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    require_config_keys
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir', 'out_figs', 'out_report')

# Load configuration
config = load_config()
require_config_keys(config, ['mne'])

# == LOAD DATA ==
fname = config['mne']
raw = mne.io.read_raw_fif(fname, verbose=False)

ecg_projs, ecg_events = mne.preprocessing.compute_proj_ecg(raw, raw_event=None, tmin=config['tmin'], tmax=config['tmax'], n_grad=config['n_grad'],
            n_mag=config['n_mag'], n_eeg=config['n_eeg'], l_freq=config['l_freq'], h_freq=config['h_freq'], average=config['average'],
            filter_length=config['filter_length'],
            n_jobs=-1, ch_name=config['ch_name'], reject=None, flat=None, bads=[],
            avg_ref=config['avg_ref'], no_proj=config['no_proj'], event_id=config['event_id'], ecg_l_freq=config['ecg_l_freq'], ecg_h_freq=config['ecg_h_freq'],
            tstart=config['tstart'],
            qrs_threshold=config['qrs_threshold'], filter_method=config['filter_method'], iir_params=config['iir_params'], copy=True, return_drop_log=False,
            meg=config['meg'])

mne.write_proj(os.path.join('out_dir', 'proj.fif'), ecg_projs, overwrite=True)

# == FIGURES ==
fig_ep = mne.viz.plot_projs_topomap(ecg_projs, info=raw.info)
topomap_path = os.path.join('out_figs', 'ecg_projectors.png')
fig_ep.savefig(topomap_path)

ecg_evoked = mne.preprocessing.create_ecg_epochs(raw).average()
ecg_evoked.apply_baseline((None, None))

f = ecg_evoked.plot_joint()
joint_paths = []
for i, fig in enumerate(f):
    joint_path = os.path.join('out_figs', f'ecg_{i}.png')
    fig.savefig(joint_path)
    joint_paths.append(joint_path)

report = mne.Report(title='SSP ECG Projectors')
report.add_projs(info=raw.info, projs=ecg_projs, title='SSP ECG Projectors')
for i, fig in enumerate(f):
    report.add_figure(fig, f'ECG Evoked {i}')

report.save(os.path.join('out_report', 'report.html'), overwrite=True)

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, f'Computed {len(ecg_projs)} ECG SSP projector(s)', 'success')
add_image_to_product(product_items, 'ECG projectors topomap', filepath=topomap_path)
create_product_json(product_items)
