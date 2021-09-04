import os
from pathlib import Path
from collections import Counter


# 创建文件夹
os.makedirs("d1/d2")
# 或者
Path("d3/d4").mkdir(parents=True)

# 判断文件是否存在
txtpath = Path("1.txt")
print(txtpath.exists())
print("================================")

# 获取当前程序的工作目录
nowpath = Path.cwd()
print(nowpath)
print("================================")

# 相对于当前工作目录
codepath = nowpath.joinpath("..", "code")
print(codepath)
print("================================")

# 判断是否为文件夹
txtpath = Path("1.txt")
print(txtpath.is_dir())
print("================================")

# 判断是否为文件 True表示是文件
txtpath.is_file()

# 判断路径是否相同
txtpath = Path("1.txt")
txt2path = Path("1.txt")
txtpath.samefile(txt2path)

# 获取文件名、文件扩展名、文件所在目录等信息
print(txtpath.name)
print(txtpath.suffix)
print(txtpath.parent)
print("================================")


# 寻找扩展名为py的文件个数
def findallpyfile(dir):
    # 以递归形式遍历dir文件夹 找寻满足py条件的文件
    for p in dir.rglob("*.py"):
        # 深度
        depth = len(p.relative_to(dir).parts)
        print(p.name, depth)

print("================================")
findallpyfile(Path.cwd())


# 计算出不同类型的文件的个数
gen = []
# 遍历当前文件夹中的文件
for i in Path.cwd().iterdir():
    # 将文件类型添加到list中
    gen.append(i.suffix)
print(Counter(gen))
print("================================")




