# Vendor-performance-analysis


## 📌 Project Overview
This project focuses on **analyzing vendor performance** using **Python, SQL, and Power BI**.  
The workflow includes **data ingestion from multiple sources (5 tables)**, data preprocessing, **summary table creation**, logging for process tracking, and visualization in **Power BI**.  

The objective is to evaluate vendors across dimensions like purchase contribution, sales performance, stock turnover, and lead time. The insights are delivered through an **interactive Power BI dashboard**.

---

## 🎯 Objectives
- Ingest and consolidate data from **multiple raw tables** into a structured summary.  
- Perform **data cleaning, transformation, and logging** for traceability.  
- Build a **summary table** capturing vendor KPIs.  
- Conduct **EDA (Exploratory Data Analysis)** in Python.  
- Create an **interactive Power BI dashboard** for decision-making.  

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Logging) → Data ingestion, EDA, summary table, logging  
- **SQL** → Data querying and transformation  
- **Power BI** → Dashboard development  
- **Jupyter Notebook** → Step-by-step analysis  

---


---

## 🔑 Workflow & Methodology

### 1. Data Ingestion
- Read **5 different raw tables** (purchase, sales, lead time, stock, vendor master).  
- Implemented a **logging system** to record each step of the ingestion process.  
- Logged details include:  
  - Timestamp of ingestion  
  - Number of records read  
  - Any missing/invalid values  

### 2. Data Cleaning & Transformation
- Standardized column names and formats.  
- Handled missing values and outliers.  
- Normalized numerical fields (purchase values, sales quantities).  

### 3. Summary Table Creation
- Combined the **5 raw tables** into a **single summary table**.  
- Metrics included in summary:  
  - Total Purchase  
  - Total Sales  
  - Purchase Contribution %  
  - Stock Turnover  
  - Lead Time (average & deviation)  

### 4. Exploratory Data Analysis (EDA)
- Used Pandas and Matplotlib/Seaborn to:  
  - Analyze vendor contribution distribution  
  - Identify slow-moving stock (low turnover)  
  - Compare sales vs purchase trends  
  - Detect vendors with delayed lead times  

### 5. Dashboard Development (Power BI)
- Imported summary table into Power BI.  
- Built visuals including:  
  - **Top 10 vendors by purchase contribution**  
  - **Stock turnover distribution**  
  - **Lead time delays**  
  - **Sales vs purchase trends**  
- Created filters and slicers for dynamic exploration.  

---

## 📊 Dashboard Preview
![Dashboard Preview]

---

## 📈 Insights & Results
- Identified **top 10 vendors** contributing the most to purchases.  
- Found vendors with **very low stock turnover**, leading to excess stock.  
- Detected **lead time delays** from specific vendors.  
- Built a **Power BI dashboard** that allows real-time vendor performance monitoring.  

---

## 🚀 Future Improvements
- Automate ingestion pipeline with real-time data updates.  
- Add machine learning models for vendor risk prediction.  
- Extend dashboard to multi-year vendor performance tracking.  
- Integrate automated email alerts for vendors with poor performance.  

---

## 👨‍💻 Contributions
- **Data Ingestion & Logging** – Read and tracked ingestion of 5 raw tables.  
- **Data Cleaning & Transformation** – Handled preprocessing and normalization.  
- **Summary Table Creation** – Consolidated metrics into 1 master dataset.  
- **Exploratory Data Analysis** – Conducted KPI-based analysis in Jupyter Notebook.  
- **Dashboard Development** – Built interactive Power BI dashboard.  
- **Project Documentation** – Created project report and README.  

---

## 📌 How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/vendor-performance-analysis.git
2.Open the Jupyter Notebook:

3.Explore the Power BI dashboard (.pbix file in Dashboard/ folder).

4.Read the Report.pdf for detailed methodology and results.
       
# License

This project is open-source and available under the MIT License.
