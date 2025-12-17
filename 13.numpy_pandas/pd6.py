import pandas as pd
data = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park'],
    'Age': [25, 30, 22],
    'Gender': ['Female', 'Male', 'Female']
})

data['Age_Squarred'] = data['Age'].apply(lambda x: x**2)
print(data)