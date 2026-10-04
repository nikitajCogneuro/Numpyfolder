
from scipy import stats

exam_score = [72, 61, 81, 68, 75, 55, 88, 70]
passed = [1, 1, 1, 1, 1, 0, 1, 1]

result = stats.pointbiserialr(
    passed,
    exam_score
)

print("Point-biserial correlation:", result.statistic)
print("p-value:", result.pvalue)