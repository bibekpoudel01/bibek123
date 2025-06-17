import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title('Frequency distribution with a=king, b=rcb')
plt.savefig('matplotlib_histogram.png')  # Corrected from plt.save() to plt.savefig()
plt.show()
