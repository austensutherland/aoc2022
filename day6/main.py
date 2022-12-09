import pathlib

path = pathlib.Path(__file__).resolve().parent


def part_one():
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read()

    print(content)
    for index, item in enumerate(content):
        if index <= 3:
            continue

        items = content[(index - 4):index]
        if len(list(set(items))) == len(items):
            print(items)
            return index

print(part_one())


def part_two():
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read()

    print(content)
    for index, item in enumerate(content):
        if index <= 13:
            continue

        items = content[(index - 14):index]
        if len(list(set(items))) == len(items):
            print(items)
            return index


print(part_two())