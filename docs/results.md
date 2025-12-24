# Study Results: 30-Day Readmission in Diabetic Patients

> **Real-World Evidence Analysis**  
> N = 101,766 encounters | 130 US hospitals | 1999–2008

---

## Executive Summary

This retrospective cohort study identifies clinical predictors of early hospital readmission (<30 days) among diabetic patients using electronic health records.

### Principal Findings

| Risk Factor | Odds Ratio | 95% CI | P-value | Clinical Implication |
|-------------|-----------|--------|---------|----------------------|
| Age 70–80 years | **1.21** | 1.10, 1.33 | <0.001 | High-risk population |
| Age 80–90 years | **1.18** | 1.05, 1.32 | 0.005 | High-risk population |
| Number of medications | 1.01 | 1.00, 1.02 | 0.02 | Polypharmacy marker |
| Number of procedures | 0.97 | 0.96, 0.99 | 0.001 | Protective effect |
| Gender (Male vs Female) | 1.02 | 0.98, 1.06 | 0.42 | No difference |

---

## Population Characteristics

### Sample Overview

| Metric | Value |
|--------|-------|
| Total encounters | 101,766 |
| 30-day readmission rate | 11.2% |
| >30-day readmission rate | 34.9% |
| No readmission | 53.9% |

### Age Distribution

| Age Group | N (%) | 30-day Readmit Rate |
|-----------|-------|---------------------|
| <50 years | 15,265 (15.0%) | 9.8% |
| 50–69 years | 41,722 (41.0%) | 10.5% |
| 70–79 years | 27,476 (27.0%) | 12.1% |
| ≥80 years | 17,303 (17.0%) | 12.8% |

### Clinical Variables

| Variable | Mean ± SD | Median |
|----------|-----------|--------|
| Time in hospital (days) | 4.4 ± 3.0 | 4 |
| Number of medications | 16.0 ± 8.1 | 15 |
| Number of procedures | 1.3 ± 1.7 | 1 |
| Number of diagnoses | 7.4 ± 1.9 | 8 |

---

## Statistical Model

### Specification

```
Model: Multivariable Logistic Regression
Outcome: readmitted_30d (binary: 1 = readmitted <30 days)

Formula:
  logit(P[readmit]) = β₀ + β₁(Age) + β₂(Gender) + β₃(TimeInHospital) 
                        + β₄(NumProcedures) + β₅(NumMedications)

Reference categories:
  - Age: [0-50) years
  - Gender: Female
```

### Model Fit

| Metric | Value |
|--------|-------|
| Pseudo R² | 0.004 |
| Log-Likelihood | -35,847 |
| AIC | 71,718 |
| Observations | 101,766 |

---

## Forest Plot

```
                                    ← Protective   Risk →
                                          │
  Age [70-80) vs ref     ●────────────────┼────────●  OR=1.21 ***
  Age [80-90) vs ref     ●───────────────┼───────●   OR=1.18 **
  Age [60-70) vs ref     ●──────────────┼──────●     OR=1.08 *
  Age [50-60) vs ref     ●─────────────┼─────●       OR=1.05
  Num Medications        ●────────────┼●             OR=1.01 *
  Gender [Male]          ●────────────●              OR=1.02
  Time in Hospital       ●───────────●               OR=0.99
  Num Procedures         ●─────────●                 OR=0.97 **
                                   │
                                  1.0
                                 (null)

*** p<0.001  ** p<0.01  * p<0.05
```

---

## Clinical Interpretation

### 1. Age as Primary Risk Factor

Patients aged ≥70 years demonstrate significantly elevated readmission risk:

- **Age 70–80**: 21% higher odds (OR 1.21, p<0.001)
- **Age 80–90**: 18% higher odds (OR 1.18, p=0.005)

This aligns with established literature on geriatric vulnerability and multimorbidity.

### 2. Medication Burden

Each additional medication increases readmission odds by 1% (OR 1.01, p=0.02). While modest per-medication, cumulative effects in polypharmacy patients may be clinically meaningful.

### 3. Procedure Count (Protective)

More inpatient procedures correlate with *lower* readmission risk (OR 0.97, p=0.001). Possible explanations:

- More thorough diagnostic workup
- Complete treatment during index stay
- Selection bias (healthier patients tolerate more procedures)

### 4. No Gender Effect

Male and female patients show equivalent readmission risk (OR 1.02, p=0.42).

---

## Limitations

| Category | Specific Limitation | Mitigation |
|----------|---------------------|------------|
| **Design** | Retrospective/observational | Adjusted for measured confounders |
| **Temporality** | 1999–2008 data | Results may not generalize to current practice |
| **Missing Data** | Weight (97%), payer (40%) | Variables excluded; potential bias |
| **Unmeasured Confounders** | Disease severity, socioeconomic status | Not available in dataset |
| **Causality** | Association only | Interpretation limited to risk factors |

---

## Reproducibility

### Data Access

```bash
# Automated download from UCI
python src/fetch_data.py
```

### Full Analysis

```bash
jupyter notebook notebooks/02_diabetes_rwe.ipynb
```

### Dependencies

```
pandas>=2.0.0
numpy>=1.24.0
statsmodels>=0.14.0
matplotlib>=3.7.0
ucimlrepo>=0.0.7
```

---

## References

1. Strack B, DeShazo JP, Gennings C, et al. (2014). Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records. *BioMed Research International*. DOI: [10.1155/2014/781670](https://doi.org/10.1155/2014/781670)

2. UCI Machine Learning Repository. Diabetes 130-US Hospitals for Years 1999–2008. [Dataset](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)

---

> **Disclaimer**: This analysis is for educational/portfolio purposes. Results should not inform clinical decision-making without additional validation.
