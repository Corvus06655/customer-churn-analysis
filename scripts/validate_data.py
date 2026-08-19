from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'Customer.csv')
expected = {'customerID', 'Contract', 'TotalCharges', 'Churn'}
assert expected.issubset(df.columns), f'Missing expected columns: {expected - set(df.columns)}'
assert len(df) == 7043, f'Unexpected row count: {len(df)}'
assert int(df['customerID'].duplicated().sum()) == 0, 'Duplicate customer IDs found.'
assert set(df['Churn'].dropna().astype(str).str.strip().unique()) <= {'Yes', 'No'}, 'Unexpected churn labels found.'
charges = pd.to_numeric(df['TotalCharges'].replace(' ', '0'), errors='coerce')
assert charges.notna().all(), 'TotalCharges contains non-numeric values after blank handling.'
churned = df['Churn'].astype(str).str.strip().eq('Yes')
assert int(churned.sum()) == 1869, f'Unexpected churn count: {int(churned.sum())}'
print('Customer Churn validation passed')
print(f'customers={len(df)} churned={int(churned.sum())} churn_rate={churned.mean():.4%}')
