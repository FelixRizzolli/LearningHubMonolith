
def finder(search: str, text: str) -> bool:
    position = 0
    for char in search:
        result = text.find(char, position)
        if result == -1:
            return False
        else:
            position = result + 1
    return True


def find(search: str, text: str) -> None:
    result = finder(search.lower(), text.lower())
    if result:
        print('Yes')
    else:
        print('No')


find('donor', 'Nabucodonosor')
find('donut', 'Nabucodonosor')
