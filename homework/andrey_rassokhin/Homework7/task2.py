def output_text(dict):
    for key, value in dict.items():
        key *= value
        print(key)


output_text({'I': 3, 'love': 5, 'Python': 1, '!': 50})
