import pandas as pd

data=pd.DataFrame({
    'Name':['Kim','Lee','Park'],    
    'Age':[25,30,22],
    'Gender':['Female','Male','Female'] 
})

grouped_data=data.groupby('Gender')['Age'].mean()
print(grouped_data)