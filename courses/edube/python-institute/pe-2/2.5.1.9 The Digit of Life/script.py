
def sum_digits(digits: int) -> int:
    number: int = 0
    for digit in str(digits):
        number += int(digit)
    return number


age = input('Enter your age (YYYYMMDD): ')

digit_of_life: int = int(age)
while digit_of_life >= 10:
    digit_of_life = sum_digits(digit_of_life)

print(digit_of_life)
