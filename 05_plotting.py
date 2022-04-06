# %% Import

import matplotlib.pyplot as plt

# %%

xs = list(range(10))
f1s = [x + 7 for x in xs]
f2s = [x ** 2 + 7 for x in xs]

print(xs)
print(f1s)
print(f2s)

# %%

plt.figure()
plt.plot(xs, f1s, label="f1")
plt.plot(xs, f2s, label="f2")
plt.legend()
plt.xlabel("x")
plt.ylabel("f")
plt.title("Some good title")
plt.savefig("figures/file_name.pdf")
plt.savefig("figures/file_name.png")
plt.show()
