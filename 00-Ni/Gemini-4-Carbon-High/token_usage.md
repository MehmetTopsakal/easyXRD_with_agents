# Token Usage Summary — Ni XRD Rietveld Refinement (`gemini-4-carbon`)

From local session telemetry (`assistant_usage_events`, session `72bda468-5d4a-4408-81a9-338a41fdfab0`, model `gemini-4-carbon`, `reasoning_effort = high`):

| Scope | Calls | Uncached Input | Cache-Read Input | Total Input | Output (incl. Reasoning) | **Total Tokens** |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Turn 1: Pixi preference setup** | 2 | 47,353 | 40,634 | 87,987 | 6,877 (6,474) | **94,864** |
| **Turn 2: Refinement + `.ipynb`** | 50 | 278,663 | 5,329,218 | 5,607,881 | 73,962 (33,887) | **5,681,843** |
| **Turn 3: `walkthrough.md` turn** | 6 | 73,340 | 348,627 | 421,967 | 13,706 (3,830) | **435,673** |
| **Refinement Task Subtotal (Turns 2–3)** | **56** | **352,003** | **5,677,845** | **6,029,848** | **87,668 (37,717)** | **6,117,516** |
| **Turn 4: Token-usage query** | 3 | 14,574 | 208,564 | 223,138 | 3,284 (1,053) | **226,422** |
| **Full Session Subtotal (Turns 1–4)** | **61** | **413,930** | **5,927,043** | **6,340,973** | **97,829 (45,244)** | **6,438,802** |

### Notes
- **Total Input** equals `Uncached Input + Cache-Read Input` (~94.2% of refinement-task input tokens were served from prompt cache).
- **Output** includes internal reasoning tokens (shown in parentheses).
- Turn 2 (`50` calls) and Turn 3 (`6` calls) each include `1` context-compaction call.
