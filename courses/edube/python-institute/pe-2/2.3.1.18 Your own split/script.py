
def mysplit(my_string: str):
    words = []

    word: str = ''
    for character in my_string:
        if character == ' ':
            words.append(word)
            word = ''
        else:
            word += character
    words.append(word)
    
    return words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(""))
print(mysplit("abc"))
print(mysplit(""))