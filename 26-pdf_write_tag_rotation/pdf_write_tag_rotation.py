import fitz
import PyPDF4


# 写入文字
# 创建新的pdf
pdf = fitz.open()
# 新的一页pdf
page = pdf.newPage()

start_x = 50
start_y = 50

# [内容, 字体]
# china-s 黑体
# china-ss 宋体
# china-t 繁体
texts = [["Hello PDF!"], ], ["你好", "china-ss"]

for text in texts:
  # 文字内容的起点
  p = fitz.Point(start_x, start_y)
  rc = page.insertText(
    p,
    text[0],
    fontname=text[1] if len(text) == 2 else "helv",
    fontsize=11,
    # rotate角度 其他可以用值 90, 180, 270
    rotate=0
  )
  # 下移
  start_y += 20

pdf.save("text.pdf")
pdf.save("text2.pdf")


# 生成大纲
pdf = fitz.open("text2.pdf")
# 获取pdf的大纲
toc = pdf.getToC()
print(toc)
# 清空
toc = []
# 添加
toc.append([1, "标签1", 1])
toc.append([1, "标签2", 2])
pdf.setToC(toc)
print(toc)
# 保存
pdf.saveIncr()


# 旋转PDF页面
pdfReader = PyPDF4.PdfFileReader("text2.pdf")
# 获取第一页
page = pdfReader.getPage(0)
# 页面旋转90度
page.rotateClockwise(90)

pdfWriter = PyPDF4.PdfFileWriter()
pdfWriter.addPage(page)

with open("text2-rotation.pdf", "wb") as f:
  pdfWriter.write(f)
