import numpy as np
numbers = [1, 2, 3, 4, 5]
arr=np.array(numbers)
print(arr)
print(arr*2)
print(arr + 10)
print(arr ** 2)
print(arr.mean())
print(arr.sum())   

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix.shape)
print(matrix[1])
print(matrix[1,2])



import pandas as pd

data = {
    "name": ["Likitha", "Rahul", "Ananya"],
    "age": [25, 23, 27],
    "grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.columns)
print(df["name"])
print(df[df["grade"] == "A"])

df["passed"] = df["grade"] == "A"
print(df)

print(df.describe())
print(df.isnull().sum())