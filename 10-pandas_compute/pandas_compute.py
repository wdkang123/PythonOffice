import pandas as pd


# 统计运算基础
df = pd.DataFrame(
    [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
    columns=["col1", "col2", "col3", "col4"]
)
print(df)
print("=====")
'''
   col1  col2  col3  col4
0     1     1     1     1
1     2     2     2     2
2     3     3     3     3
'''

# mean 方法用来求某一行或列的平均数
result = df.mean(axis=1)
print(result)
print("======")
'''
0    1.0
1    2.0
2    3.0
dtype: float64
'''

# 删除某一行 或者 某一列
result = df.drop("col4", axis=1)
print(result)
print("======")
'''
   col1  col2  col3
0     1     1     1
1     2     2     2
2     3     3     3
'''

# axis=1将作用于每行中的所有列
# axis=0将作用于每列中的所有行

# 多种运算
peoples = pd.read_excel("peoples.xlsx", index_col="id")
column_name = ["小测1", "小测2", "小测3"]

# 对每一行中的每一列进行求和
row_sum = peoples[column_name].sum(axis=1)
# 对每一行中的每一列进行求平均值
row_mean = peoples[column_name].mean(axis=1)

total = "总分"
average = "平均分"
peoples[total] = row_sum
peoples[average] = row_mean
column_name += [total, average]

# axis默认为0 对每一列中的每一行进行求平均操作
col_mean = peoples[column_name].mean()
col_mean["名称"] = "Summary"
# append 方法添加新的一行 ignore_index为True表示忽略index
peoples = peoples.append(col_mean, ignore_index=True)

print(peoples)
print("======")
'''
                 名称   小测1    小测2   小测3     总分        平均分
0       Carig Davis  88.0  100.0  88.0  276.0  92.000000
1  Samantha Montoya  30.0   76.0  35.0  141.0  47.000000
2   Ivan Montgomery  55.0   99.0  55.0  209.0  69.666667
3       Allen Smith  90.0   90.0  30.0  210.0  70.000000
4    Mark Dominguez  76.0   70.0  99.0  245.0  81.666667
5           Summary  67.8   87.0  61.4  216.2  72.066667
'''

# 非空元素计算
peoples.count()
# 最小值
peoples.min()
# 最大值
peoples.max()
# 最小值的位置
# peoples.idxmin()
# 最大值的位置
# peoples.idxmax()
# 10%分位数
peoples.quantile(0.1)
# 求和
peoples.sum()
# 均值
peoples.mean()
# 中位数
peoples.median()
# 众数
peoples.mode()
# 方差
peoples.var()
# 标准差
peoples.std()
# 平均绝对偏差
peoples.mad()
# 偏度
peoples.skew()
# 峰度
peoples.kurt()
# 一次性输出多个描述性统计指标
peoples.describe()
