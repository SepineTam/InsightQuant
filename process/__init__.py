#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : __init__.py
import pandas as pd


class Data:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(data_path)
