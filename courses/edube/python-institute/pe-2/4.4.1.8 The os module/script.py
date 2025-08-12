import os
import shutil


def create_test_env():
    if os.path.isdir("tree"):
        shutil.rmtree("tree")
    os.mkdir("tree")
    os.mkdir("tree/c")
    os.mkdir("tree/c/other_courses")
    os.mkdir("tree/c/other_courses/cpp")
    os.mkdir("tree/c/other_courses/python")
    os.mkdir("tree/cpp")
    os.mkdir("tree/cpp/other_courses")
    os.mkdir("tree/cpp/other_courses/c")
    os.mkdir("tree/cpp/other_courses/python")
    os.mkdir("tree/python")
    os.mkdir("tree/python/other_courses")
    os.mkdir("tree/python/other_courses/c")
    os.mkdir("tree/python/other_courses/cpp")


def find(path: str, dir: str):
    for d in os.listdir(path):
        new_path = os.path.join(path, d)
        if os.path.isdir(new_path):
            if d == dir:
                print(new_path)
            find(new_path, dir)


create_test_env()
find(path="./tree", dir="python")
