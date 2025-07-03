# Automating experimental optics with sample-efficient machine learning methods
<<<<<<< HEAD
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15800501.svg)](https://doi.org/10.5281/zenodo.15800501)

### 🔗 Links to the paper
=======

### 🔗 Links
>>>>>>> 7a07957ed9babb535f0fd49a78f0a9c9b5a140af
Published in
[Optica](https://doi.org/10.1364/OPTICA.562734)

Also available on 
[arXiv](https://arxiv.org/abs/2503.14260)

## 📊 Project Overview
This project contains the data collected from the experiment through multiple rounds of optimisation. Some of the data here 
This repository contains tools and notebooks for analyzing optical traces collected from photodetector intensity measurements, with a focus on:

- Thermal drift correction in optical traces
- Data visualization with color-coded performance metrics
- Batch processing of experimental data


## 📁 Project Structure

```text
aqua_optics/
├── data_explorer.ipynb         # Main analysis notebook
├── utils.py                    # Core utility functions
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

- `obs`: Optical trace observations (photodetector intensity vs scan position)
- `params`: Experimental parameters used
- `reward`/`costs`: ML agent performance metrics


## 👨‍💻 Author

**Arindam Saha**  
Australian National University (ANU), 2025

- GitHub: [@arindam5aha](https://github.com/arindam5aha)
- Email: <arindam96@outlook.com>

## 📚 Citation

If you use this code in your research, please cite:

```bibtex
@misc{saha2025aquaoptics,
  title={Aqua Optics: ML-Driven Optical Data Analysis},
  author={Saha, Arindam},
  year={2025},
  institution={Australian National University}
}
```

## 🐛 Issues

If you encounter any issues or have suggestions for improvements, please feel free to contact the author.

---

**Last updated:** July 2025
