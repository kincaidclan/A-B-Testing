# A/B Testing Analysis: Ad vs. PSA Campaign

This project analyzes a real-world A/B test conducted by a marketing team to compare the effectiveness of an **ad campaign** versus a **public service announcement (PSA)**. The key goal was to determine whether exposure to ads results in a higher conversion rate compared to the PSA.

## Dataset

The dataset comes from a Kaggle marketing A/B testing competition and contains:
- `test group`: Whether the user was shown the ad (`ad`) or PSA (`psa`)
- `converted`: Whether the user converted (1) or not (0)
- `most ads day`: Day of the week when the user saw the most ads
- `most ads hour`: Hour of the day when the user saw the most ads

## Methodology

We ran a **one-tailed z-test for proportions** to evaluate whether the ad group had a statistically higher conversion rate than the PSA group.

### Key Results
- **Ad group conversion rate:** 2.55%
- **PSA group conversion rate:** 1.79%
- **Z-statistic:** 7.37
- **P-value:** 1.7e-13

> Result: The difference is statistically significant. The ad group led to a higher conversion rate than the PSA group.

## Files Included
- `ab_test_cleaned.csv`: Cleaned version of the dataset
- `ab_test_ztest.py`: Python script that runs the A/B test and outputs results

## How to Run

Make sure you have `pandas` and `scipy` installed. Then run:

```bash
python ab_test_ztest.py
```

## Conclusion

This project demonstrates how to run and interpret an A/B test using a z-test for proportions. It’s a strong example of how experimentation and data science can guide product and marketing decisions.
