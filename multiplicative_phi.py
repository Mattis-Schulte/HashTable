import matplotlib.pyplot as plt

n_values = [chr(i) + chr(j) for i in range(65, 91) for j in range(65, 91)]
c_values = [0.618]

for c in c_values:
    y_values = [int(587 * (sum(ord(char) * (c ** i) for i, char in enumerate(n, 1)) % 1)) for n in n_values]
    plt.scatter(n_values, y_values, label="c = " + str(c))

plt.xlabel("n")
plt.ylabel("f(n)")
plt.legend()
plt.xticks(n_values[::100], n_values[::100])
plt.show()