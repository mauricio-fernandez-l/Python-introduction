# %% Import

import numpy as np

# %%

a1 = np.array([10, 11, 15])

print(type(a1))
print(a1.dtype)
print(a1.shape)
print(a1.shape[0])

print("Extract elements of array")
for i in range(a1.shape[0]):
    print(f"Element at position {i}")
    print(a1[i])
    
# %%

a2 = np.array([
    [10, 12, 14],
    [20, 22, 24]
    ])

print(a2.shape)

for i1 in range(a2.shape[0]):
    for i2 in range(a2.shape[1]):
        print(f"\nPosition: {i1, i2}")
        print(f"Old element: {a2[i1, i2]}")
        a2[i1, i2] = 100*i1 + i2
        print(f"New element: {a2[i1, i2]}")
        
# %%

n = 100
a3 = np.random.rand(n, 3)
print(a3.shape)
print(a3[:10])