# ---------------------------------------------------------
# Point-biserial correlation
# ---------------------------------------------------------
# Point-biserial correlation is appropriate when one
# variable is continuous and the other variable has
# exactly two categories.
#
# Here:
#   0 = failed
#   1 = passed
#
# The 0/1 values are category labels, not quantities.
# We are examining whether exam scores are associated
# with membership in the two groups.
# ---------------------------------------------------------

from scipy import stats

exam_score = [72, 61, 81, 68, 75, 55, 88, 70]
passed = [1, 1, 1, 1, 1, 0, 1, 1]

result = stats.pointbiserialr(
    passed,
    exam_score
)

print("Point-biserial correlation:", result.statistic)
print("p-value:", result.pvalue)
