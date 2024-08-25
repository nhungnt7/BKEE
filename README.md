# BKEE: Pioneering Event Extraction in the Vietnamese Language

## Overview

This repository hosts the BKEE dataset, a pioneering resource designed for event extraction in the Vietnamese language. The dataset includes both the raw data and processed data that have been prepared for use in training, development, and testing. 

### Files and Directories

- **data.gz**: This file contains the raw dataset in compressed format.
- **processed/**: This directory contains the processed data, organized into the following files:
  - `train.json`: The training dataset.
  - `dev.json`: The development/validation dataset.
  - `test.json`: The testing dataset.

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

# License

This dataset is licensed under the Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). You are free to use, share, and adapt the data as long as you provide appropriate credit, do not use the material for commercial purposes, and indicate if changes were made.

# Citation

If you use this dataset in your research, please cite the following paper:

```
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