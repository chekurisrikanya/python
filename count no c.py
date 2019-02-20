def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 3
        else:
            dict[n] = 2
    return dict
print(char_frequency('google.com'))
