# Automating experimental optics with sample-efficient machine learning methods

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15800501.svg)](https://doi.org/10.5281/zenodo.15800501)

![Experimental setup figure](figs/fig_1.svg)

### 🔗 Links to the paper
Published on:
[Optica](https://doi.org/10.1364/OPTICA.562734)

Also available on:
[arXiv](https://arxiv.org/abs/2503.14260)

## 📊 Project Overview
This project contains the data collected from the experiment through multiple rounds of optimisation. The data presented here can be used to train ML models for various purposes, including pre-training of AQUA.
This repository contains tools and notebooks for analyzing raw experimental data, with a focus on:

- Thermal drift correction in optical traces
- Data visualization with color-coded performance metrics
- Batch processing of experimental data


## 📁 Project Structure

```text
aqua_optics/
├── data_explorer.ipynb         # Main analysis notebook
├── utils.py                    # Core utility functions
├── env_data/                   # Experimental data directory
|   └── sampled_data_*.bz2      # Compressed data files
└── figs/                       # Experimental Setup figure

```

## 🚀 Getting Started

### Prerequisites

```bash
pip install numpy matplotlib scipy bz2 pickle glob
```

### Installation

```bash
git clone https://github.com/arindam5aha/aqua_optics.git
cd aqua_optics
```

## 🔧 Key Functions

### utils.py Functions

- `save_bz2()` / `load_bz2()`: Compress/decompress experimental data
- `allign_traces()`: Correct thermal drift in optical measurements
- `argmax_height()`: Find trace with maximum signal amplitude
- `plot_in_dark_mode()`: Configure matplotlib for dark theme
- `topk()`: Extract top-k performing measurements
- `max_till()`: Track cumulative maximum values

## 📈 Data Format

Each data file contains:

- `obs`: Optical traces as observations
- `params`: Experimental control parameters used
- `reward`/`costs`: Raw performance metrics


## 👨‍💻 Author

**Arindam Saha**  
Australian National University (ANU), 2025

- GitHub: [@arindam5aha](https://github.com/arindam5aha)
- Email: <arindam96@outlook.com>
- Linkedin: [@arindams96](https://www.linkedin.com/in/arindams96/)

## 🐛 Issues

If you encounter any issues or have suggestions for improvements, please feel free to contact the author.

---

**Last updated:** July 2025
