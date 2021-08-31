from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from pathlib import Path
from PyPDF4 import PdfFileReader, PdfFileWriter


# 给PDF添加水印
def create_watermark(content):
  # 创建水印
  file_name = "watermark.pdf"
  # 创建水印画布
  c = canvas.Canvas(file_name, pagesize = (30 * cm, 30 * cm))
  # 移动坐标原点[坐标系左下为(0, 0)]
  c.translate(10 * cm, 2 * cm)
  # 设置字体
  c.setFont("Helvetica", 80)
  # 指定描边的颜色
  c.setStrokeColorRGB(0, 1, 0)
  # 指定填充颜色
  c.setFillColorRGB(0, 1, 0)
  # 旋转45度 坐标系被转换
  c.rotate(45)
  # 指定填充颜色
  c.setFillColorRGB(0.6, 0, 0)
  # 设置透明度 1为不透明
  c.setFillAlpha(0.2)
  # 绘制文本
  c.drawString(3 * cm, 0 * cm, content)
  # 设置透明度
  c.setFillAlpha(0.4)
  # 关闭并保存文件
  c.save()
  return file_name


def add_watermark(input_pdf, output):
  # 添加水印
  watermark = Path("watermark.pdf")
  
  # 如果文件不存在则创建水印
  if not watermark.is_file():
    create_watermark("Python!!!")
  
  watermark_obj = PdfFileReader(str(watermark))
  watermark_page = watermark_obj.getPage(0)
  
  pdf_reader = PdfFileReader(input_pdf)
  pdf_writer = PdfFileWriter()
  
  # 给所有页面添加水印
  for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)
  
  with open(output, "wb") as out:
    pdf_writer.write(out)

add_watermark("text.pdf", "text-watermark.pdf")
