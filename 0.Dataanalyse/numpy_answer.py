import numpy as np

feature = np.arange(6, 20 + 1)
print(feature)

label = 3 * feature + 4;
print(label)

noise = np.random.random([len(feature)]) * 4 - 2
print(noise)

label = label.astype(float) + noise
print(label)


