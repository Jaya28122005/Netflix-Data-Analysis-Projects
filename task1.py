import pandas as pd
#load the data set
df = pd.read_csv(
    r"C:\Users\DELL\Documents\Auspify_Task1\Task1_Netflix_Cleaning\Dataset.csv"
)

print(df.head())
print(df.shape)
print(df.columns)

# check missing values
print(df.isnull().sum())

#To check the duplicate records
print(df.duplicated().sum())
df['type'] = df['type'].str.strip().str.title()
df['type'] = df['type'].replace({
    'Tv Show': 'TV Show'
})
print(df["type"].unique())
df['rating'] = df['rating'].replace({
    'UR': 'Not Rated',
    'NR': 'Not Rated'
})
print(df["rating"].unique())
print(df["country"].unique())
print((df["country"] == "Not Given").sum())
df["country"] = df["country"].replace("Not Given", pd.NA)
print(df["country"].isnull().sum())
df['country'] = df['country'].fillna('Not Given')
print(df['country'].isnull().sum())
#cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("Cleaned dataset exported successfully!")

import os

print(os.path.abspath("netflix_cleaned.csv"))