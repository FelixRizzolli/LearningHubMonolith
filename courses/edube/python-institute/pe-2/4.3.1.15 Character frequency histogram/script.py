

def create_test_file(filename="test.txt", content="aBc\n"):
    with open(filename, "w") as f:
        f.write(content)


create_test_file()


filename = input()
letter_counts = {}
try:
    with open(filename, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha() and char.lower() >= 'a' and char.lower() <= 'z':
                    ch = char.lower()
                    letter_counts[ch] = letter_counts.get(ch, 0) + 1
    for letter in sorted(letter_counts.keys()):
        print(f"{letter} -> {letter_counts[letter]}")
except FileNotFoundError:
    print("File not found")
