import pandas as pd

data=pd.DataFrame({
    'Date':['2023-07-01','2023-07-01','2023-07-02','2023-07-02','2023-07-03'],
    'Product':['A','B','A','C','B'],
    'Price':[1000,1500,800,2000,1200],
    'Quantity':[5,3,7,2,4]
    })

print("=== 원본 데이터 ===")
print(data)

sorted_data=data.sort_values(by='Price', ascending=False)
print("\n=== 데이터 정렬 ===")
print(sorted_data)

filtered_data=data[data['Price']>=1000]
print("\n=== 데이터 필터링 ===")
print(filtered_data)

grouped_data=data.groupby('Product')['Price'].mean()
print("\n=== 데이터 그룹화와 집계 ===")
print(grouped_data)

data['TotalPrice']=data['Price']*data['Quantity']
print("\n=== 데이터 변형 ===")
print(data) 

additional_data=pd.DataFrame({
    'Date':['2023-07-03','2023-07-04'],
    'Product':['A','B'],
    'Price':[900,1300],
    'Quantity':[6,5]
})

merged_data=pd.concat([data,additional_data],ignore_index=True)
print("\n=== 데이터 병합 ===")
print(merged_data)

