import pathlib
import re
from pprint import pprint
from typing import OrderedDict

path = pathlib.Path(__file__).resolve().parent


def build_file_tree(content):
    dir_tree = {"/": 0}
    current_path = ""
    for item in content:
        cd = "^\$\ cd (.+)"
        ls = "^\$\ ls"

        # If item is a cd, throw it into the dir tree
        if re.search(cd, item):
            dir = re.search(cd, item).groups()[0].replace("dir ", "")
            if dir == '/':
                current_path = ""
            elif dir == "..":
                current_path = "/".join(current_path.split("/")[:-1])
            else:
                current_path = f"{current_path}/{dir}"
                dir_tree[current_path] = 0

        # If item is not cd (and it not ls) put its content within the proper dir
        # We dont have to care about dirs that we never cd into because we dont know their content
        elif not re.search(ls, item) and "dir" not in item:
            file_size = re.search("^(\d*)", item).groups()[0]
            path = current_path or "/"
            dir_tree[path] += int(file_size)

        else:
            continue

    return dir_tree


def part_one():
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read().split("\n")

    file_tree = build_file_tree(content)
    sorted_tree = OrderedDict(sorted(file_tree.items(), key=lambda item: len(item[0]), reverse=True))
    summed_direct = 0
    for key, value in sorted_tree.items():
        if value <= 100000:
            summed_direct += value

        parent_key = "/".join(key.split("/")[:-1])
        if len(key.split("/")) == 2 and key != "/":
            parent_key = "/"
        if parent_key:
            sorted_tree[parent_key] += value
    print(summed_direct)
    return sorted_tree

part_one()


def part_two():
    sorted_tree = part_one()
    root_dir_size = sorted_tree.get("/")
    required_deletion = 30000000 - (70000000 - root_dir_size)

    print("required_deletion", required_deletion)
    min_size = root_dir_size
    for key, value in sorted_tree.items():
        if value > required_deletion and value < min_size:
                min_size = value
                print(value)

    print("min_size", min_size)

part_two()