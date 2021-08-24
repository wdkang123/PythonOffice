import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


students = pd.read_excel("students.xlsx")
score = "分数"
age = "年龄"

# 传入字体路径 实例化对应的字体
myfont = FontProperties(fname="C:/Windows/Fonts/SimHei.ttf")

# 绘制散点图
students.plot.scatter(x=score, y=age)
plt.title("学生分数", fontsize=16, fontweight="bold", fontproperties=myfont)
plt.xlabel(score, fontproperties=myfont)
plt.ylabel(age, fontproperties=myfont)
plt.show()
