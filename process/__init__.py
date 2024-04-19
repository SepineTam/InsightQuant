#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : __init__.py

"""TODO(0/2)
- function addition
- check function available
"""

import pandas as pd
import sqlite3
import re


class SQLData:
    def __init__(self, sql_path: str):
        self.sql_path = sql_path
        self.conn = sqlite3.connect(self.sql_path)
        self.cursor = self.conn.cursor()
        self.schema = None

    def connect(self):
        """连接数据库"""
        self.conn = sqlite3.connect(self.sql_path)
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        """执行的SQL语句"""
        self.cursor.execute(sql)

    def commit(self):
        """提交前面所要执行的SQL语句"""
        self.conn.commit()

    def close(self):
        """关闭数据库连接"""
        self.conn.close()

    def submit_sql(self, sql):
        self.connect()
        self.execute(sql)
        self.commit()
        self.close()


class Data(SQLData):
    def __init__(self, data_path: str, sql_path: str = "data/data.sqlite"):
        super().__init__(sql_path)
        self.data_path: str = data_path
        self.sql_path: str = sql_path
        self.table_name = self._get_table_name()
        self.data = pd.read_csv(data_path)

    def _get_table_name(self) -> str:
        """
        get table name based on name of csv file
        :return: table name
        """
        return re.sub(r"\D", "", self.data_path)

    def _schema(self, schema: dict = None) -> dict:
        """
        导入已经做好的schema
        :param schema: table structure
        :return: table structure in dict
        """
        default = {
            'Date': 'DATE PRIMARY KEY',  # 日期类型，作为主键
            'column1': 'INTEGER',  # 整数类型
            'column2': 'TEXT NOT NULL',  # 文本类型，不允许为空
            'column3': 'REAL'  # 浮点数类型
        }
        return default if schema is None else self.schema

    def update_schema(self, schema: dict = None):
        """
        exchange a new schema
        :param schema: table structure
        :return: None
        """
        self.schema = schema

    def get_schema(self) -> dict:
        return self.schema

    def creat_table(self) -> None:
        """
        create table base on the structure which is defined in schema
        :return: None
        """
        columns_with_types = ', '.join([
            f"{column_name} {data_type}" for column_name, data_type in self._schema().items()
        ])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_with_types});"

        self.submit_sql(create_table_sql)

    def get_data(self, column: str, index: str) -> str:
        """
        get data from sql table
        :param column: column which is the position of the data
        :param index: index which is the position of the data
        :return: the fixed value on the table
        """
        get_data_sql = ""
        self.submit_sql(get_data_sql)  # TODO: make the function with a return

    def change_data(self, column: str, index: str, value: str):
        """
        change data from sql table
        :param column: column which is the position of the data
        :param index: index which is the position of the data
        :param value: the changed value
        :return: whether the change was successful
        """
        change_data_sql = ""
        self.submit_sql(change_data_sql)

    def delete(self): pass

    def add(self): pass

    def update(self): pass

    def select(self): pass

    def insert(self): pass


