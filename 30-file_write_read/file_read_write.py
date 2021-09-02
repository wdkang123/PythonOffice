import time

# 读写文件

# 打开文件
f = open("test.txt", "r", encoding="utf-8")
# 读取内容
all_content = f.read()
print(all_content)
# 关闭文件句柄
f.close()

print("===============================")

# 逐行读取内容
f = open("test.txt", "r", encoding="utf-8")
for line in f.readlines():
    print(line)
    print("---")
f.close()

print("===============================")

# 以只读的方式打开
fr = open("test.txt", "r", encoding="utf-8")
# 以只写的方式打开
fw = open("test.txt", "w", encoding="utf-8")

fw.write("新的内容")
print(f"读取 {fr.read()}")

fr.close()
fw.close()

# 不用close的写法 会自动关闭
with open("test.txt", "r", encoding="utf-8") as f:
    all_content = f.read()
    print(all_content)

print("==============================")


# 任何实现了 __enter__ 和 __exit__ 方法的对象 都可以称为上下文管理器对象
# 自定义一个
class myopen():
    # 模拟with关键字使用open的方法
    def __init__(self, filepath, mode, encode):
        self.filepath = filepath
        self.mode = mode
        self.encode = encode

    def __enter__(self):
        print("打开文件")
        self.f = open(self.filepath, self.mode, encoding=self.encode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.f.close()


with myopen("test.txt", "r", "utf-8") as f:
    res = f.read()
    print(res)

print("==============================")

# 写入二进制
with open("test2.txt", "wb") as f:
    f.write("写入的是二进制".encode("utf-8"))
with open("test2.txt", "rb") as f:
    res = f.read()
    print(res.decode("utf-8"))

# 判断是否存在
# 存在则会抛出FileExistsError: [Errno 17] File exists的异常
# 不存在则新建
with open("test2.txt", "x") as f:
    f.write("写入的是二进制2")
