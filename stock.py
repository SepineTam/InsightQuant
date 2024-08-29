#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : stock.py

class Stock:
    def __init__(self, code: str):
        """
        初始化函数
        :param code: 股票代码，股票代码是股票的唯一表示码
        """
        self._code = code  # 股票代码
        self._average_price = 0  # 股票的平均价格
        self._holding = 0  # 股票的持仓情况
        self._total = self._average_price * self._holding  # 总持仓价格
        self._position = {
            'code': self._code,
            'holding': self._holding,
            'price': self._average_price,
            'total': self._total
        }

    def __repr__(self):
        _repr = ""
        _position = self.get_position()
        for _key, _value in _position.items():
            if _key == 'price' or _key == 'total':
                _value = str(_value) + " RMB"
            _repr += f"{_key.ljust(10)}: {str(_value).rjust(10)}"
            _repr += "\n"
        return _repr

    def get_average_price(self):
        return self._average_price

    def get_holding(self):
        return self._holding

    def get_total(self):
        return self._total

    def get_position(self):
        """
        获取当前股票的头寸配置
        :return: 当前股票的头寸
        """
        position = {
            'code': self._code,
            'holding': self._holding,
            'price': self._average_price,
            'total': self._total
        }  # code: 股票代码, holding: 持股数, price: 股票的平均价格
        self._position = position  # 刷新一下头寸情况
        return self._position

    def buy(self, number: int, price: float = None):
        if price is None:
            price = self._average_price
        self._holding += number

    def sell(self):
        pass

    def _settle(self):
        pass

    def _close(self):
        pass

    def close(self):
        choice = input('确定平仓吗？Y/n')
        if choice.upper() == 'Y':
            self._close()
            _flag = True
        else:
            _flag = False
        return _flag

    @property
    def total(self):
        return self._total


if __name__ == '__main__':
    stock = Stock('600009.SH')
    print(stock.total)
