# 📊 Exploratory Data Analysis — Financial Loan Dataset

## 📌 Project Overview

This project focuses on extracting, cleaning, and analysing a financial loan dataset to uncover patterns in borrower behaviour, loan performance, and credit risk indicators.

The dataset originates from a PostgreSQL database dump and simulates a real-world scenario where analysts must extract raw data, standardise it, and prepare it for exploratory data analysis (EDA).

This project demonstrates:

- Data extraction from database dumps
- Schema reconstruction
- Data cleaning and transformation
- Exploratory data analysis preparation
- Version-controlled analytical workflow

---

## 🎯 Project Objectives

- Extract loan payment data from a raw database dump
- Reconstruct dataset schema using SQL definitions
- Clean and standardise dataset structure
- Prepare dataset for exploratory analysis
- Develop insights into loan performance and borrower characteristics

---

## 🧰 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Jupyter Notebook**
- **Git & GitHub**
- **PostgreSQL (schema reference)**

---

## 📂 Project Structure

project_root
│
├── src
│ ├── db_utils.py
│ └── convert_dat_to_csv.py
│
├── data
│ └── loan_payments.csv
│
├── notebooks
│ └── 01_familiarise_data.ipynb
│
├── project-data
│ └── eda_raw_db
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation Instructions

### 1. Clone Repository

git clone <your_repo_link>
cd project_root


---

### 2. Install Dependencies
pip install -r requirements.txt


---

## ▶️ Usage Guide

### Convert Raw Database Dump to CSV

python src/convert_dat_to_csv.py


This script:

- Reads `.dat` database dump files
- Applies schema headers
- Cleans placeholder values
- Outputs a structured CSV file

Output location:

data/loan_payments.csv


---

### Run Exploratory Analysis

Open notebook:

notebooks/01_familiarise_data.ipynb


---

## 🧹 Data Cleaning Steps Completed

- Applied column headers from SQL schema
- Removed dump artefact columns
- Removed placeholder rows
- Standardised missing values
- Corrected ID datatypes
- Prepared dataset for analytical use

---

## 🔍 Exploratory Analysis Focus Areas

Planned analysis includes:

- Loan amount and interest rate distributions
- Borrower credit behaviour patterns
- Loan performance by grade and purpose
- Missing value impact assessment
- Feature relationships influencing repayment behaviour

---

## 📊 Dataset Description

The dataset contains anonymised loan records including:

- Borrower income
- Credit history indicators
- Loan terms and repayment information
- Loan grading and risk classification
- Payment performance metrics

---

## 🧠 Key Skills Demonstrated

- Data extraction from structured dumps
- Schema interpretation and reconstruction
- Data quality assessment
- Data cleaning and transformation
- Analytical documentation
- Version control best practices

---

## 🔐 Security Note

Sensitive connection credentials are excluded via `.gitignore`.

---

## 🚀 Future Improvements

- Advanced data cleaning automation
- Feature engineering for predictive modelling
- Risk classification modelling
- Data visualisation dashboards
- Performance trend analysis

---

## 📜 License

This project is for educational and portfolio purposes.

---

## 👨‍💻 Author

**David Awoyelu**

Aspiring Data Analyst with experience in financial data, analytics, and business intelligence.




