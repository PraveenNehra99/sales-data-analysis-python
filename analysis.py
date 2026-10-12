"""
Sales Data Analytics Project
Note: sales_data.csv contains synthetic practice data, not real company data.
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("sales_data.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["revenue_inr"] = pd.to_numeric(df["revenue_inr"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Basic data-quality checks
print("Rows and columns:", df.shape)
print("\nMissing values by column:\n", df.isna().sum())
print("\nDuplicate order IDs:", df["order_id"].duplicated().sum())

# Remove incomplete rows and duplicate order IDs for this simple exercise
df = df.dropna(subset=["order_id", "order_date", "revenue_inr", "quantity"])
df = df.drop_duplicates(subset=["order_id"])

# Summary tables
total_revenue = df["revenue_inr"].sum()
total_orders = df["order_id"].nunique()
total_units = df["quantity"].sum()
average_order_value = total_revenue / total_orders if total_orders else 0

summary = pd.DataFrame({
    "metric": ["Total Revenue (INR)", "Number of Orders", "Units Sold", "Average Order Value (INR)"],
    "value": [round(total_revenue, 2), int(total_orders), int(total_units), round(average_order_value, 2)]
})
summary.to_csv(OUTPUT_DIR / "overall_summary.csv", index=False)

category_sales = (
    df.groupby("category", as_index=False)["revenue_inr"]
      .sum()
      .sort_values("revenue_inr", ascending=False)
)
category_sales.to_csv(OUTPUT_DIR / "sales_by_category.csv", index=False)

city_sales = (
    df.groupby("city", as_index=False)["revenue_inr"]
      .sum()
      .sort_values("revenue_inr", ascending=False)
)
city_sales.to_csv(OUTPUT_DIR / "sales_by_city.csv", index=False)

monthly_sales = (
    df.assign(month=df["order_date"].dt.to_period("M").astype(str))
      .groupby("month", as_index=False)["revenue_inr"]
      .sum()
      .sort_values("month")
)
monthly_sales.to_csv(OUTPUT_DIR / "monthly_sales.csv", index=False)

# Visualisations
plt.figure(figsize=(8, 5))
plt.bar(category_sales["category"], category_sales["revenue_inr"])
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_by_category.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(monthly_sales["month"], monthly_sales["revenue_inr"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue_trend.png", dpi=150)
plt.close()

print("\nOverall summary:\n", summary.to_string(index=False))
print("\nRevenue by category:\n", category_sales.to_string(index=False))
print(f"\nFinished. Results are saved in: {OUTPUT_DIR.resolve()}")
