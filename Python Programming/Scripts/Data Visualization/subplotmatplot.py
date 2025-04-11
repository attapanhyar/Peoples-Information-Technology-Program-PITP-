import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [1, 4, 9])
axs[1].plot([1, 2, 3], [9, 4, 1])
plt.show()