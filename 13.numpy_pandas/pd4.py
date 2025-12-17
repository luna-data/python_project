import pandas as pd
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})  
filtered_data = data[data['Age'] > =25]
print(filtered_data)