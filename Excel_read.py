#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    Excel_read
Author:    Mrtutu
Date:    2018/3/13
Description:
------------------------------------

"""
import xlrd

data = xlrd.open_workbook('Excle.xls')

sheet0 = data.sheet_by_index(0)

nrows = sheet0.nrows
for i in range(nrows):
    print(sheet0.row_values(i))

nclos = sheet0.ncols
for i in range(nclos):
    print(sheet0.row_values(i))