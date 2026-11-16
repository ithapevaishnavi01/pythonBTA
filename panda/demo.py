import pandas as pd
import pandas as np

df = pd.DataFrame({
    'Name': ['Vaishnavi', 'Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19, 22],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Nashik']
})

# df = df.rename(columns={'A': 'its_A'})


# print(df)

# df.to_csv('output.csv', index=False) ---->>export dataframe to csv file

#load_df = pd.read_csv('output.csv')   #---->>import dataframe from csv file
# print(load_df)


# print(load_df.where(load_df['A'] > 1))

# df['clg'] = ['MIT', 'IIT', 'NIT', 'VIT']
# print(df)
# df.loc[len(df)] = ['Rohit', 23, 'Bangalore', 'IIT']
# print(df)

# df.loc[0,'City'] = 'yesPune'
# print(df)

# df.drop(df[df.Name == 'Rohit'].index)
# print(df)


# df.drop('clg', axis=1, inplace=True)
# print(df)


# df.sort_values(by='Age', ascending=True, inplace=True)
# print(df)

# df["DOJ"]= ['2020-01-01', '2019-05-15', '2021-07-20', '2018-03-10 ']

# df['DOJ'] = df['DOJ'].str.strip()

# df['DOJ'] = pd.to_datetime(df['DOJ'])

# print(df)

# print(df.dtypes) 

df1=df
# print(df1)


# df1 = df1['DOJ'].dt.day
# print(df1) 

# df1.loc[df1.Name == 'Rahul', 'City'] = pd.NA
# print(df1)
# print(df1.isnull())
 
# print(df1.isnull().sum())  #---->>count of null values in each column

# print(df1.fillna('Not Available'))  #---->>replace null values with 'Not Available'

# print(df1['Age'].value_counts())



# print(df[df1['Age']==19].value_counts())


# print(df.groupby('Name')['Age'].mean())

# print(df.groupby('Name').agg({'Age': ['mean', 'sum'], 'City': 'count'}))



df1 = pd.DataFrame({
    'id': [1,2,3],
    'name': ['Vaish','Adi','Rit']
})


df2 = pd.DataFrame({
    'id': [1,2,2,4],
    'score':[22,546,87,24]
})

# print(df1)
# print(df2)

print(pd.concat([df1, df2], axis=0))  #---->>concatenate two dataframes vertically (one below the other) based on index 
print(pd.concat([df1, df2], axis=1))  #---->>concatenate two dataframes horizontally (side by side) based on index  


print(pd.merge(df1, df2, on='id', how='inner') ) #---->>merge two dataframes based on common column 'id' with inner join   