# Price Optimization and Elasticity Modeling

## Overview

This repository contains a set of functions and tools for **price optimization** and **price elasticity modeling**. The primary objective is to build econometric models to understand the relationship between price and quantity sold, considering factors such as product category and external parameters. This repository uses **Python** for data manipulation, analysis, and optimization, and includes **Jupyter Notebooks** for easy experimentation and visualization.

The key functionality includes:
- Price elasticity estimation.
- Price optimization for maximizing quantity sold.
- Usage of **linear programming** for optimization.
- Model parameters managed in a YAML configuration file.
  
## Key Components

1. **`src/`**: This folder contains all source code for data processing, modeling, and utilities.
   - **`exploratory.py`**: Functions for performing exploratory data analysis (EDA).
   - **`econometric_model.py`**: Functions to develop econometric models for price elasticity.
   - **`optimization.py`**: Functions to implement linear programming for price optimization.

2. **`conf/`**: Contains configuration files, including parameter settings for modeling and optimization.
   - **`parameters.yaml`**: YAML file to store the parameters like price change range, product categories, and others.

3. **`notebooks/`**: Jupyter Notebooks for interactive analysis, modeling, and optimization.
   - **`modeling.ipynb`**: The notebook for building and analyzing the price elasticity model.
   - **`optimize.ipynb`**: The notebook to run optimization for price adjustments based on the elasticity model.

4. **`data/`**: Folder to store raw and processed data. (Typically `.csv`, `.xlsx`, or other formats)
   - **`raw/`**: Raw input data files.
   - **`processed/`**: Cleaned and preprocessed data files ready for modeling.

5. **`requirements.txt`**: Lists all required Python dependencies for the project.

## Setup and Installation

### Prerequisites
- Python 3.7+
- Git
- Virtual environment tool (e.g., `venv` or `conda`)

### Steps to Set Up the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/price-optimization.git
   cd price-optimization    
   ```

2. Create a virtual environment (optional but recommended):    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install required dependencies:    
    ```bash
    pip install -r requirements.txt
    ```

## File Structure

    price-optimization/
    │
    ├── src/
    │   ├── exploratory.py
    │   ├── econometric_model.py
    │   └── optimization.py
    │
    ├── conf/
    │   └── parameters.yaml
    │
    ├── notebooks/
    │   ├── modeling.ipynb
    │   └── optimize.ipynb
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── requirements.txt
    └── README.md

## Contribution
Feel free to fork this repository and contribute! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


