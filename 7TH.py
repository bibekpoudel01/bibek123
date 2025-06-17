import pandas as pd

# Custom immigration dataset
data = {
    'Country': ['India', 'China', 'Philippines', 'Pakistan', 'Nigeria'],
    '2010': [4500, 4800, 3000, 2000, 1000],
    '2011': [4700, 4900, 3200, 2200, 1300],
    '2012': [5000, 5100, 3400, 2400, 1600],
    '2013': [5200, 5300, 3600, 2600, 1900],
    '2014': [5500, 5600, 3800, 2800, 2200]
}

df_immigration = pd.DataFrame(data)

print(df_immigration)
df_immigration.head()
