from pathlib import Path
import pdfplumber
import pandas as pd


def use_pdfplumber(pdfpath):
  pdf = pdfplumber.open(pdfpath)
  # 获取具有表格的某页pdf
  p0 = pdf.pages[0]
  # 获取pdf中的表格
  try:
    table = p0.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    df.to_csv("table1.csv")

  except Exception as e:
    print("无法解析pdf中的表格")
    raise e

pdfpath = Path("1.pdf")
print(pdfpath)
use_pdfplumber(pdfpath)
