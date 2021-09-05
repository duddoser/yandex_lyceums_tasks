d = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
     "б": "b", "ю": "ju", "ё": "jo"}
with open('cyrillic.txt') as file, open('transliteration.txt', 'w') as new_file:
    for i in file.read():
        if i.lower() in d:
            if i.isupper():
                new_file.write(d[i.lower()].capitalize())
            else:
                new_file.write(d[i.lower()])
        else:
            new_file.write(i)
