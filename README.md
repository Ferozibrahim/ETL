# Actuarial Claims Data Pipeline (ETL)

## Overview
An automated Extract, Transform, Load (ETL) pipeline built in Python to process, clean, and standardize raw insurance claims data for actuarial pricing models. 

This project replaces manual Excel data manipulation, demonstrating how to programmatically handle missing values, standardize messy text/dates, and engineer risk-evaluation features.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Openpyxl
* **Environment:** Jupyter Notebook, VS Code

## The Pipeline
1. **Extract:** Generated a mock dataset of 500 messy claims (inconsistent dates, currency strings, missing values) to simulate legacy database exports.
2. **Transform:** 
   * Stripped currency symbols and converted string data to math-ready floats.
   * Standardized chaotic date formats (`pd.to_datetime`).
   * Imputed missing values and rigorously dropped unrecoverable data.
   * Engineered a new `Risk_Band` feature to categorize claims > £25,000 as high-risk.
3. **Load:** Exported the clean, deduplicated, and sorted data into a final `.xlsx` file ready for underwriting analysis.
