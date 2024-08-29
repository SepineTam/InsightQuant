#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : chost.py

import pandas as pd

file_path = 'strategyDic/default.strategy.csv'
file = pd.read_csv(file_path)

print(file)

