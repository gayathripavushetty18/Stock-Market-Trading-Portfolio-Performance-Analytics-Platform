# Stock Market Trading & Portfolio Performance Analytics Platform

An end-to-end data engineering and analytics platform designed to process, analyze, and curate stock market and portfolio performance data using scalable, production-grade architectures.

![Airflow](https://img.shields.io/badge/Airflow-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


---

## 📖 Project Overview

This project focuses on building a robust stock market analytics pipeline that transforms raw financial time-series data into curated, analytics-ready datasets. The platform is designed following modern data engineering best practices and supports downstream reporting, portfolio evaluation, and market insight generation.

The solution emphasizes scalability, data quality, and modularity, making it suitable for real-world financial analytics use cases.

---

## 🎯 Business Objectives

- Analyze historical stock price movements across multiple companies  
- Evaluate portfolio performance and investment exposure  
- Generate return, trend, and risk-related financial metrics  
- Enable decision-ready datasets for dashboards and analytics  

---

## 🛠️ Technology Stack

- **Python** – Data ingestion and validation  
- **Pandas** – Time-series feature engineering  
- **Apache Spark (PySpark)** – Scalable data processing  
- **Delta Lake** – Reliable storage with ACID compliance  
- **Azure Databricks** – Distributed analytics platform  
- **Apache Airflow** – Workflow orchestration  
- **Docker & Docker Compose** – Containerized Airflow setup  
- **Power BI** – Data visualization and reporting  

---

## 🏗️ High-Level Architecture

```text
Raw CSV Data
     ↓
Python Ingestion & Validation
     ↓
Bronze Layer (Delta Tables)
     ↓
Silver Layer (Cleaned & Enriched)
     ↓
Gold Layer (Aggregated Business Metrics)
     ↓
Power BI Dashboards
````

---

## ⏱️ Workflow Orchestration (Apache Airflow)

Apache Airflow is used to orchestrate and trigger Databricks Serverless jobs responsible for executing the ETL pipeline.

### Key Highlights:

* Dockerized Airflow setup using `docker-compose`
* LocalExecutor with Postgres metadata database
* DAG triggers Databricks Serverless jobs via `DatabricksRunNowOperator`
* Supports retry logic and failure handling
* Enables modular and automated pipeline execution

---

## 📂 Repository Structure

```text
├── airflow/
│   ├── airflow-dags/
│   │   └── stocks.py
│   ├── airflow-logs/
│   ├── airflow-plugins/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── requirements.txt
│
├── notebooks/
│   ├── bronze_layer.ipynb
│   ├── silver_layer.ipynb
│   └── gold_layer.ipynb
│
├── data/
│   ├── raw/
│   │   ├── stocks/
│   │   │   ├── AAPL.csv
│   │   │   ├── GOOGL.csv
│   │   │   ├── JPM.csv
│   │   │   └── MSFT.csv
│   │   └── portfolio/
│   │       └── portfolio_transactions.csv
│   │
│   └── processed/
│       ├── clean_stock_data.csv
│       └── stock_analytics_pandas.csv
│
├── src/
│   ├── ingestion/
│   │   └── ingest_stock_data.py
│   │
│   ├── transformation/
│   │   └── pandas_time_series.py
│   │
│   └── utils/
│       └── generate_datasets.py
│
├── databricks/               # Databricks notebooks for Bronze–Silver–Gold layers
├── powerbi/
│   └── Stock Market Trading & Portfolio Performance.pbix
├── airflow/                  # Airflow DAGs and Docker setup
├── README.md

```
---
## 🔹 Logging, Monitoring & Observability

Execution-level logging and monitoring are handled by Apache Airflow and Databricks, which automatically capture task execution details, failures, and retry events, without requiring custom logging logic in the application code.

Airflow provides detailed logs for DAG parsing, task execution, retries, and failures, while Databricks captures job execution logs, Spark driver logs, and executor logs through its managed runtime environment.

---

## 📊 Analytics & Metrics

The platform computes and exposes the following analytics:

* Daily and cumulative returns
* Short-term and long-term moving averages
* Volatility and risk indicators
* Stock-wise performance trends
* Portfolio-level investment exposure

---

## 📈 Dashboards

The curated Gold-layer datasets are used to build interactive dashboards, including:

* **Executive Market Overview**
* **Portfolio Performance Dashboard**
* **Risk & Market Insights Dashboard**


---

## 🚀 Future Enhancements

* Real-time stock data ingestion using APIs
* Advanced risk modeling and factor analysis
* Machine learning-based price forecasting
* Automated data quality monitoring
* CI/CD integration for pipelines

---

## 👤 Author

**Gayathri Pavushetty**
Stock Market Trading & Portfolio Performance Analytics Platform
