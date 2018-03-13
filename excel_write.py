#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    excel
Author:    Mrtutu
Date:    2018/3/13
Description:
------------------------------------

"""

import xlwt


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('test', cell_overwrite_ok=True)

sheet.write(0,0,'EnglishName')
sheet.write(1,0,'Mrtutu')

txt1 = '中文名字'
sheet.write(0,1,txt1)

txt2 = '兔兔'
sheet.write(1,1,txt2)

book.save('Excle.xls')
