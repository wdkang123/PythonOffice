import pandas as pd
from datetime import date, timedelta


filepath = "people.xlsx"
# 读出工作簿名为Sheet1的工作表
people = pd.read_excel(filepath, sheet_name="Sheet1")
print(people)
print("=====1=====")

# header = 2 表示从第3行开始 相当于跳过了第2行
people1 = pd.read_excel(filepath, header=2, sheet_name="Sheet1")
print(people1)
print("=====2=====")

# skiprows 跳过开头几行 usecols表示使用哪些列的数据
people3 = pd.read_excel(filepath, sheet_name="Sheet1", skiprows=4, usecols="B:C")
print(people3)
print("=====3=====")

# 指定id列为索引 dtype设置某一列数据的类型
people2 = pd.read_excel(filepath, sheet_name="Sheet1", index_col="id", dtype={"name": str, "data": str})
print(people2)
print("=====4=====")

# 通过字典形式构建DataFrame
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["张三", "李四", "王五"],
    "age": [26, 50, 30]
})

# 自定义索引
df = df.set_index("id")
print(df)

df.to_excel("people_result.xlsx")
print("=====5=====")


people = pd.read_excel("./people2.xlsx", skiprows=4, usecols="B:E", dtype={
    "id": str,
    "name": str,
    "gender": str,
    "data": str
})

# 开始日期
startday = date(2021, 7, 1)
for i in people.index:
    # 累加ID
    people.at[i, "id"] = i + 1
    # 判断性别
    people.at[i, "gender"] = "Male" if i % 2 == 0 else "Female"
    people.at[i, "data"] = date(startday.year + i, startday.month, startday.day)

# inplace 表示就地修改 DateFrame 不必再重新创建一个新的DateFrame来存储修改后的状态
people.set_index("id", inplace=True)
people.to_excel("people2_result.xlsx")




