#!/usr/bin/env python
# coding: utf-8

from collections import Counter, defaultdict
from outputty import Table


class Influences(object):
    def __init__(self, filename):
        self.table = Table()
        self.table.read('csv', filename)
        self._cleanup()

    def _cleanup(self):
        for row in self.table:
            row[0] = row[0].strip()
            row[1] = row[1].strip()

    def _most(self, column, number):
        counter = Counter()
        for person in self.table[column]:
            counter[person] += 1
        return counter.most_common(number)

    def _rank_table(self, data):
        table = Table(headers=['Rank', 'Person'])
        for person, rank in data:
            table.append((rank, person))
        return table

    def most_influences(self, number):
        return self._rank_table(self._most('Influnces', number))

    def most_influenced(self, number):
        return self._rank_table(self._most('Influenced', number))

    def influence_map(self):
        result = defaultdict(list)
        for influnce, influenced in self.table:
            result[influnce].append(influenced)
        return result

def main():
    influences = Influences('../datasets/p01_Influences.csv')
    most_influential = influences.most_influences(10)
    most_influenced = influences.most_influenced(10)
    print 'Top 10 influnces persons:'
    print most_influential
    print 'Top 10 influenced persons:'
    print most_influenced
    total = len(set(influences.table['Influnces'] + \
                    influences.table['Influenced']))
    print 'Total of persons:', total

if __name__ == '__main__':
    main()
