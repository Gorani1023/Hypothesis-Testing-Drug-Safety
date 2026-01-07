# Drug Safety Statistical Analysis

This project performs a **statistical analysis of drug safety data** to compare
a treatment group (Drug) with a control group (Placebo).

Multiple hypothesis tests are applied to evaluate:
- Differences in adverse event rates
- Independence between treatment and number of adverse effects
- Age differences between treatment groups

This analysis is suitable as an **introductory biostatistics / clinical trial analysis project**.

---

## 📌 Project Overview

The goal of this project is to statistically assess whether a drug differs from a placebo
in terms of safety-related outcomes.

Specifically, the project addresses the following questions:
1. Is the proportion of patients experiencing adverse effects different between groups?
2. Is the number of adverse effects independent of treatment assignment?
3. Are there age differences between the Drug and Placebo groups?

---

## 🧪 Statistical Methods Used

| Research Question | Method |
|------------------|--------|
| Difference in adverse event rates | Two-sample proportion z-test |
| Independence between group and number of effects | Chi-square test of independence |
| Age difference (parametric) | Welch’s t-test |
| Age difference (non-parametric) | Mann–Whitney U test |

---

## 🛠 Technologies & Libraries

- Python
- pandas
- scipy
- statsmodels
- Jupyter Notebook / Python script

---

## 📂 Project Structure


---

## ▶ How to Run

### Option 1: Run as a Python Script
```bash
python drug_safety_statistical_analysis.py

Option 2: Run in Jupyter Notebook

1. Launch Jupyter Notebook

2. Open drug_safety_statistical_analysis.ipynb

3. Run all cells from top to bottom

📊 Description of the Analysis
1. Adverse Event Rate Comparison

A two-sample proportion z-test is used to compare the proportion of patients
who experienced adverse effects between the Drug and Placebo groups.

This test is appropriate because:

The outcome is binary (adverse effects: yes/no)

Two independent groups are compared

2. Independence Between Treatment and Number of Adverse Effects

A chi-square test of independence evaluates whether the number of adverse effects
is related to treatment assignment.

This helps determine whether adverse effects are distributed differently
across treatment groups.

3. Age Comparison Between Groups

Two methods are applied:

Welch’s t-test (does not assume equal variances)

Mann–Whitney U test as a non-parametric alternative

Using both tests improves robustness when normality assumptions may not hold.

📈 Output

The script prints p-values for each statistical test:

Proportion z-test p-value

Chi-square test p-value

Age comparison p-values (t-test and Mann–Whitney U)

These values are used to assess statistical significance.

💡 What I Learned

How to choose appropriate statistical tests based on data type

Applying hypothesis testing to real-world clinical trial–like data

Interpreting p-values in the context of drug safety analysis

Structuring a statistical analysis project for GitHub

🚀 Future Improvements

Add effect size calculations (Cohen’s d, Cramér’s V)

Visualize results using boxplots and bar charts

Adjust for multiple testing

Extend analysis using logistic regression

👤 Author

Created by [Lee HyunJun]