import matplotlib.pyplot as plt
import pandas as pandas
import seaborn as sns
import numpy as np 

a = 0
b = 10
pts = 100
x = np.linspace(a,b,pts)

y= x**2
plt.plot(x,y)

#comments