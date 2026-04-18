import re


韵: list[str] = [
    'iu',
    'ia',
    'ua',
    'e',
    'uan',
    'van',
    'ue',
    've',
    'ing',
    'uai',
    'u',
    'i',
    'o',
    'uo',
    'un',

    'a',
    'ong',
    'iong',
    'iang',
    'uang',
    'en',
    'eng',
    'ang',
    'an',
    'ao',
    'ai',

    'ei',
    'ie',
    'iao',
    'ui',
    'v',
    'ou',
    'in',
    'ian',

    'ng',
]

print('\n'.join(sorted(韵, key=lambda x: len(x), reverse=True)))
