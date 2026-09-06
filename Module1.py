import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "exam_score": [72, 61, 81, 68, 75, 55, 88, 70]
})

plt.hist(data["exam_score"], bins=5)
plt.xlabel("Exam score")
plt.ylabel("Frequency")
plt.show()


