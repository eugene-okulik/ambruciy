text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \n'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text = text.split()
new_text2 = []
for word in text:
    if ',' in word:
        new_word = word.replace(',', 'ing,')
        new_text2.append(new_word)
    elif '.' in word:
        new_word = word.replace('.', 'ing.')
        new_text2.append(new_word)
    else:
        word += 'ing'
        new_text2.append(word)
print(f'{" ".join(new_text2)}')
