#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : test_frame.py
import process.SQLFrame as frame
from process import *


def test_frame():
    data = Data("../data/600519.SH.CSV")
    new = frame.get_frame(data)
    print(new)
