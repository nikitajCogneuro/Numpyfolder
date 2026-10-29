This script models the probability of passing an exam
using sleep hours as a predictor.

Outcome:
    passed = 1 if the student passes
    passed = 0 if the student fails

Logistic regression is used because the outcome is binary.



import pandas as pd
import statsmodels.api as sm
import math

# Create illustrative data with overlapping outcomes.
students = pd.DataFrame({
    "sleep_hours": [
        4, 5, 5, 6, 6, 6, 7, 7,
        7, 8, 8, 8, 9, 9, 5, 7
    ],
    "passed": [
        0, 0, 1, 0, 1, 1, 0, 1,
        1, 0, 1, 1, 1, 0, 1, 0
    ]
})

# Predictor: sleep hours.
X = students[["sleep_hours"]]

# Binary outcome: 0 = failed, 1 = passed.
y = students["passed"]

# Include the intercept.
X = sm.add_constant(X)

# Fit the logistic regression model.
model = sm.Logit(y, X).fit()

# Display model results.
print(model.summary())

# Convert the sleep-hours coefficient into an odds ratio.
odds_ratio = math.exp(model.params["sleep_hours"])
print("Odds ratio for sleep hours:", odds_ratio)

# Calculate predicted probabilities.
students["predicted_probability"] = model.predict(X)

print(students)
