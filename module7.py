

import pandas as pd
import statsmodels.api as sm

# Create a small illustrative dataset.
students = pd.DataFrame({
    "sleep_hours": [7, 5, 8, 6, 7, 4, 9, 6],
    "passed":      [1, 1, 1, 1, 1, 0, 1, 1]
})

# Define the predictor and binary outcome.
X = students[["sleep_hours"]]
y = students["passed"]

# Add an intercept to the model.
X = sm.add_constant(X)

# Fit a logistic regression model.
model = sm.Logit(y, X).fit()

# Display the estimated coefficients and statistical tests.
print(model.summary())

# Convert the sleep-hours coefficient into an odds ratio.
odds_ratio = model.params["sleep_hours"].__float__()

import math
odds_ratio = math.exp(odds_ratio)

print("Odds ratio for sleep hours:", odds_ratio)

# Estimate each student's probability of passing.
students["predicted_probability"] = model.predict(X)

print(students)
