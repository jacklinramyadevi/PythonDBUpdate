# -*- coding: utf-8 -*-

import time
import pandas as pd
import matplotlib.pyplot as plt
import json
import codecs



#jitem = {}
def load_pt_city(filename):
    with open(filename,'r',encoding='UTF-8') as f:
        jitem = json.loads(f.read())

        return jitem 

def read_cmb_excel(filename, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'CMB'
        city_item['provinceName'] = col_province[ri]
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri]
        city_item['areaName'] = col_area[ri]
        item_list.append(city_item)

    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))


def read_cmbc_excel(filename,jitem, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    #col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'CMBC'
        city_item['provinceName'] = col_province[ri]
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri]
        city_item['areaName'] = ''

        for rowi in range(len(jitem)):
            pnn = jitem[rowi]['provinceName']
            cnn = jitem[rowi]['cityName']
            rnn = jitem[rowi]['areaName']
            if pnn == city_item['provinceName'] and cnn == city_item['cityName'] and len(rnn) > 0:
                cc_item = {}
                cc_item['BANK_CODE'] = city_item['BANK_CODE']
                cc_item['provinceName'] = city_item['provinceName']
                cc_item['cityName'] = city_item['cityName']
                cc_item['areaName'] = rnn
                print(cc_item)
                item_list.append(cc_item)


    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))


def read_bosh_excel(filename,jitem, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    #col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'BOSH'
        city_item['provinceName'] = col_province[ri]
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri]
        city_item['areaName'] = ''

        for rowi in range(len(jitem)):
            pnn = jitem[rowi]['provinceName']
            cnn = jitem[rowi]['cityName']
            rnn = jitem[rowi]['areaName']
            if pnn == city_item['provinceName'] and cnn == city_item['cityName'] and len(rnn) > 0:
                cc_item = {}
                cc_item['BANK_CODE'] = city_item['BANK_CODE']
                cc_item['provinceName'] = city_item['provinceName']
                cc_item['cityName'] = city_item['cityName']
                cc_item['areaName'] = rnn
                print(cc_item)
                item_list.append(cc_item)

    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))


def read_comm_excel(filename,jitem, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    #col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'COMM'
        city_item['provinceName'] = col_province[ri]
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri]
        city_item['areaName'] = ''

        for rowi in range(len(jitem)):
            pnn = jitem[rowi]['provinceName']
            cnn = jitem[rowi]['cityName']
            rnn = jitem[rowi]['areaName']
            if pnn == city_item['provinceName'] and cnn == city_item['cityName'] and len(rnn) > 0:
                cc_item = {}
                cc_item['BANK_CODE'] = city_item['BANK_CODE']
                cc_item['provinceName'] = city_item['provinceName']
                cc_item['cityName'] = city_item['cityName']
                cc_item['areaName'] = rnn
                print(cc_item)
                item_list.append(cc_item)

    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))

def read_hxb_excel(filename,jitem, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    #col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'HXB'
        city_item['provinceName'] = col_province[ri]
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri]
        city_item['areaName'] = ''

        for rowi in range(len(jitem)):
            pnn = jitem[rowi]['provinceName']
            cnn = jitem[rowi]['cityName']
            rnn = jitem[rowi]['areaName']
            if pnn == city_item['provinceName'] and cnn == city_item['cityName'] and len(rnn) > 0:
                cc_item = {}
                cc_item['BANK_CODE'] = city_item['BANK_CODE']
                cc_item['provinceName'] = city_item['provinceName']
                cc_item['cityName'] = city_item['cityName']
                cc_item['areaName'] = rnn
                print(cc_item)
                item_list.append(cc_item)

    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))

def read_citic_excel(filename, xls_name, sheetname):
    # 代码示例:
    excel_path = xls_name
    d = pd.read_excel(excel_path, sheet_name=sheetname)
    print(d.keys())
    col_province = d['省']
    col_city = d['城市']
    col_area = d['区']

    MAX_COLUMN_LEN = len(col_city)
    print('MAX_COLUMN_LEN:', MAX_COLUMN_LEN)

    item_list = []
    for ri in range(len(col_city)):
        #print('city:',col_city[ri],'  area:',col_area[ri])
        city_item = {}
        city_item['BANK_CODE'] = 'CITIC'
        city_item['provinceName'] = col_province[ri].replace(' ','')
        if '市' not in col_city[ri]:
            col_city[ri] = col_city[ri] + '市'
        city_item['cityName'] = col_city[ri].replace(' ','')
        city_item['areaName'] = col_area[ri].replace(' ','')
        item_list.append(city_item)

    with codecs.open(filename,'w','utf-8') as f:
        jstr = f.write(json.dumps(item_list,ensure_ascii=False))




if __name__ == '__main__':

    begin_time = time.time()

    jitem = load_pt_city('E:\\workshop\\信用卡申请\\基础数据json\\pt_city_info.json')

    # filename = 'E:\\workshop\\信用卡申请\\基础数据json\\cmb_support_city.json'
    # read_cmb_excel(filename,r'E:\workshop\信用卡申请\银行网点\招商银行.xlsx', 'Sheet2')
    #print(jitem)

    

    # filename = 'E:\\workshop\\信用卡申请\\基础数据json\\cmbc_support_city.json'
    # read_cmbc_excel(filename,jitem,r'E:\workshop\信用卡申请\银行网点\民生银行.xlsx', 'Sheet1')
    
    # bank of shanghai
    # filename = 'E:\\workshop\\信用卡申请\\基础数据json\\bosh_support_city.json'
    # read_bosh_excel(filename,jitem,r'E:\workshop\信用卡申请\银行网点\上海银行.xls', 'Sheet1')
 

    # bank of comm
    # filename = 'E:\\workshop\\信用卡申请\\基础数据json\\comm_support_city.json'
    # read_comm_excel(filename,jitem,r'E:\workshop\信用卡申请\银行网点\交通银行.xlsx', 'Sheet2')

    # bank of hxb
    # filename = 'E:\\workshop\\信用卡申请\\基础数据json\\hxb_support_city.json'
    # read_hxb_excel(filename,jitem,r'E:\workshop\信用卡申请\银行网点\华夏银行.xlsx', 'Sheet1')

    # bank of citic
    filename = 'E:\\workshop\\信用卡申请\\基础数据json\\citic_support_city.json'
    read_citic_excel(filename,r'E:\workshop\信用卡申请\银行网点\中信银行.xls', 'Sheet1')




