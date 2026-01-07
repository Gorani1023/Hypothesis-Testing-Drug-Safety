# ==============================
# Import required libraries
# ==============================

import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind, mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest

# ==============================
# 1. Test difference in adverse event rates
#    (Drug vs Placebo)
# ==============================

# Create a contingency table:
# Treatment group (Drug / Placebo) x Adverse effects (Yes / No)
adverse_table = pd.crosstab(
    drug_safety["trx"],
    drug_safety["adverse_effects"]
)

# Number of patients with adverse effects in each group
count = adverse_table.iloc[:, 1].values

# Total number of patients in each group
nobs = adverse_table.sum(axis=1).values

# Two-sample proportion z-test
_, two_sample_p_value = proportions_ztest(
    count,
    nobs
)

# ==============================
# 2. Test independence between treatment group
#    and number of adverse effects
# ==============================

# Create a contingency table:
# Treatment group x Number of adverse effects
num_effects_table = pd.crosstab(
    drug_safety["trx"],
    drug_safety["num_effects"]
)

# Chi-square test of independence
_, num_effects_p_value, _, _ = chi2_contingency(num_effects_table)

# ==============================
# 3. Test age difference between Drug and Placebo groups
# ==============================

# Extract ages for each treatment group
drug_ages = drug_safety.loc[
    drug_safety["trx"] == "Drug", "age"
]
placebo_ages = drug_safety.loc[
    drug_safety["trx"] == "Placebo", "age"
]

# Welch's t-test (does not assume equal variance)
_, age_group_effects_p_value_ttest = ttest_ind(
    drug_ages,
    placebo_ages,
    equal_var=False
)

# Non-parametric alternative: Mann–Whitney U test
_, age_group_effects_p_value_mwu = mannwhitneyu(
    drug_ages,
    placebo_ages,
    alternative="two-sided"
)

# ==============================
# Print results
# ==============================

print("Two-sample proportion test p-value:", two_sample_p_value)
print("Chi-square test p-value:", num_effects_p_value)
print("Age difference (t-test) p-value:", age_group_effects_p_value_ttest)
print("Age difference (Mann–Whitney U) p-value:", age_group_effects_p_value_mwu)

## 📊 Results

### 1. Difference in Adverse Event Rates
A two-sample proportion z-test was conducted to compare the proportion of patients
experiencing adverse effects between the Drug and Placebo groups.

The test results indicate whether the adverse event rate differs significantly
between the two treatment groups based on the calculated p-value.

---

### 2. Independence Between Treatment Group and Number of Adverse Effects
A chi-square test of independence was performed to examine the relationship between
treatment assignment and the number of adverse effects experienced by patients.

The results suggest whether the distribution of adverse effects is independent
of the treatment group.

---

### 3. Age Comparison Between Treatment Groups
To compare the age distributions of the Drug and Placebo groups, both a
Welch’s t-test and a Mann–Whitney U test were applied.

Using both parametric and non-parametric methods provides a more robust assessment
of potential age differences between groups.

## 🧾 Summary

This project applies statistical hypothesis testing to drug safety data,
including proportion tests, chi-square tests, and group comparison methods,
to evaluate differences between a drug treatment and a placebo group.

