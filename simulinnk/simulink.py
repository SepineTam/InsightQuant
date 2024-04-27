#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved
#
# @Author  : Sepine Tam
# @File    : simulink.py.py

import numpy as np


def default(self, time, code): pass


class Simulink():
    def __init__(self, init_fund):
        self.fund = init_fund
        self.exchange = np.array([])

    def _get_price(self, time, code, rule=default):
        """
        获取{code}股票在{time}时候的报价，可以选择rule(获取规则)
        :param time: 交易时刻
        :param code: 股票代码
        :param rule: 规则
        :return: 股票报价
        """
        return rule(time, code)

    def process(self, time, quantity, code):
        """
        记录{code}股票在{time}时刻交易{quantity}的行为action
        :param time: 交易时刻
        :param quantity: 交易数量
        :param code: 股票代码
        :return: None
        """
        price = self._get_price(time, code)
        _exchange = {
            'price': price,
            'quantity': quantity,
            'code': code
        }
        self.exchange = np.append(_exchange)
