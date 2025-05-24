# 📊 Evaluation for GRE 

This document provides instructions on evaluating GRE on the image geo-localization task and GREval-Bench.

## 1. Image Geo-localization
We test three benchmarks, Im2GPS3k, Google World Streets 15k (GWS15k) and Google StreetView.

Evaluation data structure:
```
eval
├── eval_data
│   ├── Im2GPS3k # Official website:
│   │   └── test
│   │       ├── img
│   │       └── label
│   ├── GWS15k # Official website:
│   │   └── test
│   │       ├── img
│   │       └── label
│   └── Google_StreetView # Official website:
│       └── test
│           ├── img
│           └── label
└── output # The output of the model
```

Running command:

```bash
# Im2GPS3k evaluation
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/eval/eval_img2gps3k.sh
# GWS15k evaluation
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/eval/eval_gws15k.sh
# Google StreetView evaluation
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/eval/eval_google_streeview.sh
```

## 2. GREval-Bench
Please prepare the datasets and annotations used for evaluation, as outlined in [GREval-Bench](../benchmark/README.md).

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/eval_bench/eval_greval-bench.sh
```