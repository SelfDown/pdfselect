#!/usr/bin/env python
# -*- coding: utf_8 -
from PyPDF2 import PdfFileReader, PdfFileWriter


def readJSON():
	import json
	file=open("config.json")
	content=file.read()
	print content
	data=json.loads(content)
	return data
data = readJSON()
infn = data['source_path']
outfn = data['target_path']
# 获取一个 PdfFileReader 对象
pdf_input = PdfFileReader(open(infn, 'rb'))
# 获取 PDF 的页数
page_count = pdf_input.getNumPages()



# 获取一个 PdfFileWriter 对象
pdf_output = PdfFileWriter()
for i in data["print_pages"]:
	# 返回一个 PageObject
	page = pdf_input.getPage(i)
	# 将一个 PageObject 加入到 PdfFileWriter 中
	pdf_output.addPage(page)
# 输出到文件中
pdf_output.write(open(outfn, 'wb'))