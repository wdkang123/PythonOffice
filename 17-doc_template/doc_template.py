from mailmerge import MailMerge

# pip install docx-mailmerge

template = "doc_templates.docx"

doc = MailMerge(template)

# 将内容添加到Word模板文件中 参数名与Word模板中的域名相同
doc.merge(
  name="二两",
  id="111222333",
  year="2021",
  month="8",
  day="30"
)

doc.write("doc_templates_new.docx")
