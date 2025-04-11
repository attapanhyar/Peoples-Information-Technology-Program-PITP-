import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
numeric_data = data.select_dtypes(include='number')
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of the 'tips' Dataset")
plt.show()
