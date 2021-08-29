import fitz
from pathlib import Path

# pip install pymupdf 由于历史原因 使用pympdf时 导入的库名为 fitz

pdf_path = Path("1.pdf")


def extract_all_ducument_text():
  # 提取PDF中所有的文字 缺点: 提取之后没有顺序
  # 打开pdf文件
  pdf = fitz.open(pdf_path)
  content = ""
  for page in pdf:
    # 获取文字
    text = page.getText()
    content += text
  with open("1.txt", "w") as f:
    f.write(content)

extract_all_ducument_text()


pdf_path = Path("2.pdf")
# 从bbox按顺序获取文字
def extract_all_document_text_by_block():
  # 提取PDF中的所有文字 通过区块读取文字 实现顺序读取
  # block中有很多信息可以用于排序 从而获取正确的顺序
  pdf = fitz.open(pdf_path)
  content = []
  for page in pdf:
    # 获取文本块
    blocks = page.getText("blockes")
    print(blocks)
    # 对bbox的y0坐标进行排序 以获取正常的顺序
    # blocks = sorted(blocks, key=lambda x:x[1])
    content.extend(blocks)
  with open("2.txt", "w") as f:
    # content = "\n".join([_[4] for _ in content])
    f.write(str(content))

extract_all_document_text_by_block()
