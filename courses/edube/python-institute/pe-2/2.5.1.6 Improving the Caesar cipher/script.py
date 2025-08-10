
def translate(text: str, shifts: int):
    translated = ''
    for character in text:
        if character.islower():
            # Shift within 'a'..'z'
            offset = ord('a')
            translated += chr((ord(character) - offset + shifts) % 26 + offset)
        elif character.isupper():
            # Shift within 'A'..'Z'
            offset = ord('A')
            translated += chr((ord(character) - offset + shifts) % 26 + offset)
        else:
            # Leave non-letters unchanged
            translated += character
    return translated


text = input('Enter your message: ')
shifts = int(input('Enter the ASCII shifts (1-25): '))
if shifts < 1 or shifts > 25:
    raise ValueError('Shifts should be in the range between 1-25!')

print(translate(text, shifts))
