import matplotlib.pyplot as plt
import pandas as pd

# Custom dataset
data = {
    'Country': ['India', 'China', 'Philippines', 'Pakistan', 'Nigeria'],
    '2010': [45, 4800, 3000, 2000, 10],
    '2011': [4700, 49, 3200, 2200, 130],
    '2012': [50000,51000,340, 2400, 1600],
    '2013': [5200, 5300, 3600, 260, 1900],
    '2014': [500, 5600, 3800, 2800, 200]
}

df_immigration = pd.DataFrame(data)
df_immigration.set_index('Country', inplace=True)

years = ['2010', '2011', '2012', '2013', '2014']

# Plot only India
df_immigration.loc[['India'], years].T.plot(kind='area', legend=False)

plt.title('Immigration from India')
plt.xlabel('Years')
plt.ylabel('Number of Immigrants')
plt.show()
