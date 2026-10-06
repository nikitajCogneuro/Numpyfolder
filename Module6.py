
import pandas as pd
import statsmodels.api as sm

students= pd.DataFrame({
"sleep_hours": [7, 5, 8, 6, 7, 4, 9, 6],
"exam_score": [72, 61, 81, 68, 75, 55, 88, 70]})

X = students["sleep_hours"]
y = students["exam_score"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())


