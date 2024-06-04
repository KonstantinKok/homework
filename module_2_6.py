def single_root_words(root_word, *other_words):
    words = []
    for i in other_words:
        i = i.lower()
        root_word = root_word.lower()
        if root_word in i or i in root_word:
            words.append(i)
    return words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
