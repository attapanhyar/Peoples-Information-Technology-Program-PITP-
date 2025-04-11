import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.annotate("Peak", xy=(2, 5), xytext=(2, 5.5), 
             arrowprops=dict(arrowstyle="->"))
plt.show()
