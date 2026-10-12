# Sales Data Analytics Project

A beginner-friendly Data Analytics project using Python, Pandas, and Matplotlib. It explores a sample retail sales dataset, checks basic data quality, calculates key metrics, and creates charts.

> **Data transparency:** `sales_data.csv` is synthetic practice data generated for learning. It is not actual Thiranex data and does not represent real company performance.

## Project objectives
- Load and inspect a CSV dataset.
- Check missing values and duplicate order IDs.
- Calculate total revenue, order count, units sold, and average order value.
- Compare revenue by product category and city.
- Explore monthly revenue trends.
- Export summary tables and visualisations.

## Tools
- Python 3.10+
- pandas
- matplotlib

## Folder structure
```text
Sales_Data_Analytics_GitHub_Project/
├── sales_data.csv
├── analysis.py
├── requirements.txt
├── README.md
└── outputs/                 # Created when the script runs
```

## How to run

1. Install Python 3.10 or later.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Run the analysis:

   ```bash
   python analysis.py
   ```

The script prints basic results and creates an `outputs` folder containing:
- `overall_summary.csv`
- `sales_by_category.csv`
- `sales_by_city.csv`
- `monthly_sales.csv`
- `revenue_by_category.png`
- `monthly_revenue_trend.png`

## Questions explored
1. What is the total revenue in the sample dataset?
2. Which product category generates the highest revenue?
3. Which city has the highest revenue?
4. How does revenue change month by month?
5. Are there missing values or duplicate order IDs?

## Example findings
Run the script to calculate the exact metrics from the included dataset. Do not copy conclusions from another dataset without rerunning the analysis.

## Limitations
- The dataset is synthetic and relatively small.
- It is intended to demonstrate an analysis workflow, not to make real business decisions.
- Revenue is calculated from the provided quantity, unit price, and discount fields.

## Possible future improvements
- Build an interactive dashboard using Streamlit or Power BI.
- Add profit and cost analysis.
- Add more robust data validation and automated tests.
- Use a real, properly licensed public dataset.

## Academic integrity note
This is a practice portfolio project. If you use it in an academic internship report, describe it accurately as a self-practice/sample project unless it was genuinely assigned or approved by your internship organisation. Do not claim that the synthetic data or project was provided by Thiranex.
