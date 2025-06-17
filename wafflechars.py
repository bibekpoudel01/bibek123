from pywaffle import Waffle
import matplotlib.pyplot as plt

# Data to plot
data = {'Apples': 32, 'Bananas': 45, 'Oranges': 23}

# Create Waffle chart figure
fig = plt.figure(
    FigureClass=Waffle,
    rows=10,  # Number of rows (10x10 grid = 100 squares)
    values=data,
    title={'label': 'Fruit Distribution', 'loc': 'center'}
)

plt.show()
