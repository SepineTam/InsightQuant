#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : test_data_frame.py

from process import *


def test():
    csv_path = '../data/600519.SH.csv'
    data = Data(csv_path, "data/600519.sqlite")
    print(data)
