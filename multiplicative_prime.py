import matplotlib.pyplot as plt

n_values = [chr(i) + chr(j) for i in range(65, 91) for j in range(65, 91)]

# 2 ** 64 / 1.618 ≈ 11400714819323198549 (prime)
multiplier = 31
y_values = [sum(ord(char) * (multiplier ** i) for i, char in enumerate(n, 1)) % 4861 for n in n_values]
plt.scatter(n_values, y_values, label=multiplier)

plt.xlabel("n")
plt.ylabel("f(n)")
plt.legend()
plt.xticks(n_values[::100], n_values[::100])
# plt.show()