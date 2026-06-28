import pandas as pd

# Create a list of dataframes
dfs = []
for year in range(2015, 2020):
    df_year = pd.read_csv(f'input_data/{year}.csv')
    dfs.append(df_year)

# Change the header names for 2017 dataframe to match the other years
dfs[2].columns = dfs[2].columns.str.replace('.', ' ')
dfs[2].columns = dfs[2].columns.str.replace('  ', ' ')


# Compare header names across all years
reference = set(dfs[0].columns)

for i, df in enumerate(dfs[1:], start=1):
    diff = set(df.columns) - reference
    missing = reference - set(df.columns)
    print(f"\n{2015 + i}:")
    print(f"  Extra columns:   {diff}")
    print(f"  Missing columns: {missing}")
'''
# Check shape and structure
print("Shape")
for year in range(2015, 2019):
    print(f"Year {year}: {df_year.shape}")
    
print("First 10 rows")
for year in range(2015, 2019):
    print(f"Year {year}: {df_year.head(10)}")
    
print("Data Types")
for year in range(2015, 2019):
    print(f"Year {year}: {df_year.dtypes}")

# Check for missing values

if df.isnull().values.any():
    print("There are missing values in the dataset.")
else:
    print("There are no missing values in the dataset.")

# Check for duplicates
if df.duplicated().any():
    print("There are duplicate rows in the dataset.")
else:
    print("There are no duplicate rows in the dataset.")

# Check stats
print(df.describe())

# Union all years data

df_all_years = pd.concat([pd.read_csv(f'{year}.csv') for year in range(2015, 2019)], ignore_index=True)
print(df_all_years.shape)

df_all_years.to_csv('world_happiness_report_all_years.csv', index=False)
'''
