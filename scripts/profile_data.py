from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "Customer.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].replace(" ", "0"), errors="coerce")
churned = df["Churn"].astype(str).str.strip().eq("Yes")
print(f"customers={len(df)}")
print(f"columns={len(df.columns)}")
print(f"duplicate_customer_ids={int(df['customerID'].duplicated().sum())}")
print(f"churned_customers={int(churned.sum())}")
print(f"overall_churn_rate={churned.mean():.4%}")
print("churn_rate_by_contract=")
print((df.assign(churned=churned).groupby("Contract")["churned"].mean().sort_values(ascending=False) * 100).round(2).to_string())
print("churn_rate_by_payment_method=")
print((df.assign(churned=churned).groupby("PaymentMethod")["churned"].mean().sort_values(ascending=False) * 100).round(2).to_string())
print("churn_rate_by_internet_service=")
print((df.assign(churned=churned).groupby("InternetService")["churned"].mean().sort_values(ascending=False) * 100).round(2).to_string())
print("churn_rate_by_senior_citizen=")
print((df.assign(churned=churned).groupby("SeniorCitizen")["churned"].mean() * 100).round(2).to_string())
