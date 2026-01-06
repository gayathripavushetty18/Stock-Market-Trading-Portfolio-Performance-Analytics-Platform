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

## 🌀 Apache Airflow Orchestration

Apache Airflow is used to **orchestrate the Databricks ETL job**, where triggering the DAG in Airflow automatically runs the **Bronze → Silver → Gold** pipeline in Databricks.

### 🔄 Workflow Overview

* Airflow DAG triggers a Databricks Job (`ETL_for_stocks`)
* Databricks executes tasks sequentially:
<img width="1915" height="995" alt="image" src="https://github.com/user-attachments/assets/6d886237-dd48-4dcf-be92-6279cd736619" />

  * **Bronze** – Raw stock data ingestion
  * **Silver** – Data cleaning & transformation
  * **Gold** – Aggregated analytics for reporting
* Each DAG run results in a successful Databricks job execution, as shown in the monitoring view.

> *This setup ensures reliable scheduling, dependency management, and observability for the ETL pipeline.*

---

### 🛠 Airflow Setup (Docker-based)

The following Docker Compose commands were used to initialize and manage Airflow locally:

```bash
# Initialize Airflow metadata database
docker compose run --rm airflow-webserver airflow db init

# Create Airflow admin user
docker compose run --rm airflow-webserver airflow users create \
  --username admin \
  --firstname Gayathri \
  --lastname Pavushetty \
  --role Admin \
  --email gayathri@example.com \
  --password admin

# Start all Airflow services (webserver, scheduler, etc.)
docker compose up -d

# Stop and clean up Airflow services
docker compose down
```

### 🔐 Airflow Access

* **URL:** `http://localhost:8080`
* **Username:** `admin`
* **Password:** `admin`

---

### 📸 Reference

**Airflow-Triggered Databricks ETL Job Execution**
*(Triggering the DAG in Airflow automatically runs the Databricks job with Bronze, Silver, and Gold tasks.)*

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
├── databricks/            # Databricks notebooks for Bronze–Silver–Gold layers
├── powerbi/
│   └── Stock Market Trading & Portfolio Performance.pbix
├── README.md

```
---

## 🏗️ Data Processing & ETL (30%)
<img width="723" height="661" alt="ETL pipeline" src="https://github.com/user-attachments/assets/c2143a91-fba4-4935-9c83-7ca78bba985c" />

A structured **Bronze–Silver–Gold ETL pipeline** is implemented using **Azure Databricks and Delta Live Tables**.
Raw stock prices and portfolio transactions are ingested into Bronze streaming tables, cleansed and standardized in the Silver layer.
The Gold layer produces aggregated analytical tables such as portfolio metrics, sector allocation, stock volatility, and portfolio summary.
The Databricks pipeline graph illustrates **data lineage, dependencies, and successful execution** across all ETL stages.

---
## 🔹 Logging, Monitoring & Observability

Execution-level logging and monitoring are handled by Apache Airflow and Databricks, which automatically capture task execution details, failures, and retry events, without requiring custom logging logic in the application code.

Airflow provides detailed logs for DAG parsing, task execution, retries, and failures, while Databricks captures job execution logs, Spark driver logs, and executor logs through its managed runtime environment.

---

## 📊 Dashboards & Visual Analytics

The project includes **three interactive Power BI dashboards** that provide end-to-end insights into stock performance, portfolio allocation, and market risk. These dashboards are built on the **Gold layer** outputs from the Databricks ETL pipeline.

---


### 📈 Stock Market Trends Dashboard
<img width="1268" height="714" alt="image" src="https://github.com/user-attachments/assets/01778f07-0c86-4d2e-b4ca-15a779d57fe0" />

**Purpose:** Analyze long-term price and volume behavior of selected stocks.

**Key Insights:**

* Year-wise **stock price trends**
* **Trading volume trends** over time
* **Moving averages** to smooth price fluctuations
* Stock-level slicer for interactive comparison (AAPL, GOOGL, JPM, MSFT)

**Business Value:**
Helps understand historical performance, momentum, and market activity for informed investment decisions.

---


### 💼 Portfolio Performance Dashboard
<img width="1259" height="713" alt="image" src="https://github.com/user-attachments/assets/cef84a1a-b1c5-4823-af43-3874c9085438" />
**Purpose:** Evaluate overall portfolio value and stock-wise contribution.

**Key Insights:**

* Total portfolio value
* Average investment per stock
* Number of stocks in the portfolio
* Investment allocation by stock
* Percentage contribution of each stock
* Detailed portfolio holdings table

**Business Value:**
Provides a clear snapshot of portfolio composition, diversification, and capital distribution.

---


### ⚠️ Risk & Market Insights Dashboard
<img width="1258" height="713" alt="image" src="https://github.com/user-attachments/assets/9c5b4b80-2d49-47c7-97e8-9616010698b4" />
**Purpose:** Assess portfolio exposure and risk across sectors and time.

**Key Insights:**

* Stock risk ranking trends over time
* Sector-wise market exposure
* Sector-wise investment allocation
* Risk intensity heatmap (monthly, per stock)
* Sector exposure trends (Technology vs Finance)

**Business Value:**
Enables identification of high-risk stocks, sector concentration, and potential over-exposure.

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
