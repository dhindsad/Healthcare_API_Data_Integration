# Healthcare API Data Integration Pipeline

## Overview
This project demonstrates an API-based healthcare data pipeline using Python. The pipeline extracts healthcare data from a public API, cleans and transforms the dataset, validates data quality, loads the data into SQLite, and prepares outputs for reporting.

This project simulates API-based healthcare data exchange concepts similar to modern healthcare interoperability workflows such as FHIR.

## Tools Used
- Python
- Pandas
- Requests
- SQLite

## Pipeline Architecture
API Extract → Transform → Validate → Load

## Workflow

### 1. Extract
- Connected to a public healthcare API using Python requests
- Retrieved data in CSV format
- Saved raw API data locally

### 2. Transform
- Cleaned column names
- Removed duplicate records
- Handled missing values
- Created processed dataset for reporting

### 3. Validate
- Checked missing values
- Checked duplicate records
- Confirmed dataset structure

### 4. Load
- Loaded cleaned API data into SQLite database
- Generated summary report for validation and reporting

## Outputs
- Raw data: data/raw/api_health_data.csv'
- Clean data: `data/processed/clean_api_health_data.csv`
- Database: `outputs/api_health_database.db`
- Summary report: `outputs/api_health_summary_report.csv`
