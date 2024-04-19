#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Author  : Sepine Tam
# @File    : __init__.py.py

from matplotlib import pyplot as plt


class Draw:
    def __init__(self):
        self.fig = plt.figure()

    def show(self):
        self.fig.show()
