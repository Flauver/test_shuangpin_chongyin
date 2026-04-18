from collections import defaultdict
from typing import DefaultDict
from re import *

频率表: DefaultDict[str, int] = defaultdict(int)

with open('snow_pinyin.dict.yaml') as f:
    text = f.read()
for 行 in findall(r'^.+\t([-a-z]+)\d(?:\t(\d+))?$', text, flags=M):
    if 行[1] == '':
        continue
    频率表[行[0]] = int(行[1])

with open('snow_pinyin.base.dict.yaml') as f:
    text = f.read()

for 行 in findall(r'^.+\t([a-z\d ]+)\t(\d+)$', text, flags=M):
    for 码 in 行[0].split(' '):
        频率表[码[:-1]] += int(行[1])

频率表 = sorted(频率表.items(), key=lambda x: x[1], reverse=True)
频率表 = [x for x in 频率表 if x[1] != 0]
with open('freq.txt', 'w') as f:
    f.write('\n'.join([f'{x[0]}\t{x[1]}' for x in 频率表]))
