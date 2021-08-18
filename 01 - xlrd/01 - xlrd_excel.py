import xlrd

# 1 读取xlsx
book = xlrd.open_workbook("./xlrd_excel.xlsx")

# 读取sheet
# 获取第1个sheet
sheet = book.sheets()[0]
# sheet = people.sheet_by_index(0)
# sheet = people.sheet_by_name("Sheet1")

# 读取表格
# sheet.cell_value(row, col)
data1 = sheet.cell_value(1, 0)
data2 = sheet.cell_value(1, 0)
print(f"data1: {data1}")
print(f"data2: {data2}")

# 读取所有的工作表
sheets = book.sheets()
for sheet in sheets:
    # 行数
    nrows = sheet.nrows
    # 列数
    ncols = sheet.ncols
    for row in range(0, nrows):
        for col in range(0, ncols):
            print(sheet.cell_value(row, col))

# 读入日期
time_value1 = sheet.cell_value(1, 6)
time_value2 = sheet.cell_value(2, 6)
# 将读入的日期转换为元组的形式
# (2019, 5, 6, 12, 10, 32)
time_tuple = xlrd.xldate_as_tuple(time_value1, 0)

# 将日期数据转换为datetime对象
time_datetime = xlrd.xldate_as_datetime(time_value1, 0)
# 将datetime对象格式化转化为对应的字符串
# 2019-05-06
time_str = time_datetime.strftime("%Y-%m-%d %H:%M:%S")







