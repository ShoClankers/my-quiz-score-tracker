import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
scores = [70, 85, 60, 90, 75]

plt.plot(days, scores)
plt.show()


plt.plot(days, scores)
plt.title("MY quiz score tracker")
plt.xlabel("Days")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.plot(days, scores, marker='o', linestyle='dashed', color='cyan', linewidth=2)
plt.title("MY quiz score tracker")
plt.xlabel("Days")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.bar(days, scores, color='crimson')
plt.title("MY quiz score tracker")
plt.xlabel("Days")
plt.ylabel("Scores")
plt.ylim(0, 100)
plt.show()