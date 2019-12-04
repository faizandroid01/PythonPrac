import pandas as p

#  iloc behavioural attributes

data = (p.Series([1, 2, 3]), p.Series([4, 5, 6]))
index = ['A', 'B']
df = p.DataFrame(data)

df.set_index(index)



print(df)

# Single selections using iloc and DataFrame
# # Rows:
# data.iloc[0]  # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
# data.iloc[1]  # second row of data frame (Evan Zigomalas)
# data.iloc[-1]  # last row of data frame (Mi Richan)
# # Columns:
# data.iloc[:, 0]  # first column of data frame (first_name)
# data.iloc[:, 1]  # second column of data frame (last_name)
# data.iloc[:, -1]  # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
# data.iloc[0:5]  # first five rows of dataframe
# data.iloc[:, 0:2]  # first two columns of data frame with all rows
# data.iloc[[0, 3, 6, 24], [0, 5, 6]]  # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
# data.iloc[0:5, 5:8]  # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# Note that .iloc returns a Pandas Series when one row is selected,
# and a Pandas DataFrame when multiple rows are selected, or if any column in full is selected.
# To counter this, pass a single-valued list if you require DataFrame output.
# explained below

# print(type)
