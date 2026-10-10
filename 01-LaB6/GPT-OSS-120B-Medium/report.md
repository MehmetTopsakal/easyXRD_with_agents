# LaB6 Rietveld Refinement Report

This report summarizes the Jupyter notebook **`LaB6.ipynb`** that performs a full Rietveld refinement workflow for LaB6 using **easyXRD**.

---

## Overview
The notebook demonstrates:
1. Loading the sample and background diffraction patterns (radial range 1–10 Å).
2. Baseline correction using the background.
3. Setting up GSAS‑II with instrument parameters from `_instrument_parameters.gpx`.
4. Sequential refinement of:
   - Background profile (Chebyshev polynomial, order 10).
   - Lattice parameters.
   - Instrument parameters (U, V, W, X, Y, Z, SH/L, Zero).
   - Two alternating background‑+‑cell refinements.
   - A full Rietveld refinement (structure + lattice + all instrument params).
   - Oxygen atomic site (coordinates and isotropic displacement).
5. Final visualization of the refined pattern.

Each step is accompanied by explanatory markdown cells in the notebook, making the workflow easy to follow.

---

## How to Run
```bash
# Activate the Pixi environment (default)
/home/mt/mpixi/.pixi/envs/default/bin/python -m ipykernel install --user --name=easyxrd
# Then launch Jupyter Lab/Notebook in the workspace directory
cd /home/mt/repos/easyXRD_with_agents/01-LaB6/GPT-OSS-120B-Medium
jupyter notebook LaB6.ipynb
```
The notebook will execute each cell sequentially. After the final cell, a plot of the refined diffraction pattern will be displayed.

---

## Key Files
- Notebook: [/home/mt/repos/easyXRD_with_agents/01-LaB6/GPT-OSS-120B-Medium/LaB6.ipynb](file:///home/mt/repos/easyXRD_with_agents/01-LaB6/GPT-OSS-120B-Medium/LaB6.ipynb)
- Instrument parameters: `_instrument_parameters.gpx`
- Sample data: `20260731-124851_A3E69F_count_LaB6_moving.xy`
- Background data: `20260731-111250_935BAC_count_Air.xy`

---

## Expected Output
The final refinement prints the Rietveld result (e.g., R<sub>wp</sub> and GOF) and shows a plot with:
- Observed data (points)
- Calculated pattern (line)
- Difference curve (bottom panel)

---

*This report was generated automatically by the Antigravity assistant.*
