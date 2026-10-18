# Token Usage Report

**Project Directory:** `/home/mt/repos/easyXRD_with_agents/00-Ni/_combined_with_Gemini-3.8-Flash-High`  
**Model:** Gemini 3.8 Flash (High)  
**Total Interactive Model Turns:** 83  

---

## Summary of Token Consumption

| Token Category | Token Count | Percentage of Total | Description |
| :--- | :--- | :--- | :--- |
| **New (Uncached) Input Tokens** | **343,328** | 5.09% | Fresh prompt tokens including tool execution outputs, command logs, and newly read notebook cells |
| **Cached Input Tokens Read** | **6,306,496** | 93.44% | Context tokens retrieved from prefix context cache across sequential refinement turns |
| **Output / Generated Tokens** | **99,671** | 1.48% | Generated model text, reasoning, tool invocations, code cells, and reports |
| **Total Prompt Tokens** | **6,649,824** | 98.52% | Combined prompt context ($343\text{k new} + 6.31\text{M cached}$) |
| **Grand Total Tokens Processed** | **6,749,495** | 100.00% | Cumulative total tokens processed and generated |

---

## Key Efficiency Metrics

- **Context Cache Hit Rate:** **94.8%** of prompt tokens were served via context caching, minimizing latency and compute redundancy during multi-step iterative notebook execution and debugging.
- **Average Prompt Size:** ~80,100 tokens per invocation turn.
- **Average Generated Output:** ~1,200 tokens per invocation turn.
