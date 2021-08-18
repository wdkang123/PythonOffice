import xlrd
from xlutils.copy import copy

# 读入数据 获取Book对象
# formatting_info=True格式
rd_book = xlrd.open_workbook("./xlutils_test.xlsx", formatting_info=True)
# 获取工作簿中第一个工作表 方便后续操作
rd_sheet = rd_book.sheets()[0]

# 复制Book对象为WorkBook对象
wt_book = copy(rd_book)
# 从workbook对象中获取Sheet对象
wt_sheet = wt_book.get_sheet(0)
# 循环处理每一行的第一列数据 修过其中的内容
for row in range(rd_sheet.nrows):
    wt_sheet.write(row, 0, "修改内容")
wt_book.save("./xlutils_test_copy.xls")
