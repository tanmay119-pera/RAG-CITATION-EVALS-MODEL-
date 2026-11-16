# RAG System Failure Analysis and Diagnostics

Total Evaluated Cases: 60
Total Diagnosed Failures: 8
System Success Rate: 86.7%

## Diagnostic Breakdown

- **FALSE_REFUSAL**: 3 instances
- **MISSED_REFUSAL**: 5 instances

## Detailed Log

| Case ID | Mode | Query | Details |
|---|---|---|---|
| `eval_19` | `FALSE_REFUSAL` | What is the grade point value for a B+?... | Refused an answerable question. |
| `eval_20` | `FALSE_REFUSAL` | What percentage score corresponds to a letter... | Refused an answerable question. |
| `eval_46` | `FALSE_REFUSAL` | What outstanding balance threshold causes an ... | Refused an answerable question. |
| `eval_neg_03` | `MISSED_REFUSAL` | What is the university policy on drone delive... | Answered unanswerable query. |
| `eval_neg_04` | `MISSED_REFUSAL` | How many Bitcoin mining rigs are allowed per ... | Answered unanswerable query. |
| `eval_neg_06` | `MISSED_REFUSAL` | What brand of espresso beans is provided in t... | Answered unanswerable query. |
| `eval_neg_09` | `MISSED_REFUSAL` | Can students use quantum entanglement communi... | Answered unanswerable query. |
| `eval_neg_12` | `MISSED_REFUSAL` | Does the student recreation center offer free... | Answered unanswerable query. |
