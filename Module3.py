from scipy import stats

study_hours = [1, 2, 3, 4, 5]
exam_scores = [2, 5, 20, 100, 500]

result = stats.spearmanr(study_hours, exam_scores)

print(result)

