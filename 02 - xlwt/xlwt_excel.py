import xlwt


# 创建xls类型文件对象
book = xlwt.Workbook()

# 新建名为Sheet1的对象
sheet = book.add_sheet("Sheet1")

# 写入数据到第一行第一列的单元格
# 按(row, col, value) 的方式添加数据
sheet.write(0, 0, "xlwt写入的数值")
# 重复对相同单元格赋值 程序会报错崩溃
sheet.write(0, 0, "写入的值")

# 保存工作簿
book.save("./people2.xls")
