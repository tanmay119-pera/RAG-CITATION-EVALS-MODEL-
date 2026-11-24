# Vector Quantization Benchmarks

## Overview
Evaluating 8-bit uniform scalar quantization (`ScalarQuantizer`) for offline index storage.

## Results
- **Memory Footprint**: 74.8% reduction compared to raw float32 arrays.
- **De-quantization Mean Absolute Error**: < 0.008 per dimension.
- **Top-5 Retrieval Recall Retention**: > 98.4% on golden academic test set.
