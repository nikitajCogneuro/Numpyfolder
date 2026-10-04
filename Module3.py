# ---------------------------------------------------------
# Spearman correlation
# ---------------------------------------------------------
# Spearman's correlation is a rank-based measure of
# association. It is useful when variables have a
# monotonic relationship but the relationship is not
# necessarily linear.
#
# The values are considered through their ranks rather
# than requiring the actual numerical distances between
# observations to follow a straight-line pattern.
# ---------------------------------------------------------

from scipy import stats

study_hours = [1, 2, 3, 4, 5]
exam_scores = [2, 5, 20, 100, 500]

result = stats.spearmanr(study_hours, exam_scores)

print(result)

