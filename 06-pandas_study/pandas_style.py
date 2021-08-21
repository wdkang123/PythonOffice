import pandas as pd


# 实例化Series对象
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="s1")

# 输出Series对象
print(s1)
# 输出Series对象的索引
print(s1.index)
# 输出Series对象中索引为1的值
print(s1[1])

# 输出结果
'''
1    1
2    2
3    3
Name: s1, dtype: int64
Int64Index([1, 2, 3], dtype='int64')
1
'''

print("---------------")
# 创建Series对象
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="A")
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name="B")
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name="C")

# 创建Series对象实例化DataFrame对象
df = pd.DataFrame([s1, s2, s3])
print(df)
'''
     1    2    3
A    1    2    3
B   10   20   30
C  100  200  300
'''
print("---")
# 通过字典形式构建DataFrame对象
df2 = pd.DataFrame({
    s1.name: s1,
    s2.name: s2,
    s3.name: s3
})
print(df2)
'''
   A   B    C
1  1  10  100
2  2  20  200
3  3  30  300
'''

print("---")
