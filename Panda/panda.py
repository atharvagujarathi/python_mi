import pandas as pd

print("Empty data frame")
df = pd.DataFrame()
print(df)


print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

print("Dataframe with list")
data = [['ppa', 4], ['lb', 3], ['python', 3], ['angular', 3]]
df = pd.DataFrame(data, columns=['Name', 'Duration'])
print(df)

data = {'Name':['ppa', 'lb', 'python', 'angular'], 'Duration':[4,3,3,3]}
df = pd.DataFrame(data)
print(df)

data = [{'Name':'ppa', 'Duration':3, 'Fees':10500}, {'Name':'angular', 'Duration':3, 'Fees': 10500}, {'Name': 'python', 'Fees': 10500}]
df = pd.DataFrame(data)
print(df)

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['x', 'y', 'z', 'w'])}
df = pd.DataFrame(d)
print(df['one'])

d = {'one': pd.Series([{'name': ['Atharva', 'Amit', 'Mohit', 'Manish']}, {'DoY': [2000, 2001, 2002, 2000]}], index=['a', 'b'])}
df = pd.DataFrame(d)
print(df)