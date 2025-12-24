# RWE Diabetes Readmission Analysis

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Data](https://img.shields.io/badge/Data-UCI%20ML-orange.svg)](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/)

**Real-World Evidence analysis identifying risk factors for 30-day hospital readmission in 101,766 diabetic patient encounters.**

---

## 📊 Results at a Glance

| Metric | Value |
|--------|-------|
| **Sample Size** | 101,766 encounters |
| **Outcome Rate** | 11.2% (30-day readmission) |
| **Statistical Method** | Multivariable Logistic Regression |
| **Primary Finding** | Age ≥70 years: OR 1.21 (95% CI: 1.10–1.33) |

### Significant Risk Factors

| Factor | Odds Ratio | 95% CI | P-value |
|--------|-----------|--------|---------|
| Age 70–80 years | **1.21** | 1.10–1.33 | <0.001 |
| Age 80–90 years | **1.18** | 1.05–1.32 | 0.005 |
| Number of medications | 1.01 | 1.00–1.02 | 0.02 |

> 📖 **[View complete analysis with Forest Plot →](notebooks/02_diabetes_rwe.ipynb)**

---

## Study Design

```
┌─────────────────────────────────────────────────────────────────┐
│  POPULATION     Adults with diabetes (130 US hospitals)        │
│  TIMEFRAME      1999–2008                                       │
│  EXPOSURE       Age, gender, medications, procedures, LOS       │
│  OUTCOME        Hospital readmission within 30 days (binary)    │
│  ANALYSIS       Logistic regression, adjusted for confounders   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
rwe-diabetes-readmission/
├── notebooks/
│   └── 02_diabetes_rwe.ipynb   ← Full analysis with outputs
├── src/
│   └── fetch_data.py           ← Reproducible UCI data download
├── docs/
│   └── results.md              ← Detailed results summary
├── requirements.txt
└── README.md
```

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/rwe-diabetes-readmission.git
cd rwe-diabetes-readmission

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run analysis (notebook has pre-computed outputs)
jupyter notebook notebooks/02_diabetes_rwe.ipynb
```

---

## Key Insights

1. **Age is the strongest predictor** — Patients aged 70+ have 18–21% higher odds of early readmission
2. **Medication count matters** — Each additional medication slightly increases readmission risk
3. **More procedures = lower risk** — Possibly indicates more thorough inpatient care
4. **No gender difference** — Male and female patients show similar readmission patterns

---

## Limitations

| Limitation | Implication |
|------------|-------------|
| Observational design | Association ≠ causation |
| Historical data (1999–2008) | Practice patterns may differ today |
| Missing variables | Weight (97%), payer (40%) unavailable |
| Binary outcome | Severity/urgency not captured |

---

## Data Source

**Diabetes 130-US Hospitals for Years 1999–2008**  
UCI Machine Learning Repository (ID: 296)

- 📄 [Dataset Documentation](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)
- 📚 [Original Publication](https://doi.org/10.1155/2014/781670) — Strack et al., BioMed Research International, 2014
- ⚖️ License: CC BY 4.0

---

## Skills Demonstrated

- **RWE/Epidemiology**: Cohort definition, outcome measurement, confounder adjustment
- **Statistical Analysis**: Logistic regression, odds ratio interpretation, confidence intervals
- **Data Engineering**: Reproducible ETL from UCI repository
- **Communication**: Clear visualization of clinical findings

---

> *This project demonstrates competencies in pharmacovigilance, clinical research, and health data science.*
