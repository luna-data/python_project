import pandas as pd

data1=pd.DataFrame({
    'Name':['Kim','Lee','Park'],
    'Age':[25,30,22]

})

data2=pd.DataFrame({
    'Name':['Kim','Lee','David'],
    'Gender':['Female','Male','Male']
})  

merged_data=pd.merge(data1,data2,on='Name',how='inner')
print(merged_data)