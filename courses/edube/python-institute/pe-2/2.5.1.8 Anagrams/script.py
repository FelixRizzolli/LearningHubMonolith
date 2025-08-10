
def get_statistics(text: str) -> dict[str, int]:
    statistics: dict = {}
    for character in text:
        if statistics.get(character):
            statistics[character] += 1
        else:
            statistics[character] = 1
    return statistics


def is_anagram(text_a: str, text_b: str) -> bool:
    formated_text_a = text_a.replace(' ', '').lower()
    formated_text_b = text_a.replace(' ', '').lower()

    if formated_text_a == '' or formated_text_b == '':
        return False

    statistics_text_a = get_statistics(formated_text_a)
    statistics_text_b = get_statistics(formated_text_b)

    if statistics_text_a.__len__() != statistics_text_b.__len__():
        return False

    for character in statistics_text_a.keys():
        if statistics_text_a[character] != statistics_text_b[character]:
            return False

    return True


text_1 = input('Enter your text 1: ')
text_2 = input('Enter your text 2: ')

if is_anagram(text_1, text_2):
    print('Anagrams')
else:
    print('Not anagrams')
