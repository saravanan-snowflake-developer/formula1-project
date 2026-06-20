# 🚀 Formula1 Data Engineering Pipeline (Medallion Architecture)

## 📌 Project Overview
This project is an end-to-end **Data Engineering pipeline** built using a **Dockerized Apache Airflow environment** to process and transform the Formula1 dataset in **Azure Cloud** using modern data engineering tools like **Snowflake, dbt, and Airflow**.

The project follows the **Medallion Architecture (Bronze → Silver → Gold)** for scalable and structured data processing.

---

## 🏗️ Architecture

- **Data Source:** Formula1 dataset  
- **Orchestration:** Apache Airflow (Docker)  
- **Data Warehouse:** Snowflake (Azure Cloud)  
- **Transformation Tool:** dbt (Data Build Tool)  

### Medallion Layers:

### 🥉 Bronze Layer
- Raw data ingestion from source systems  
- Data loaded into Snowflake raw tables  

### 🥈 Silver Layer
- Data cleaning and transformation  
- Deduplication and standardization using dbt  

### 🥇 Gold Layer
- Business-ready aggregated datasets  
- Used for reporting and analytics  

---

## ⚙️ Tech Stack

- 🐳 Docker  
- 🌬️ Apache Airflow  
- ❄️ Snowflake (Azure Cloud)  
- 🔧 dbt (Data Build Tool)  
- 🐍 Python  
- 🗄️ SQL  

---

## 🔄 Pipeline Workflow

1. Airflow triggers ingestion DAG  
2. Raw Formula1 data is loaded into Snowflake (Bronze layer)  
3. dbt transforms data into Silver models  
4. Gold layer aggregates data for analytics  
5. Final datasets are ready for BI dashboards  

---

## 📦 Docker Setup

```bash
# Start Airflow containers
docker-compose up -d
