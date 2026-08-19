# Telecom Customer Churn Analysis

A reproducible Python analysis of **7,043 telecom customers** designed to identify observed churn patterns and translate them into retention actions.

> **Portfolio focus:** data cleaning, exploratory analysis, customer segmentation, churn-rate comparison, and business recommendations.

## Business objective

Customer churn reduces recurring revenue and increases acquisition costs. This project examines which customer segments show higher observed churn rates so a retention team can prioritize outreach, contract conversion, and service improvements.

## Dataset and quality

The dataset contains 7,043 customers and 21 columns, with zero duplicate rows. The target field is `Churn`, and the overall observed churn rate is 26.5%. The notebook converts numeric fields such as `TotalCharges`, checks data types, reviews missing values, and uses grouped comparisons to make segment-level patterns visible.

## Visual evidence

![Observed churn rate by contract type](images/churn_contract_rate.png)

## Observed findings

**Overall churn:** 26.5% of customers are marked as churned in the supplied dataset.

**Contract comparison:** month-to-month customers show a 42.7% observed churn rate, compared with 11.3% for one-year contracts and 2.8% for two-year contracts.

**Interpretation:** this is descriptive segmentation, not a causal or production prediction model. Contract type is associated with different churn rates in this dataset, but the project does not claim that contract type alone causes churn.

## Analytical workflow

The notebook inspects the schema, duplicates, missing values, and numeric types; cleans and standardizes fields; calculates overall and grouped churn rates; compares contract, tenure, billing, and service segments; and translates the largest observed differences into retention questions.

## Business recommendations

Use month-to-month customers as the first segment for retention experiments and contract-conversion campaigns. Pair contract analysis with tenure, monthly charges, payment method, and support-service behavior before targeting individual customers. Validate any intervention with a controlled experiment or pre/post measurement rather than assuming an observed association is causal.

## Tools and repository contents

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Jupyter Notebook`

The repository contains `Customer.csv`, the `TCA.ipynb` analysis notebook, the presentation PDF, and the verified chart preview at `images/churn_contract_rate.png`.

## Run locally

Clone the repository, install the dependencies with `pip install -r requirements.txt`, and open `TCA.ipynb` in Jupyter Notebook.

## Limitations and next steps

This is a descriptive portfolio project. A production-ready churn model would require a defined prediction horizon, a time-aware validation split, a baseline model, precision/recall or ROC-AUC reporting, probability calibration, and monitoring for drift. A useful next extension would be a retention cohort analysis or a validated logistic-regression baseline.

---

*Part of Mayank Srivastava's Data Analyst portfolio. Project evidence is intended for learning and portfolio demonstration, not for making decisions about individual customers.*
