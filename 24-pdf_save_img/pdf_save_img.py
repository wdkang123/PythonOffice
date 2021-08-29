import fitz
from pathlib import Path


imgdir = Path("images")

# 文件不存在 需要创建
if not imgdir.is_dir():
  imgdir.mkdir(parents=True)

def get_all_images(pdfpath):
  # 获取pdf中所有的图片
  pdf = fitz.open(pdfpath)

  xreflist = []
  for page_num in range(len(pdf)):
    # 获取某页所有的图片数据
    imgs = pdf.getPageImageList(page_num)
    for img in imgs:
      xref = img[0]
      if xref in xreflist:
        # 已经处理过 跳过
        continue
      # 获取图片信息
      pix = recoverpix(pdf, img)
      # 获取原始图像
      if isinstance(pix, dict):
        # 图像扩展名
        ext = pix["ext"]
        # 图像原始数据
        imgdata = pix["image"]
        # 图像颜色通道
        n = pix["colorspace"]
        # 图像保存路径
        imgfile = imgdir.joinpath(f"img-{xref}.{ext}")
      else:
        # 图像保存路径
        imgfile = imgdir.joinpath(f"img-{xref}.png")
        n = pix.n
        imgdata = pix.getImageData()
      if len(imgdata) <= 2048:
        # 图像大小至少大于或等于2KB 否则忽略
        continue
      # 保存图像
      print(imgfile)
      with open(imgfile, 'wb') as f:
        f.write(imgdata)
      # 不再重复处理相同的xref
      xreflist.append(xref)
      print(f"{imgfile} save")


def getimage(pix):
  # 像素色彩空间不为4 表示没有透明层
  if pix.colorspace.n != 4:
    return pix
  tpix = fitz.Pixmap(fitz.csRGB, pix)
  return tpix


def recoverpix(pdf, item):
  # 恢复图片 处理不同类型的图片 处理遮罩层
  xref = item[0]
  # xref 对应的遮罩层
  smask = item[0]
  if smask == 0:
    # 没有遮罩层 直接导出
    return pdf.extractImage(xref)

  pix1 = fitz.Pixmap(pdf, xref)
  pix2 = fitz.Pixmap(pdf, smask)
  # 完整性判断
  if not all([
    # 像素矩形相同
    pix1.irect  == pix2.irect,
    # 像素图都没有Alpha层
    pix1.alpha == pix2.alpha == 0,
    # pix2像素图每像素只有一维
    pix2.n == 1
  ]):
    pix2 = None
    return getimage(pix1)

  # 复制pix1 也用于添加alpha值
  pix = fitz.Pixmap(pix1)
  pix.setAlpha(pix2.samples)
  pix1 = pix2 = None
  return getimage(pix)


def main():
  pdfpath = Path("3.pdf")
  get_all_images(pdfpath)

main()
