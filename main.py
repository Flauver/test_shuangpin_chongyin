from re import *
from dataclasses import dataclass

@dataclass
class 拼运:
    type: str
    fr: str
    to: str

    def apply(self, inputs: list[str]) -> list[str]:
        results: list[str] = []
        for 音节 in inputs:
            match self.type:
                case 'xform':
                    results.append(sub(self.fr, self.to, 音节))
                case 'derive':
                    results.append(音节)
                    results.append(sub(self.fr, self.to, 音节))
        
        return results


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

def 应用拼运(text: str) -> list[str]:
    声, 韵  = 分割(text)
    声 = 声.replace('zh', 'v')
    声 = 声.replace('ch', 'i')
    声 = 声.replace('sh', 'u')
    拼韵: list[str] = 拼运(type='xform', fr='iong', to='s').apply([韵])
    拼韵  = 拼运(type='xform', fr='iang', to='d').apply(拼韵)
    拼韵: list[str] = 拼运(type='xform', fr='iang', to='d').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='uang', to='d').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='uan', to='r').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='van', to='r').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ing', to='y').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='uai', to='y').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ong', to='s').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='eng', to='g').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ang', to='h').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='iao', to='c').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ian', to='m').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='iu', to='q').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ia', to='w').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ua', to='w').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ue', to='t').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ve', to='t').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='uo', to='o').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='un', to='p').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='en', to='f').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='an', to='j').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ao', to='k').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ai', to='l').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ei', to='z').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ie', to='x').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ui', to='v').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ou', to='b').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='in', to='n').apply(拼韵)
    拼韵 = 拼运(type='xform', fr='ng', to='g').apply(拼韵)
    拼韵 = 拼运(type='derive', fr='i', to='d').apply(拼韵)
    if 声 == '':
        if len(韵) == 2:
            return [韵]
        else:
            return [韵[0] + x for x in 拼韵]
    return [声 + x for x in 拼韵]

列表: list[tuple[str, int, float]] = []

with open('freq.txt') as f:
    text = f.read()
for 行 in findall(r'^([a-z]+)\t(\d+)$', text, flags=M):
    行: tuple[str, str]
    (行)
    结果 = [(x, int(行[1]), 当量[x]) for x in 应用拼运(行[0])]
    print(行, 结果)
    m = min([x[2] for x in 结果])
    列表.append(next((x for x in 结果 if x[2] == m)))

列表 = sorted(列表, key=lambda x: x[1] / 67028000 + x[2] / (-1.4))

with open('result.txt', 'w') as f:
    f.write('\n'.join('\t'.join([str(y) for y in x]) for x in 列表))
