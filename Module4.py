# ---------------------------------------------------------
# Kendall's tau
# ---------------------------------------------------------
# Kendall's tau is a rank-based measure that evaluates
# how consistently the ordering of observations agrees
# between two variables.
#
# It compares concordant pairs (the ordering agrees)
# with discordant pairs (the ordering disagrees).
# ---------------------------------------------------------

from scipy import stats

study_hours = [1, 2, 3, 4, 5]
exam_scores = [2, 5, 20, 100, 500]

result = stats.kendalltau(study_hours, exam_scores)

print(result)
