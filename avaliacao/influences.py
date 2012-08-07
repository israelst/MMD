#!/usr/bin/env python
# coding: utf-8

from collections import Counter
from outputty import Table


influence_table = Table()
influence_table.read('csv', '../datasets/p01_Influences.csv')
for row in influence_table:
    row[0] = row[0].strip()
    row[1] = row[1].strip()

influences = Counter()
for person in influence_table['Influnces']:
    influences[person] += 1
influenced = Counter()
for person in influence_table['Influenced']:
    influenced[person] += 1

table = Table(headers=['Rank', 'Person'])
for person, rank in influences.most_common(10):
    table.append((rank, person))
print 'Top 10 influences:'
print table

table = Table(headers=['Rank', 'Person'])
for person, rank in influenced.most_common(10):
    table.append((rank, person))
print 'Top 10 influenced:'
print table
