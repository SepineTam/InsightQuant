#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved
#
# @Author  : Sepine Tam
# @File    : simulink.py.py

import numpy as np
from strategy import Strategy


class Simulink:
    def __init__(self):
        self._init_money = 10000000  # 初始金额默认为100万
        self.strategy = "default"

    def mk_strategy(self):
        """
        从策略列表中提取策略进行操作
        :return:
        """

        return None

    def get_money(self):
        return self._init_money

    def change_money(self, money):
        self._init_money = money

    def get_strategy(self):
        return self.strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
