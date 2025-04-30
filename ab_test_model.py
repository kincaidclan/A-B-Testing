import pandas as pd
from scipy.stats import norm

# Load dataset
df = pd.read_csv("marketing_AB.csv")

# Clean and prepare columns
df['converted'] = df['converted'].astype(int)
df['group_binary'] = df['test group'].map({'ad': 1, 'psa': 0})

# Split data into groups
ad_group = df[df['group_binary'] == 1]
psa_group = df[df['group_binary'] == 0]

# Count conversions and totals
conversions_ad = ad_group['converted'].sum()
conversions_psa = psa_group['converted'].sum()
n_ad = len(ad_group)
n_psa = len(psa_group)

# Conversion rates
p1 = conversions_ad / n_ad
p2 = conversions_psa / n_psa
p_pool = (conversions_ad + conversions_psa) / (n_ad + n_psa)

# Z-test statistic (one-tailed)
z = (p1 - p2) / ((p_pool * (1 - p_pool) * (1 / n_ad + 1 / n_psa)) ** 0.5)
p_value = 1 - norm.cdf(z)

# Print results
print(f"Conversion Rate (Ad): {p1:.4f}")
print(f"Conversion Rate (PSA): {p2:.4f}")
print(f"Z-Statistic: {z:.4f}")
print(f"P-Value: {p_value:.10f}")

# Interpretation
if p_value < 0.05:
    print("Result: Statistically significant — ad group converted better.")
else:
    print("Result: Not statistically significant — no clear difference.")
