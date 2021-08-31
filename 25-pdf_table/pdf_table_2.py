from pathlib import Path
import camelot
import cv2


def use_camelot(pdfpath):
  tables = camelot.read_pdf(str(pdfpath))
  tables.export("table2.csv", f="csv", compress=True)


pdfpath = Path("2.pdf")
print(pdfpath)
use_camelot(pdfpath)
