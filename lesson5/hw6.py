import re

def translated():

    global new

    translated = input("Введите текст для перевода: ")
    map = {ord('a'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ё'): 'io',
    ord('ж'): 'j', ord('з'): 'z', ord('и'): 'i', ord('й'): 'ji', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
    ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u',
    ord('ф'): 'f', ord('х'): 'h', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'sh', ord('ъ'): '_', ord('ы'): 'y',
        ord('ь'): '_', ord('э'): 'e', ord('ю'): 'ju', ord('я'): 'ja'}
    res = []
   

    for char in translated:

        if char == char.upper():
            new = char.lower()
            new = new.translate(map).upper()

        elif char == char.lower():
            new = char.translate(map)
        res.append(new)
    res = re.sub(r'(\W)', '_', ''.join(res))
 

    return res
