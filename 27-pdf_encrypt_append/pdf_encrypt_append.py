import PyPDF4


# 加密PDF
pdfReader = PyPDF4.PdfFileReader("text.pdf")
pdfWriter = PyPDF4.PdfFileWriter()

# 将内容读取并添加到pdfWriter中
for pagenum in range(pdfReader.numPages):
  pdfWriter.addPage(pdfReader.getPage(pagenum))

# 加密
pdfWriter.encrypt("123456")
with open("text-encrypt.pdf", "wb") as f:
  pdfWriter.write(f)


# 合并pdf
pdfReaders = [PyPDF4.PdfFileReader("text.pdf"), PyPDF4.PdfFileReader("text2.pdf")]
pdfWriter = PyPDF4.PdfFileWriter()
for pdfReader in pdfReaders:
  for pagenum in range(pdfReader.numPages):
    page = pdfReader.getPage(pagenum)
    pdfWriter.addPage(page)

# 持久化
with open("text_text2.pdf", "wb") as f:
  pdfWriter.write(f)

