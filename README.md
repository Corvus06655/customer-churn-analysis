# Customer Churn Analysis — Telecom Retention Case Study

A Python and Pandas analysis of telecom customer behavior, focused on identifying churn patterns that can support retention prioritization. The project examines contract type, tenure, services, billing behavior, payment method, and customer charges.

> **Portfolio focus:** data cleaning, segmentation, churn-rate measurement, contract comparison, retention reasoning, and visual communication.

## Business objective

Customer-retention teams need to understand which customer groups leave most often and where an intervention may be useful. This case study compares churn across contract structures and customer attributes while keeping the conclusions descriptive rather than causal.

## Verified dataset facts

The dataset contains **7,043 customers**, 21 analytical columns, zero duplicate customer IDs, and **1,869 churned customers** [1]. The observed overall churn rate is **26.54%**.

| Metric | Verified result |
|---|---:|
| Customers | 7,043 |
| Churned customers | 1,869 |
| Overall churn rate | 26.54% |
| Highest-churn contract | Month-to-month: 42.71% |
| Lowest-churn contract | Two year: 2.83% |
| Duplicate customer IDs | 0 |

## Visual evidence

![Churn rate by contract](images/churn_contract_rate.png)

The chart compares observed churn rates by contract type. It does not establish that contract type causes churn; tenure, pricing, service usage, acquisition channel, and customer experience may also contribute.

## Key business insights

Month-to-month customers have the highest observed churn rate at **42.71%**, while two-year customers have the lowest at **2.83%**. The gap suggests a practical retention question: whether month-to-month customers should receive earlier engagement, service-quality follow-up, or contract-transition offers. Any intervention should be tested against a defined control group rather than assumed to work.

The analysis should also be segmented by tenure, monthly charges, internet service, support services, and payment method. Contract type is a useful first cut, not a complete churn explanation.

## Analytical workflow

The notebook cleans the `TotalCharges` field, converts numeric columns, checks identifiers, explores the target variable, and uses grouped summaries and charts to compare churn behavior. The repository includes a small validation script so a reviewer can confirm the source row count, identifier uniqueness, and target labels before opening the notebook.

## Data-quality checks

The validation script checks for the expected 21 columns, duplicate customer IDs, blank `TotalCharges` values, and invalid values outside the `Yes`/`No` churn labels. It also confirms that the documented customer count and churn count match the CSV used by the notebook.

## Repository structure

```text
├── Customer.csv
├── README.md
├── TCA.ipynb
├── images/
│   └── churn_contract_rate.png
├── scripts/
│   └── validate_data.py
├── requirements.txt
└── Teco Customer Churn Analysys.pdf
```

## How to reproduce

```bash
git clone https://github.com/Corvus06655/customer-churn-analysis.git
cd customer-churn-analysis
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_data.py
```

Then open `TCA.ipynb` in Jupyter and run the cells from top to bottom. The included PDF is a supplementary project artifact; the notebook and CSV are the primary reproducibility inputs.

## Data provenance and limitations

The repository contains the customer-level CSV used for this educational analysis. The dataset is commonly used for telecom churn practice and should be treated as an anonymized analytical extract rather than a live customer system. It does not support causal claims about why customers churn without additional experiment, service-quality, and longitudinal data.

## References

[1]: Customer.csv — customer-level source extract.
[2]: TCA.ipynb — cleaning, exploratory analysis, and churn comparison workflow.
[3]: images/churn_contract_rate.png — contract-level churn visualization.

## Author

**Mayank Srivastava** · [GitHub](https://github.com/Corvus06655) · [LinkedIn](https://linkedin.com/in/mayank-srivastava-076020215)
