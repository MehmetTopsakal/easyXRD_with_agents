# Token & Context Usage Summary

This document details the breakdown of tokens and context metrics spent during the 2D XRD integration and Rietveld refinement task for pure Nickel (Ni).

---

### Token & Context Summary

| Metric | Estimated Count | Details |
| :--- | :---: | :--- |
| **Model** | **Gemini 3.8 Flash** | Medium reasoning effort |
| **Total Transcript Steps** | **88** | User prompts, tool actions, responses, and background tasks |
| **Model Invocations / Turns** | **43** | Model planner response iterations |
| **Unique Generated (Output) Tokens** | **~9,700 tokens** | ~38,700 characters (thinking, code generation, tool calls, and text) |
| **Final Session Context Length** | **~45,000 tokens** | ~181,000 characters (system instructions, tool definitions, logs, outputs) |
| **Cumulative Context Processed** | **~2,610,000 tokens** | Sum of input contexts evaluated across all multi-turn interactions |

---

### Highlights
- **Output Efficiency**: ~9,700 output tokens were generated to inspect the 2D TIFF data, test the pipeline, write and execute the complete [`Ni_Rietveld_Refinement.ipynb`](Ni_Rietveld_Refinement.ipynb) notebook, and extract publication-ready outputs.
- **Context Caching**: For Gemini models, static system instructions and preceding conversation history are largely served via context caching, minimizing incremental compute overhead across turns.
