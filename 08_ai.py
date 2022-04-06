# %% Import

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# %% Data: 1D input and 2D output

n = 100
xs = (np.random.rand(n) - 0.5) * 10 + 4
fs = np.sin(xs) * 3 + xs

plt.figure()
plt.scatter(xs, fs)
plt.show()

# %% Normalize data

mean = np.mean(xs)
std = np.std(xs)

print(mean)
print(std)

xs_transformed = (xs - mean) / std

print(np.mean(xs_transformed))
print(np.std(xs_transformed))

# %% Artificial neural network (ANN) model

model = tf.keras.Sequential(
    [
        tf.keras.layers.Input(shape=[1]),
        tf.keras.layers.Dense(8, "relu"),
        tf.keras.layers.Dense(8, "relu"),
        tf.keras.layers.Dense(1),
    ]
)
model.compile("adam", "mse")

model.summary()

# %% Evaluate model

model.evaluate(xs_transformed, fs)

# %% Fit model to data

model.fit(xs_transformed, fs, epochs=1000)

# %% Predict and plot

fs_m = model(xs_transformed)

plt.figure()
plt.scatter(xs, fs, label="data")
plt.scatter(xs, fs_m, label="ANN prediction")
plt.legend()
plt.show()

# %% 2D input - 1D output

xs = np.array(
    [[x1, x2] for x1 in np.linspace(-1.5, 1.5, 20) for x2 in np.linspace(-2, 2, 20)]
)
fs = np.array([np.sin(x[0] + x[1]) + 3 for x in xs])

plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(xs[:, 0], xs[:, 1], fs, label="data")
plt.legend()
plt.show()

model = tf.keras.Sequential(
    [
        tf.keras.layers.Input(shape=[2]),
        tf.keras.layers.Dense(8, "relu"),
        tf.keras.layers.Dense(8, "relu"),
        tf.keras.layers.Dense(1),
    ]
)
model.compile("adam", "mse")

model.fit(xs, fs, epochs=100, verbose=0)

plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(xs[:, 0], xs[:, 1], fs, label="data")
ax.scatter(xs[:, 0], xs[:, 1], model(xs), label="model")
plt.legend()
plt.show()
