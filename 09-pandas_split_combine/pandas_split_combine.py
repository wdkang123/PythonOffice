import pandas as pd


peoples = pd.read_excel("people.xlsx")

# 将FullName拆分成 姓氏 和 名字 列
df = peoples["Full Name"].str.split(expand=True)
# 创建 姓氏 列
peoples["姓氏"] = df[0]
# 创建 名字 列
peoples["名字"] = df[1]

print(peoples)
print("===================")
'''
   id         Full Name        姓氏          名字
0   1       Carig Davis     Carig       Davis
1   2  Samantha Montoya  Samantha     Montoya
2   3   Ivan Montgomery      Ivan  Montgomery
3   4       Allen Smith     Allen       Smith
4   5    Mark Dominguez      Mark   Dominguez
'''

# 多表联合
students = pd.read_excel("student.xlsx", sheet_name="Sheet1")
score = pd.read_excel("score.xlsx", sheet_name="Sheet1")
age = pd.read_excel("age.xlsx", sheet_name="Sheet1")

# 合并
# fillna 将 NaN 填充为0
table = students.merge(score, how="left", on="id").fillna(0)
table["分数"] = table["分数"].astype(int)

table2 = table.merge(age, how="left", on="id").fillna(0)
table2["年龄"] = table2["年龄"].astype(int)

print(table2)
print("===================")

'''
   id                名称  分数  年龄
0   1       Carig Davis  83  22
1   2  Samantha Montoya  44  33
2   3   Ivan Montgomery  99  15
3   4       Allen Smith   0  17
4   5    Mark Dominguez  87  18
'''

# 读取时 将id设置为index 读入的DataFrame对象中就不存在名为id的列
students = pd.read_excel("student.xlsx", sheet_name="Sheet1", index_col="id")
score = pd.read_excel("score.xlsx", sheet_name="Sheet1", index_col="id")

table = students.merge(score, how="left", left_on=students.index, right_on=score.index).fillna(0)
print(table)

'''
   key_0                名称    分数
0      1       Carig Davis  83.0
1      2  Samantha Montoya  44.0
2      3   Ivan Montgomery  99.0
3      4       Allen Smith   0.0
4      5    Mark Dominguez  87.0
'''
