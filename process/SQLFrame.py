#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : SQLFrame.py

from . import Data


class SQLFrame(Data):
    def _schema(self, schema: dict = None) -> dict:
        """
        设计/导入已经做好的schema
        :param schema: table structure
        :return: table structure in dict
        """
        default = {
            'Date': 'DATE',  # 日期类型
            'column1': 'INTEGER PRIMARY KEY',  # 整数类型，作为主键
            'column2': 'TEXT NOT NULL',  # 文本类型，不允许为空
            'column3': 'REAL'  # 浮点数类型
        }
        return default if schema is None else self.schema

    def update_schema(self, schema: dict = None):
        self.schema = schema
