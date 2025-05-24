# GREval-Bench
GREval-Bench enables an in-depth evaluation of both traditional aligned-base models and existing general MLLMs through two types of assessments:

1. Coarse-grained (e.g., country, continent) and fine-grained (e.g., city, street) localization performance
2. Chain-of-Thought quality

---
### Data Download
GREval-Bench: 🤗 [download](https://huggingface.co/datasets/Anonymous0515/GREval-Bench).

Data structure:
```bash
benchmark
├── bench_data
│   ├── GREval-Bench.json
│   └── imgs
└── eval.py
```

### Data Format
The data format organized in the benchmark json file is as below:

```json
[
    {
        "sample_id": "sample_id",
        "image_path": "image_path",
        "gt_cot": "{gt_cot}",
        "gt_lat": {gt_lat},
        "gt_lon": {gt_lon}  
        
    }
    ...
]
```
