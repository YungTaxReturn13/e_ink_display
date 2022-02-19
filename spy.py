from tkinter import Y
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


d = {"x": range(100), "y": np.random.rand(100)}
df = pd.DataFrame(data=d)
print(df)

sns.lineplot(data=df, x="x", y="y")
plt.savefig("graph.png")
