import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data)
plt.show()
