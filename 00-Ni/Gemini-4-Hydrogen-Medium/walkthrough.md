# Walkthrough: Nickel (Ni) 2D XRD Integration and Rietveld Refinement

This walkthrough documents the processing of `Ni.tiff` into a 1D diffraction profile and the full Rietveld refinement performed with `easyxrd` and GSAS-II in [`Ni_Rietveld_Refinement.ipynb`](Ni_Rietveld_Refinement.ipynb).

## 1. Input Files

- `Ni.tiff`: Raw 2D area-detector XRD image (Dexela 2923, $3888 \times 3072$ pixels)
- `_calibration.poni`: pyFAI geometry calibration ($\lambda = 0.1799\ \text{\AA}$, $d \approx 0.5995\ \text{m}$)
- `_mask.edf`: Bad-pixel and detector-gap mask
- `Ni.cif`: FCC Nickel crystal structure ($Fm\bar{3}m$, space group 225, initial $a = 3.525576\ \text{\AA}$)
- `_instrument_parameters.gpx`: Pre-calibrated GSAS-II instrument profile parameters

## 2. 2D-to-1D Azimuthal Integration

Using `exrd.load_xrd_data(...)` with `_calibration.poni` and `_mask.edf`:
- Full-range integration spans $q \in [0.3035, 10.4715]\ \text{\AA}^{-1}$ ($\Delta q = 0.001\ \text{\AA}^{-1}$).
- Restricting `radial_range=[2.0, 10.4]` $\text{\AA}^{-1}$ excludes low-$q$ beamstop/background scattering (including a broad hump near $q \approx 1.5\ \text{\AA}^{-1}$) and detector-corner intensity roll-off above $10.4\ \text{\AA}^{-1}$, while retaining all 11 observed Ni Bragg peaks from `(111)` to `(440)`.
- The integrated 1D profile was exported to [`Ni_1D_q.xy`](Ni_1D_q.xy).

## 3. Phase Matching & Instrument Parameters

- `sample.load_phases([{"cif": "Ni.cif", "label": "Ni"}])` confirmed that all 11 observed Bragg reflections are indexed by cubic $Fm\bar{3}m$ Ni.
- Reading `_instrument_parameters.gpx` via `GSASII.GSASIIscriptable.G2Project` revealed `Y = -1.0844`, which causes the GSAS-II Lorentzian peak width ($\gamma = X/\cos\theta + Y\tan\theta + Z$) to become negative for $q > 7.45\ \text{\AA}^{-1}$ ($2\theta > 12.2^\circ$) and triggers `easyxrd`'s physicality guard (`_invalid_instrument_peak_widths`).
- All calibrated instrument parameters (`Polariz.`, `Azimuth`, `Zero`, `U`, `V`, `W`, `X`, `Z`, `SH/L`) were transferred from `_instrument_parameters.gpx` to `setup_gsas2_refiner(..., normalize=True)`, while `instprm_Y` was clamped to `0.0` so peak widths remain non-negative across $[2.0, 10.4]\ \text{\AA}^{-1}$.

## 4. Refinement Sequence

1. **Le Bail Pre-Refinement**:
   - Initial Le Bail fit: `Rwp = 26.960%`, `GoF = 17.918`
   - 10-coefficient Chebyshev background: `Rwp = 22.567%`, `GoF = 15.007`
   - Unit cell parameter $a$: `Rwp = 10.830%`, `GoF = 7.198`
   - Isotropic crystallite size broadening: `Rwp = 7.361%`, `GoF = 4.893`
2. **Rietveld Refinement**:
   - Switched to Rietveld (`set_LeBail(to=False, refine=True)`): `Rwp = 17.029%`, `GoF = 11.318`
   - Modeled crystallographic texture (visible in the 2D cake `i2d`) using sequential spherical harmonics preferred orientation (`min_gof_improvement=0.1`):
     - `harmonics_order=4`: `Rwp = 15.336%`, `GoF = 10.193`
     - `harmonics_order=6`: `Rwp = 10.264%`, `GoF = 6.823`
     - `harmonics_order=8`: `Rwp = 8.448%`, `GoF = 5.615`
3. **Final Polish**:
   - Unit cell parameters: `Rwp = 7.180%`, `GoF = 4.772`
   - 15-coefficient Chebyshev background: `Rwp = 6.211%`, `GoF = 4.132`
   - Ni isotropic atomic displacement parameter ($U_{\text{iso}}$): `Rwp = 6.048%`, `GoF = 4.020`

## 5. Final Results & Generated Artifacts

- **Final $R_{wp}$ / GoF**: `6.048%` / `4.020` (unit weights)
- **Lattice parameter $a$**: `3.522139(17)` Å (Volume: `43.693759` Å³)
- **Crystallite size (isotropic)**: `0.133` μm
- **Ni $U_{\text{iso}}$**: `0.008558` Å²

### Files Saved in This Directory
- [`Ni_Rietveld_Refinement.ipynb`](Ni_Rietveld_Refinement.ipynb) — Executed Jupyter notebook with all code, logs, and inline plots
- [`Ni_1D_q.xy`](Ni_1D_q.xy) — Integrated 1D diffraction profile ($q$, intensity)
- [`Ni_refined.gpx`](Ni_refined.gpx) — Exported GSAS-II refinement project
- [`Ni_refined.nc`](Ni_refined.nc) — Exported `easyxrd` NetCDF dataset
- [`Ni_Rietveld_plot.pdf`](Ni_Rietveld_plot.pdf) and [`Ni_Rietveld_plot.png`](Ni_Rietveld_plot.png) — Final Rietveld refinement fit plots
- [`walkthrough.md`](walkthrough.md) — This summary walkthrough
