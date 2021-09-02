from pathlib import Path
import time

# 获取文件大小 文件创建时间、修改时间


def get_filesize(filepath):
    # 获取文件大小 单位为B
    fsize = Path(filepath).stat().st_size
    # B转MB
    fsize = fsize / float(1000 * 1000)
    return round(fsize, 4)


fsize = get_filesize("test.txt")
print(f"文件大小为: {fsize}MB")


def get_time(timestamp):
    # 格式化时间戳
    t = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H-%M-%S", t)


filepath = "test.txt"

# 文件创建时间
ctime = Path(filepath).stat().st_ctime
ctime = get_time(ctime)

# 文件修改时间
mtime = Path(filepath).stat().st_mtime
mtime = get_time(mtime)

print(f"创建时间: {ctime}, 修改时间: {mtime}")
