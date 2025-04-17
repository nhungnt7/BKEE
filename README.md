# BKEE: Pioneering Event Extraction in the Vietnamese Language

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Research Paper](https://img.shields.io/badge/Paper-ACL%20Anthology-blue)](https://aclanthology.org/2024.lrec-main.217)
[![Dataset](https://img.shields.io/badge/Dataset-NLP-green)](https://github.com/nhungnt/BKEE)

## Table of Contents

- [Overview](#overview)
- [Dataset Description](#dataset-description)
- [Data Structure](#data-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)
- [Citation](#citation)

## Overview

BKEE is a pioneering resource designed for Event Extraction in the Vietnamese language. This repository hosts both raw and processed data ready for training, development, and testing machine learning models. The dataset significantly contributes to the field of Vietnamese Natural Language Processing by addressing the notable absence of dedicated resources for event extraction tasks.

## Dataset Description

BKEE encompasses:
- **33+ distinct event types** covering a wide range of domains
- **28 different event argument roles** capturing various semantic roles
- **1,066 labeled documents** with annotations for:
  - Entity mentions
  - Event mentions
  - Event arguments

This comprehensive dataset was developed to establish strong baselines for Vietnamese event extraction tasks and facilitate future research in this domain.

## Data Structure

### Files and Directories

```
BKEE/
├── data.gz                  # Raw dataset in compressed format
└── processed/               # Processed data directory
    ├── train.json           # Training dataset
    ├── dev.json             # Development/validation dataset
    └── test.json            # Testing dataset
```

### JSON Structure

Each processed file contains data in JSON format with the following structure:

```json
{
    "doc_id": "test-00000",
    "sent_id": "test-00000",
    "tokens": ["Chiều", "1/12", ",", "anh", "Đặng Duy Thông", "(", "36", "tuổi", ",", "Công an viên", "xã", "Bà Điểm", ",", "huyện", "Hóc Môn", ")", "chạy", "xe máy", "trên", "đường", "Nguyễn Thị Huê", ",", "huyện", "Hóc Môn", "."],
    "sentence": "Chiều 1/12 , anh Đặng Duy Thông ( 36 tuổi , Công an viên xã Bà Điểm , huyện Hóc Môn ) chạy xe máy trên đường Nguyễn Thị Huê , huyện Hóc Môn .",
    "pieces": ["▁Chiều", "▁1", "/12", ",", "▁anh", "▁Đ", "ặng", "▁Duy", "▁Thông", "▁(", "▁36", "▁tuổi", ",", "▁Công", "▁an", "▁viên", "▁xã", "▁Bà", "▁Điểm", ",", "▁huyện", "▁H", "óc", "▁Môn", "▁)", "▁chạy", "▁xe", "▁máy", "▁trên", "▁đường", "▁Nguyễn", "▁Thị", "▁Hu", "ê", ",", "▁huyện", "▁H", "óc", "▁Môn", "."],
    "token_lens": [1, 2, 1, 1, 4, 1, 1, 1, 1, 3, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 4, 1, 1, 3, 1],
    "entity_mentions": [],
    "event_mentions": [],
    "relation_mentions": []
}
```

#### Field Descriptions

- **doc_id**: Unique document identifier
- **sent_id**: Unique sentence identifier
- **tokens**: Array of tokenized words from the sentence
- **sentence**: Complete text of the sentence
- **pieces**: Subword tokenization (commonly used for transformer models)
- **token_lens**: Length of each token in subwords
- **entity_mentions**: Annotated entities in the text
- **event_mentions**: Annotated events in the text
- **relation_mentions**: Annotated relations between entities

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BKEE.git
cd BKEE
```

2. Extract the raw data:
```bash
gunzip data.gz
```

## Usage

### Basic Data Loading

Example code to load and explore the dataset:

```python
import json

# Load the training data from JSON format
with open('processed/train.json', 'r', encoding='utf-8') as f:
    train_data = json.load(f)  # For standard JSON file

# Alternative: For JSONL format (JSON Lines)
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# Print the first document
print(f"Document ID: {train_data[0]['doc_id']}")
print(f"Sentence: {train_data[0]['sentence']}")
print(f"Number of tokens: {len(train_data[0]['tokens'])}")
```

> **Note:** The processed files may be in either standard JSON or JSONL (JSON Lines) format. The `explore_bkee.py` script uses the JSONL format loader.

### Using the Exploration Script

The repository includes `explore_bkee.py`, a comprehensive utility script for analyzing the BKEE dataset:

1. Run the script:
```bash
python explore_bkee.py
```

2. The script provides various functionalities:
   - Dataset statistics (document counts, token counts, etc.)
   - Analysis of event types, entity types, and argument roles
   - Search capabilities for finding specific event types or entity types
   - Display of example documents with annotations

### Script Features

The `explore_bkee.py` script offers multiple functions for dataset analysis:

```python
# Load data from JSONL files
train_data = load_jsonl('processed/train.json')

# Get dataset statistics
stats = get_dataset_statistics(train_data)
print(f"Documents: {stats['documents']}")
print(f"Event mentions: {stats['event_mentions']}")

# Find examples with event mentions
event_examples = find_examples_with_events(train_data, limit=3)
for example in event_examples:
    display_document(example)

# Analyze event types
event_types = analyze_event_types(train_data)
for event_type, count in event_types.most_common(5):
    print(f"{event_type}: {count} instances")

# Search for specific event types
results = search_by_event_type(train_data, "Conflict:Attack")
```


## License

This dataset is licensed under the [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). You are free to:

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial** — You may not use the material for commercial purposes.

## Citation

If you use this dataset in your research, please cite our paper:

```bibtex
@inproceedings{nguyen-etal-2024-bkee,
    title = "{BKEE}: Pioneering Event Extraction in the {V}ietnamese Language",
    author = "Nguyen, Thi-Nhung  and
      Tran, Bang Tien  and
      Luu, Trong-Nghia  and
      Nguyen, Thien Huu  and
      Nguyen, Kiem-Hieu",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.217",
    pages = "2421--2427",
    abstract = "Event Extraction (EE) is a fundamental task in information extraction, aimed at identifying events and their associated arguments within textual data. It holds significant importance in various applications and serves as a catalyst for the development of related tasks. Despite the availability of numerous datasets and methods for event extraction in various languages, there has been a notable absence of a dedicated dataset for the Vietnamese language. To address this limitation, we propose BKEE, a novel event extraction dataset for Vietnamese. BKEE encompasses over 33 distinct event types and 28 different event argument roles, providing a labeled dataset for entity mentions, event mentions, and event arguments on 1066 documents. Additionally, we establish robust baselines for potential downstream tasks on this dataset, facilitating the analysis of challenges and future development prospects in the field of Vietnamese event extraction.",
}
```

---

<p align="center">
  <small>© 2024 BKEE Team. All rights reserved.</small>
</p>
