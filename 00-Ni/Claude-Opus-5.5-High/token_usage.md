# Token usage — Ni integration & Rietveld task

*Generated 2026-11-01 20:21 (local). Figures are summed from the per-turn token fields in the conversation log (`transcript_full.jsonl`).*

| Scope | Input (new) | Cache-read input | Output |
|---|---|---|---|
| **Ni task** (integration, refinement, notebook) | ~147K | ~2.59M | ~22K |
| `walkthrough.md` | ~7K | ~0.56M | ~4K |
| **Whole conversation so far** | ~172K | ~3.23M | ~28K |

## Notes
- **Cache-read tokens are the largest share.** Each model turn re-reads the conversation context, and those reads are usually billed much more cheaply than new input. The Ni task took 38 model turns.
- **Biggest contributors** were the example notebooks (the first dump included base64 images, ~180 KB), the easyxrd source I read, and the notebook outputs.
- **Output** (~22K for the Ni task) covers replies, tool calls, and the notebook-generator and test scripts.
- These are the token counts the log records. It doesn't include pricing, so no cost figure is given.
