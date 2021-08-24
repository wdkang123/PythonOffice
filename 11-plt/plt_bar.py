import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


students = pd.read_excel("students.xlsx")
name = "名称"
score = "分数"
age = "年龄"

# sort_values 方法排序 inplace表示原地修改 ascending=False表示从大到小
students.sort_values(by=score, inplace=True, ascending=False)
# 绘制成柱状图
plt.bar(students[name], students[score], color="orange")
# Font Properties 文字属性
# 传入字体路径 实例化对应的字体
myfont = FontProperties(fname="C:/Windows/Fonts/SimHei.ttf")
# 指定渲染字体
# 标题
plt.title("学生分数", fontproperties=myfont, fontsize=16)
# x轴
plt.xlabel(name, fontproperties=myfont)
# y轴
plt.ylabel(score, fontproperties=myfont)
# x旋转一下 方便显示名字
plt.xticks(students[name], rotation=90)
# 紧凑型布局
plt.tight_layout()
plt.show()




