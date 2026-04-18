from os import replace
from re import *

当量: dict[str, float] = {}

with open('当量.txt') as f:
    text = f.read()
for 行 in findall(r'^([a-z]+)\t([\d.]+)$', text, flags=M):
    当量[行[0]] = float(行[1])

def 分割(text: str) -> tuple[str, str]:
    group = match(r'^(?:n|m|ng)$', text)
    if group:
        return ('', text)
    group = match(r'^([bpmfdtnlgkhjqxzcsryw]h?)(.+)$', text)
    if group:
        return (group.group(1), group.group(2))
    return ('', text)

def 拼运(text: str) -> str:
    声, 韵  = 分割(text)
    声 = 声.replace('zh', 'v')
    声 = 声.replace('ch', 'i')
    声 = 声.replace('sh', 'u')
    拼韵 = 韵.replace('iong', 's')
    拼韵 = 拼韵.replace('iang', 'd')
    拼韵 = 拼韵.replace('uang', 'd')
    拼韵 = 拼韵.replace('uan', 'r')
    拼韵 = 拼韵.replace('van', 'r')
    拼韵 = 拼韵.replace('ing', 'y')
    拼韵 = 拼韵.replace('uai', 'y')
    拼韵 = 拼韵.replace('ong', 's')
    拼韵 = 拼韵.replace('eng', 'g')
    拼韵 = 拼韵.replace('ang', 'h')
    拼韵 = 拼韵.replace('iao', 'c')
    拼韵 = 拼韵.replace('ian', 'm')
    拼韵 = 拼韵.replace('iu', 'q')
    拼韵 = 拼韵.replace('ia', 'w')
    拼韵 = 拼韵.replace('ua', 'w')
    拼韵 = 拼韵.replace('ue', 't')
    拼韵 = 拼韵.replace('ve', 't')
    拼韵 = 拼韵.replace('uo', 'o')
    拼韵 = 拼韵.replace('un', 'p')
    拼韵 = 拼韵.replace('en', 'f')
    拼韵 = 拼韵.replace('an', 'j')
    拼韵 = 拼韵.replace('ao', 'k')
    拼韵 = 拼韵.replace('ai', 'l')
    拼韵 = 拼韵.replace('ei', 'z')
    拼韵 = 拼韵.replace('ie', 'x')
    拼韵 = 拼韵.replace('ui', 'v')
    拼韵 = 拼韵.replace('ou', 'b')
    拼韵 = 拼韵.replace('in', 'n')
    拼韵 = 拼韵.replace('ng', 'g')
    if 声 == '':
        if len(韵) == 2:
            return 韵
        else:
            return 韵[0] + 拼韵
    return 声 + 拼韵

列表: list[tuple[str, int, float]] = []

with open('freq.txt') as f:
    text = f.read()
for 行 in findall(r'^([a-z]+)\t(\d+)$', text, flags=M):
    列表.append((拼运(行[0]), int(行[1]), 当量[拼运(行[0])]))

列表 = sorted(列表, key=lambda x: x[1] / 67028000 + x[2] / (-1.4))

with open('result.txt', 'w') as f:
    f.write('\n'.join('\t'.join([str(y) for y in x]) for x in 列表))
