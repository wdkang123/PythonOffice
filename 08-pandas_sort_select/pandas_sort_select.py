import pandas as pd

# 数据排序
peoples = pd.read_excel("people.xlsx", index_col="id")
# by是根据字段 inplace就地执行 ascending为False是从大到小
peoples.sort_values(by="工资", inplace=True, ascending=False)
print(peoples)
print("============================")
'''
           名称  工资   靠谱
id                    
5       likui  44   no
4   songjiang  33   no
3        lisi  14  yes
2      wangwu  13   no
1    zhangsan  12  yes
'''

# 多列排序
peoples = pd.read_excel("people.xlsx", index_col="id")
peoples.sort_values(by=["靠谱", "工资"], inplace=True, ascending=[True, False])
print(peoples)
print("============================")

'''
           名称  工资   靠谱
id                    
5       likui  44   no
4   songjiang  33   no
2      wangwu  13   no
3        lisi  14  yes
1    zhangsan  12  yes
'''

# 数据过滤
peoples = pd.read_excel("people2.xlsx", index_col="id")
# 检查是都有None
print(peoples.isnull().any())
print("============================")
# 说明 分数 这列存在NaN
'''
名称    False
分数     True
年龄    False
性别    False
dtype: bool
'''

# 清除NaN的行
peoples.dropna(inplace=True)
print(peoples)
print("============================")

'''
          名称     分数  年龄 性别
id                        
1   zhangsan  111.0  12  F
2     wangwu  333.0  13  M
3       lisi  222.0  44  F
5      likui  312.0  13  M
'''

# 分数及格的女性(大于或等于xx分)
pass_rows = peoples[(peoples["性别"] == "F") & (peoples["分数"] >= 200)]
print(pass_rows)
print("============================")

'''
      名称     分数  年龄 性别
id                    
3   lisi  222.0  44  F
'''


# 定义一个函数
def score_50_to_90(a):
    return 100 <= a < 120


def age_20_to_30(a):
    return 10 <= a < 20


man_50_to_90 = peoples[peoples["性别"] == "F"]\
    .loc[peoples["分数"].apply(score_50_to_90)]\
    .loc[peoples["年龄"].apply(age_20_to_30)]
print(man_50_to_90)
print("============================")
'''
          名称     分数  年龄 性别
id                        
1   zhangsan  111.0  12  F
'''
