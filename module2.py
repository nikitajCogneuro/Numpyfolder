# ---------------------------------------------------------
# Pearson correlation
# ---------------------------------------------------------
# Pearson's correlation measures the strength and direction
# of a LINEAR relationship between two numerical variables.
#
# Here we examine whether sleep hours are associated with
# exam scores.
#
# The function returns:
#   - statistic: Pearson's r
#   - pvalue: test of the null hypothesis that the
#             population correlation is zero.
# --------------------------------------------------------

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
