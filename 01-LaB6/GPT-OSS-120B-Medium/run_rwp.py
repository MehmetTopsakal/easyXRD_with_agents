#!/usr/bin/env python
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
from easyxrd.core import exrd

# Setup sample
sample = exrd(i1d_ylogscale=True, i2d_logscale=False)
sample.load_xrd_data(
    from_xy_file="20260731-124851_A3E69F_count_LaB6_moving.xy",
    poni_file="_calibration.poni",
    radial_range=[1.5, 9.5]
)
# Load phase
sample.load_phases([
    "easyXRD_examples/data/LaB6/LaB6_structure_from_MaterialsProject.cif"
])
# Background object
bkg = exrd(i1d_ylogscale=True, i2d_logscale=False)
bkg.load_xrd_data(
    from_xy_file="20260731-111250_935BAC_count_Air.xy",
    poni_file="_calibration.poni",
    radial_range=[1.5, 9.5]
)
# Baseline
sample.get_baseline(input_bkg=bkg, plot=False)
# GSAS-II setup (instrument parameters from GPX)
sample.setup_gsas2_refiner(instprm_from_gpx="_instrument_parameters.gpx")
# Refine background
refine_str = sample.refine_background(num_coeffs=10, background_type="chebyschev-1", plot=False)
print(refine_str)
