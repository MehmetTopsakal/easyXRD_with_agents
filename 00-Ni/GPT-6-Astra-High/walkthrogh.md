# Ni image integration and Rietveld refinement walkthrough

Completed on 2026-10-06 using the user's Pixi environment at `/home/mt/mpixi`.

The executed [Ni_Rietveld_refinement.ipynb](Ni_Rietveld_refinement.ipynb) documents the calculations, plots, and validation. Its nine code cells completed without errors. The workflow follows the [easyXRD examples](https://github.com/MehmetTopsakal/easyXRD_examples), particularly the basic and intermediate notebooks, adapted to the installed library API. The local examples checkout was at commit `97dec4ef8260006ebe8a00b78da2bbf55d9cd5ff`.

## Inputs

| File | Purpose |
| --- | --- |
| `Ni.tiff` | Two-dimensional detector image |
| `_calibration.poni` | pyFAI detector geometry and wavelength |
| `_mask.edf` | Bad-pixel mask; nonzero pixels excluded |
| `Ni.cif` | Starting Ni structure and phase matching |
| `_instrument_parameters.gpx` | Reference GSAS-II instrument parameters |

The calibration and instrument project both specify **λ = 0.1799 Å**. The image has 3,888 × 3,072 pixels; the supplied mask excludes 54,514 pixels. The original input files were preserved and their SHA-256 hashes recorded.

## 1. Integrate the detector image

The notebook loads the image with Fabio and the geometry with pyFAI, then uses easyXRD's direct one-dimensional integration path (`integrate2d=False`). It applies the supplied mask, excludes nonfinite pixels, and enables solid-angle correction. Negative finite values are retained because the TIFF contains corrected floating-point intensities.

Integration settings:

- Range: **q = 0.5–10.4 Å⁻¹**.
- Bin spacing: **Δq = 0.004 Å⁻¹**.
- Method: bounding-box pixel splitting, CSR, Cython.
- No added dark subtraction, flat-field correction, median filtering, or polarization correction.

A separate azimuthal cake is generated for inspection. The exported 1D profile comes directly from contributing detector pixels, rather than an equally weighted average of cake rows. No background is subtracted from these exports.

The profile is saved in q and 2θ formats. A diagnostic azimuthal standard error is included in the CSV. Because no detector variance or gain model was supplied, refinement uses **relative weights `w = 1 / max(I, 1)`**. The XYE file's third column is `sqrt(max(I, 1))`, a weighting proxy rather than a measured uncertainty.

## 2. Match the Ni phase

Predicted peaks from the supplied CIF are compared with observed maxima using pymatgen. The pattern supports face-centered cubic Ni, **Fm-3m (No. 225)**, as the major crystalline phase. Peak matching is recorded in `Ni_results/Ni_phase_matches.csv`.

The refinement uses **q = 2.5–9.5 Å⁻¹**, comprising 1,750 points. This excludes diffuse scattering below the first Ni peak and the sparsely covered outer detector corners.

## 3. Perform Rietveld refinement

The notebook imports instrument parameters from the supplied GPX and explicitly sets **`LeBail=False` before refinement**, so calculated intensities depend on the Ni structure.

The model is refined in stages:

1. Histogram scale and eight Chebyshev background coefficients.
2. Cubic lattice parameter.
3. Gaussian profile coefficients U, V, W.
4. Lorentzian profile coefficients X, Y.
5. A diagnostic unconstrained Ni Uiso trial.
6. A physical model with Uiso fixed to zero, followed by analytic-Jacobian polishing and a repeat-cycle stability check.

Wavelength, zero offset, polarization, Z, and SH/L remain fixed to their imported values. Ni coordinates and full occupancy remain fixed. The nominal crystallite size is fixed at 10 μm and microstrain at zero; the fitted profile terms therefore describe total broadening, without independently determining size or strain.

| Stage | Optimizer Rwp (%) |
| --- | ---: |
| Scale and background, reference profile | 26.698 |
| Add lattice parameter | 22.220 |
| Add U, V, W | 9.868 |
| Add X, Y | 7.297 |
| Unconstrained Uiso diagnostic | 6.016 |
| Joint model with Uiso = 0 | 6.228 |
| Final polish and stability check | 6.222 |

The unconstrained Uiso trial gave **−0.0013465 Å²**, which is unphysical. That diagnostic model was rejected as the accepted structural result. Uiso was fixed at its lower physical boundary, zero, and the remaining parameters were refitted.

## 4. Final result

| Quantity | Result |
| --- | ---: |
| Phase / space group | Ni / Fm-3m |
| a = b = c | **3.522678 Å** |
| Formal lattice standard uncertainty | 0.000032 Å |
| Unit-cell volume | 43.713823 Å³ |
| Rwp, recomputed from saved profile | **6.2231%** |
| Rp | 4.7958% |
| GOF using relative weights | 0.3096 |
| Final refined parameters | 15 |
| Uiso | 0 Å², fixed |

The cached optimizer Rwp is 6.2220%; regenerating the saved profile gives 6.2231%. Validation checks the latter against the saved histogram's own residual statistic.

Residual intensity and peak-shape mismatch remains. U/V/W and X/Y are strongly correlated, with some absolute correlations above 0.95. The formal lattice error excludes calibration and other systematic uncertainties. The PONI itself identifies Ni as its calibrant, so this result is not an independent validation of the absolute length scale. GOF is not a calibrated statistical test with these proxy weights. The fit does not establish thermal displacement, crystallite size, microstrain, or quantitative phase purity.

## 5. Validation and saved files

The notebook checks finite profiles and covariance, positive fit weights, positive Gaussian and Lorentzian width functions across the fit range, stable repeated refinement, and Rietveld mode. It reopens the saved GPX and CIF to check consistency and verifies that input hashes are unchanged.

| Output | Contents |
| --- | --- |
| [Ni_Rietveld_refinement.ipynb](Ni_Rietveld_refinement.ipynb) | Executed workflow and embedded figures |
| [Ni_integrated_profile.csv](Ni_results/Ni_integrated_profile.csv) | q, 2θ, intensity, proxy and diagnostic uncertainties, pixel counts |
| [Ni_2theta.xy](Ni_results/Ni_2theta.xy) / [Ni_q.xy](Ni_results/Ni_q.xy) | Two-column integrated profiles |
| [Ni_2theta.xye](Ni_results/Ni_2theta.xye) | 2θ, intensity, and explicitly approximate uncertainty proxy |
| [Ni_Rietveld.gpx](Ni_results/Ni_Rietveld.gpx) | Accepted refinement project |
| [Ni_refined.cif](Ni_results/Ni_refined.cif) | Final Ni structural model |
| [Ni_fit_profile.csv](Ni_results/Ni_fit_profile.csv) | Observed, calculated, background, difference, and weights |
| [Ni_Rietveld_fit.png](Ni_results/Ni_Rietveld_fit.png) / [PDF](Ni_results/Ni_Rietveld_fit.pdf) | Final fit and residual plots |
| [Ni_summary.json](Ni_results/Ni_summary.json) | Numerical results and limitations |
| [Ni_provenance.json](Ni_results/Ni_provenance.json) | Versions, input hashes, and processing settings |
| [Ni_refinement_history.csv](Ni_results/Ni_refinement_history.csv) | Refinement-stage results |

Additional detector, integration, phase-matching, and peak-detail figures are in `Ni_results/`. `Ni_fixed_reference_profile.gpx` preserves the comparison before profile adjustment. `Ni_diagnostic_Uiso_trial.gpx` contains the unphysical diagnostic trial and is **not the accepted result**. Working GSAS-II projects and logs are retained under `Ni_results/gsas_work/`.

## Rerun

Open the notebook in its current directory, select a kernel using `/home/mt/mpixi/.pixi/envs/default/bin/python`, and run all cells. Keep all five input files beside the notebook. Use `pixi run --manifest-path /home/mt/mpixi/pixi.toml <command>` when environment activation is needed. Rerunning updates the named exports in `Ni_results/` and creates another GSAS-II working directory.
