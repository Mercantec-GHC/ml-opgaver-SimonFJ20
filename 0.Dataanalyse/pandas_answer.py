import numpy as np
import pandas as pd

cols = np.array(["Eleanor", "Chidi", "Tahani", "Jason"])
data = np.random.randint(size=(3, 4), low=0, high=100)

frame = pd.DataFrame(data=data, columns=cols)
print(frame)
