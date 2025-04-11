import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
sns.pairplot(data)
plt.show()
