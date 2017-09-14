import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.random.randint(1,100,1000)
p1 = plt.plot(x)
plt.show(p1)

df = pd.DataFrame(x, columns = ["Eine Übersicht"])
print(df.head())
pd
