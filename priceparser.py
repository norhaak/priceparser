#!/usr/bin/env python

from urllib import urlretrieve
import os
import xlrd
import pyExcelerator as pyxl


src_url = ("http://www.prixagriculture.org/prix-des-produits?AAPrice"
        "[REGION_ID]=5&AAPrice[PROVINCE_ID]=&AAPrice[TYPE_MARKET_ID]=2&AAPrice"
        "[productFamilyId]=&exportXLS=true")
tmpfile = '/tmp/prices.xls'
try:
    #urlretrieve(src_url, tmpfile)
    book = pyxl.parse_xls(tmpfile)
    data =book[0][1]
    len_data = len(data)/5
    print('{:*^40}'.format('Products'))
    for i in range(1,len_data):
        result = '{0:<30} {1:<5} {2:<5}'.format(data[i,0], data[i,2], data[i,1])
        print(result)
finally:
    pass
