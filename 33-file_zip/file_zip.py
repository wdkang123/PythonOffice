import zipfile
import tarfile
from pathlib import Path


# 压缩文件
path = "test"
newzip = zipfile.ZipFile("new.zip", "w")

# 压缩path目录下的所有文件
for p in Path(path).rglob("*"):
    newzip.write(p, compress_type=zipfile.ZIP_DEFLATED)
newzip.close()
print("done!")

# tar.gz格式 w:gz表示采用gzip算法压缩
tar = tarfile.open("new.tar.gz", "w:gz")
for p in Path(path).rglob("*"):
    tar.add(p)
tar.close()
print("done!")

# 解压缩文件
target_path = Path.cwd()
zippath = Path("new.zip")
# 创建ZipFile对象
zip_file = zipfile.ZipFile(zippath)
# 解压
zip_file.extractall(target_path)
zip_file.close()
print("done!")

# 解压缩tar.gz
path = "new.tar.gz"
target_path = "."

tar = tarfile.open(path, "r:gz")
# 获取压缩文件中所有文件的名称
file_names = tar.getnames()
print(f"tar zip files name: {file_names}")

# 解压
tar.extractall(target_path)
print("done!")
