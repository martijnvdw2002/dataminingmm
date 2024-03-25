# %%
import pandas as pd

# %%
marathon15 = pd.read_csv('marathon_results_2015.csv')
marathon16 = pd.read_csv('marathon_results_2016.csv')
marathon17 = pd.read_csv('marathon_results_2017.csv')

# %%
marathon15['Year'] = 2015
marathon16['Year'] = 2016
marathon17['Year'] = 2017

# Combine the dataframes
df_combined = pd.concat([marathon15, marathon16, marathon17], ignore_index=True)

# Now df_combined is your combined dataframe with the 'Year' column
df_combined.head()

# %%
# Columns to be dropped
columns_to_drop = ['Unnamed: 0', 'State', 'Citizen', 'Unnamed: 9', 'Proj Time', '...', 'Bib', 'Unnamed: 8']

# Drop the specified columns from the dataframe
df = df_combined.drop(columns=columns_to_drop, errors='ignore')  # errors='ignore' to avoid error if a column is not present

# Display the first 5 rows to confirm the columns are dropped
df

# %%



