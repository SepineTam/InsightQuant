#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : error.py

import numpy as np


def average_error(true_data, pr_data):
    error = true_data - pr_data
    ave_error = np.mean(np.abs(error))
    return ave_error
