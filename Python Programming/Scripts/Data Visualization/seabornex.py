import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
#print(data.head(2))
sns.regplot(x="total_bill", y="tip", data=data)
plt.show()

