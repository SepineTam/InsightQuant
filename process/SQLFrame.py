#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : SQLFrame.py

from . import Data


def get_frame(data: Data):
    return data.get_schema()


def change_schema(data: Data, schema: dict):
    data.update_schema(schema)
    return data
