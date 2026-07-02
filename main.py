import pandas as pd
import pprintpp as p
# print(dir(pd))
# import numpy as np

# # # np.array()
# # numbers = np.array([10, 20, 30, 40])

# # print(numbers)
# # # print(dir(np))
# a=np.array([[[1,2]],[[3,4]]]) #here it will take from nested list
# print(a.ndim)
# # b=[[1,2],[3,4],[6,5]]
# # print(type(a.size))
# # arr=np.array([1,3,5])
# # print(arr.dtype)
# # print(arr[0])
# # arr = np.array([[1, 2], [3, 4], [1, 2],[4,5]])
# # print(arr.shape)
# # print(arr.shape)
# # arr = np.array([10, 20, 30, 40, 50])
# # print(arr+5)
# # print(arr*2)
# # print(np.sum(arr)
# # data = pd.Series([10, 20, 30, 40])

# # print(data)
# # data={"id":[1,2,3,4,5,6,7,8,9,10],"salary":[20000,30000,35000,60000,25000,12000,71000,25000,32000,10000]}


# # df=pd.DataFrame(data)
# # # print(df)
# # # print(df.head())
# # # print(df.head(3))
# # # print(df.tail())
# # # print(df.tail(3))
# # # print(df.shape)
# # # print(df.columns)
# # print(df.dtypes)
# # print(df.info())
# # print(df.describe())
# # print(df["id"])
# # print(df[["id","salary"]])
# # print(df.loc[0])
# # print(df.iloc[0])
# # print(df.iloc[0:3])
# # print(df[df["salary"]>30000])
# # print(df[(df["salary"]>30000) &(df["id"]>8)])
# # print(df[(df["salary"] > 30000) & (df["id"] > 25)])
# # # df["Bonus"] = df["salary"] * 0.10
# # # print(df)
# # df["Salary"] = df["salary"] + 5000
# # print(df)
# # arr = np.array([[1, 2], [3, 4], [1, 2]])
# # print(arr.shape)
# # print(arr.size)
# # arr = np.array([10,20,30,40])

# # print(arr+5)
# # students='{s1={"name":"sangeetha","age":21},s2={"name":"shirin","age":22},s3={"name":"sandhya","age":21}}'
# # print(len(students))
# # print(type(students))

# data = {
#     "name": "John",
#     "age": 25
# }
# # print(type(data))
# data='{
#      "name": "John",
    #   "age": 25
#   }'

# print(type(data))
# json_data = '{"name":"John","age":25}'
# print(type(json_data))

df=pd.read_csv("testing.csv")
print(df)







