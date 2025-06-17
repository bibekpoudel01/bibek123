import pandas as pd

# Step 1: Download and read the Excel file into a DataFrame
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
)

print('Data downloaded and read into a dataframe!')

# Step 2: Clean the DataFrame
# Rename columns for easier access
df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

# Set 'Country' as the index
df_can.set_index('Country', inplace=True)

# Remove unnecessary columns
df_can.drop(['Type', 'Coverage', 'AREA', 'REG', 'DEV'], axis=1, inplace=True)

# Confirm the DataFrame is ready
print("\nDataFrame cleaned and ready!")
print(df_can.head())
