import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


students = pd.read_excel("students.xlsx")
name = "名称"
score = "分数"
age = "年龄"

# 指定默认字体 正常显示中文版标签
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 解决负号 显示为方块的问题
plt.rcParams["axes.unicode_minus"] = False

# 传入字体路径 实例化对应的字体
myfont = FontProperties(fname="C:/Windows/Fonts/SimHei.ttf")
# 绘制折线图
students.plot(y=[score, age])
plt.title("学生分数", fontproperties=myfont, fontsize=16, fontweight="bold")

# 重绘x轴坐标
plt.xticks(students.index)
plt.show()


