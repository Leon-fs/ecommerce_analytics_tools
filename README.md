# E-commerce Data Analysis Tool

This project is an e-commerce data analysis tool built using Python 3.9. It provides functionalities for loading, preprocessing, analyzing, and visualizing e-commerce data. The tool is designed to help users gain insights from their data and make informed decisions.

## Project Structure

```
ecommerce-data-analysis
├── src
│   ├── ecom_analysis
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   ├── analysis.py
│   │   ├── viz.py
│   │   ├── models.py
│   │   └── utils.py
│   └── scripts
│       └── download_data.py
├── notebooks
│   └── 01-exploratory-analysis.ipynb
├── data
│   ├── raw
│   └── processed
├── tests
│   ├── __init__.py
│   └── test_data_loader.py
├── requirements.txt
├── Pipfile
├── .gitignore
└── README.md
```

## Installation

To set up the project, you need to install the required dependencies. You can do this using Pipenv or by manually installing the packages listed in `requirements.txt`.

### Using Pipenv

1. Install Pipenv if you haven't already:
   ```
   pip install pipenv
   ```

2. Install the dependencies:
   ```
   pipenv install
   ```

### Using requirements.txt

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the data analysis tool, execute the `main.py` file located in the `src/ecom_analysis` directory. This file serves as the entry point for the application.

```bash
python src/ecom_analysis/main.py
```

## Notebooks

The `notebooks` directory contains Jupyter notebooks for exploratory data analysis. You can open and run the notebooks using Jupyter Notebook or Jupyter Lab.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.