import pandas as pd

## Read in the CSV file
df = pd.read_csv('pokemon_data.csv')


## Read Headers (Prints out all the columns)
print(df.columns)

## Read each column (Prints out a spefic culumn ['Name'])
print(df['Name'])

## Read each column (Prints out a spefic culumn and rows['Name'][0:5])
print(df['Name'][0:5])

## Read each column (Prints out more than one spefic culumn ([['Name', 'Type 1', 'HP']])
print(df[['Name', 'Type 1', 'HP']])

## Read each row (Iterate through each row)
#print(df.iloc[2,1])
# for index, row in df.itterrows():
#     print(index, row)

# Read a specific location (R,C)
print(df.iloc[2,1])

# Reads you a row with a specific column
print(df.loc[df['Type 1'] == "Fire"])