import pandas

pd = pandas.read_json('responsezr.json')
# print(pd)
pd.to_csv('responsezr.csv')