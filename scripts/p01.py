#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

lines = csv.reader(open('datasets/p01_Influences.csv', 'rb'), delimiter=',', quotechar='"')

prepare_values = lambda values: [value.decode('utf-8').strip() for value in values]
ranking = lambda dic: [(len(v), k) for k, v in dic.iteritems()]

def add(dic, _from, _to):
    dic.setdefault(_from, [])
    dic[_from].append(_to)

influnces_dict = {}
influenced_dict = {}
for line in lines:
    influnces, influenced = prepare_values(line)
    add(influnces_dict, influnces, influenced)
    add(influenced_dict, influenced, influnces)
