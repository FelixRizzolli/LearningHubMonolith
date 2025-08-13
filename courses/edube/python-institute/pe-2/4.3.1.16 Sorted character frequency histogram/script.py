
def create_test_file(filename="test.txt", content="cBabAa\n"):
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
    # Sort by frequency descending, then alphabetically
    sorted_hist = sorted(letter_counts.items(),
                         key=lambda item: (-item[1], item[0]))
    out_filename = filename + ".hist"
    with open(out_filename, 'w') as out:
        for letter, count in sorted_hist:
            line = f"{letter} -> {count}"
            print(line)
            out.write(line + "\n")
except FileNotFoundError:
    print("File not found")
