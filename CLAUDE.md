# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal Python learning repository focused on data science and machine learning. The codebase is organized into distinct learning modules, each containing Jupyter notebooks and supporting files for different educational topics.

## Development Environment

- **Python Version**: 3.13 (specified in `.python-version`)
- **Package Manager**: uv (uses `pyproject.toml` and `uv.lock`)
- **Virtual Environment**: `.venv` directory

### Setup Commands

```bash
# Install dependencies (production + dev)
uv sync

# Install only production dependencies
uv sync --no-dev

# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>
```

## Running Jupyter Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Start Jupyter Notebook
jupyter notebook

# Run a specific notebook from command line
jupyter execute <notebook-path>
```

## Testing

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests in a specific directory
pytest crashcourse/
```

## Code Quality Tools

```bash
# Format code with black
black .

# Check code style with flake8
flake8 .

# Type checking with mypy
mypy .
```

## Repository Structure

The repository contains three main learning directories:

### 1. `sklearn/` - Machine Learning & Data Science
- Notebooks covering scikit-learn, pandas, numpy, matplotlib, seaborn
- Data files stored in `sklearn/data/`
- Figures/plots stored in `sklearn/figures/`
- Includes MOOC materials (mooc1.ipynb through mooc4a.ipynb)

### 2. `PDA/` - Python Data Analysis
- Notebooks following Python Data Analysis topics (Chapters 1-7)
- Example data files in `PDA/examples/` (CSV, Excel, JSON, HTML, pickle formats)

### 3. `crashcourse/` - Python Crash Course
- Foundational Python learning notebooks (Chapters 1-11)
- Supporting Python scripts demonstrating modules and OOP concepts
- HTML exports of some chapters for viewing

## Key Dependencies

**Data Science Stack:**
- pandas, numpy, scipy - Data manipulation and scientific computing
- scikit-learn - Machine learning algorithms
- matplotlib, seaborn, plotly - Data visualization

**Advanced ML:**
- xgboost, lightgbm, catboost - Gradient boosting libraries
- torch - Deep learning framework
- statsmodels - Statistical modeling

**Development:**
- jupyter, ipykernel - Interactive notebook environment
- pytest - Testing framework
- black, flake8, mypy - Code quality tools

## Working with Notebooks

- All notebooks are organized by topic/chapter within their respective directories
- Data files should remain in their designated subdirectories (`data/`, `examples/`)
- Notebooks may export visualizations to `figures/` subdirectory in sklearn
- When creating new notebooks, follow the existing chapter/topic naming convention
