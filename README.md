# Automating experimental optics with sample-efficient machine learning methods

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15800501.svg)](https://doi.org/10.5281/zenodo.15800501)

<img src="https://github.com/arindam5aha/aqua_optics/blob/main/figs/Fig_1.svg" width="700"/>

### 🔗 Links to the paper
Published on:
[Optica](https://doi.org/10.1364/OPTICA.562734)

Also available on:
[arXiv](https://arxiv.org/abs/2503.14260)

## 📊 Project Overview
This project contains the data collected from the experiment through multiple rounds of sampling/ optimisation. The data presented here can be used to train ML models for various purposes, including pre-training of AQUA.
This repository contains tools and notebooks for analyzing raw experimental data, with a focus on:

- Thermal drift correction in optical traces
- Data visualization with color-coded performance metrics
- Batch processing of experimental data


## 📁 Project Structure

```text
aqua_optics/
├── data_explorer.ipynb         # Main analysis notebook
├── utils.py                    # Core utility functions
├── figs/                       # Experimental Setup figure
└── env_data/                   # Experimental data directory
    └── sampled_data_*.bz2      # Compressed data files
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

## 🔧 Utilities

### utils.py functions

- `save_bz2()` / `load_bz2()`: Compress/decompress experimental data
- `allign_traces()`: Correct thermal drift in optical measurements
- `argmax_height()`: Find trace with maximum signal amplitude
- `plot_in_dark_mode()`: Configure matplotlib for dark theme
- `topk()`: Extract top-k performing measurements
- `max_till()`: Track cumulative maximum values

## 📈 Data Handling

Basic Data Loading:
```python
from utils import *
path = './env_data/sampled_data_909.bz2'
data = load_bz2(path)
```

Each data file contains:

- `obs`: Cavity traces as observations
- `params`: Experimental control parameters used
- `reward`/`costs`: Raw performance metrics

### Control parameter specs
The bounds below specify the allowed range for each actuator, set by the physical and mechanical limits of the setup. They ensure safe operation and precise control of lens translation and mirror tip/tilt. Values are in actuator enocoder counts.

| Parameter   | Bounds               |
|-------------|----------------------|
| Lens 1      | (-100000, 100000)    |
| Lens 2      | (-100000, 100000)    |
| Mirror 1x   | (-5000, 5000)        |
| Mirror 1y   | (-5000, 5000)        |
| Mirror 2x   | (-5000, 5000)        |
| Mirror 2y   | (-5000, 5000)        |


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
