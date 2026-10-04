import pandas as pd
from scipy import stats

students = pd.DataFrame({
    "student": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep_hours": [7, 5, 8, 6, 7, 4, 9, 6],
    "exam_score": [72, 61, 81, 68, 75, 55, 88, 70]
})

result = stats.pearsonr(
    students["sleep_hours"],
    students["exam_score"]
)

print(result)