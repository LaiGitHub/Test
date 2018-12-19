#!/usr/bin/python
# -*- coding: utf-8 -*-
# 数据库帮助类
import pymysql

import datetime
from setting.sql_setting import sql_setting


# 根据数据库配置 ，获取数据库连接
def get_db_connect():
    address = sql_setting['address']
    name = sql_setting['name']
    password = sql_setting['password']
    database = sql_setting['database']
    return pymysql.connect(address, name, password, database, charset='utf8')


# 插入数据
# table_name 表名
# data_dict 数据字典
# Example :
#
# data_dict = {
#     "product_name": "MM",
#     "client": "android",
#     "bussiness": "search",
#     "data_type": "time_delay",
#     "data_value": "1.75",
#     "network": "wifi",
#     "remark": "",
#     "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# }
#
def insert_data(table_name, data_dict):
    # try:
    data_values = "(" + "%s," * (len(data_dict)) + ")"
    data_values = data_values.replace(',)', ')')
    dbField = data_dict.keys()
    dataTuple = tuple(data_dict.values())
    dbField = str(tuple(dbField)).replace("'", '')
    conn = get_db_connect()
    cursor = conn.cursor()
    sql = """ insert into %s %s values %s """ % (table_name, dbField, data_values)
    params = dataTuple
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()


def test_insert_data():
    table_name = "hefeixin_2018"
    # 插入的数据
    data_dict = {
        "product_name": "MM",
        "client": "android",
        "bussiness": "search",
        "data_type": "time_delay",
        "data_value": "1.75",
        "network": "wifi",
        "remark": "",
        "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    insert_data(table_name, data_dict)
    # result = insert_data(table_name, data_dict)
    # print (result)


if __name__ == '__main__':
    test_insert_data()
