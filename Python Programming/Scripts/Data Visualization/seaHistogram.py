import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
sns.histplot(data['total_bill'], kde=True)
plt.show()
