import pandas as pd

data=pd.DataFrame({
    'Name':['Kim','lee','Park'],
    'Age':[25,30,22],
    'Gender':['Female','Male','Female']
})

data_sorted=data.sort_values(by='Age')
print(data_sorted)