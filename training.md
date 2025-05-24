# Dataset Preparation

- GRE30K 🤗 [download](https://huggingface.co/datasets/Anonymous0515/GRE30K).

| Data | Size |
| --- | ---: |
| gre_cot.json | xx MB |
| gre_judge.json |  xx MB |
| gre_seed.json |  xx MB |

After downloading all of them, organize the data as follows in `./dataset`:

```
├── gre_cot
│   ├── gre_cot.json
│   └── imgs
├── gre_judge
│   ├── gre_judge.json
│   └── imgs
└── gre_seed
    ├── gre_seed.jsonl
    └── imgs
```

