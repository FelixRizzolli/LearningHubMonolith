class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line):
        super().__init__(f"Bad line: {line.strip()}")


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__("File is empty.")


def create_test_file(filename="test.txt", content=None):
    if content is None:
        content = "John\tSmith\t5\nAnna\tBoleyn\t4.5\nJohn\tSmith\t2\nAnna\tBoleyn\t11\nAndrew\tCox\t1.5\n"
    with open(filename, "w") as f:
        f.write(content)


def main():
    create_test_file()

    filename = input("Enter Prof. Jekyll's file name: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines or all(line.strip() == '' for line in lines):
                raise FileEmpty()
            students = {}
            for line in lines:
                if line.strip() == '':
                    continue
                parts = line.strip().split()
                if len(parts) != 3:
                    raise BadLine(line)
                first, last, points = parts
                try:
                    points = float(points)
                except ValueError:
                    raise BadLine(line)
                key = f"{first} {last}"
                students[key] = students.get(key, 0) + points
            for student in sorted(students):
                print(f"{student} \t {students[student]}")
    except FileEmpty as fe:
        print(fe)
    except BadLine as bl:
        print(bl)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
