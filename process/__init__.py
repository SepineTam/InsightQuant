#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : __init__.py

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

    def _schema(self) -> dict:
        return self.schema

    def creat_table(self) -> None:
        """
        create table base on the structure which is defined in schema
        :return: None
        """
        columns_with_types = ', '.join([f"{column_name} {data_type}" for column_name, data_type in self._schema().items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_with_types});"

        self.execute(create_table_sql)
        self.commit()
        self.close()

    def get_data(self, column: str, index: str) -> str:
        """
        get data from sql table
        :param column: column which is the position of the data
        :param index: index which is the position of the data
        :return: the fixed value on the table
        """
        # get_data_sql = f"SELECT {column} FROM {}"
        pass

    def change_data(self, column: str, index: str, value: str) -> bool:
        """
        change data from sql table
        :param column: column which is the position of the data
        :param index: index which is the position of the data
        :param value: the changed value
        :return: whether the change was successful
        """
        pass
