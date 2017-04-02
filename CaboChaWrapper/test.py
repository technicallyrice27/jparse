#!/usr/bin/python
# -*- coding: utf-8 -*-

import CaboCha

# c = CaboCha.Parser("");
c = CaboCha.Parser()

sentence = """
ここはちょうど、バラード大陸と向かい合っている海岸だ。だから攻めてくるならここしかない。
そう判断したのは宰相ベルムンドだ。迂回して反対側の海岸から攻められる可能性もあるのでは、と私は切り出した。
しかし大部隊がそんな迂回をしていれば嫌でも目立つし、何より獣の園の獣がそんな回りくどい事をするとは思えないとベルムンドは言い切った。
"""

print(c.parseToString(sentence))

tree =  c.parse(sentence)

print(tree.toString(CaboCha.FORMAT_LATTICE))
