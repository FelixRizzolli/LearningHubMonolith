def is_palindrome(text: str):
    text_list: list[str] = list(text)
    text_list.reverse()
    reversed_text: str = ''.join(text_list)
    return text.lower().replace(' ', '') == reversed_text.lower().replace(' ', '')


text = input('Enter your text: ')
if is_palindrome(text):
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
