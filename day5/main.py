import pathlib
import re
from copy import copy
from curses.ascii import isupper
from pprint import pprint

path = pathlib.Path(__file__).resolve().parent


def parse_input():
    moves = []
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read()
        move_list = copy(content)
        stacks = copy(content)

    # Collect moves, replace in stacks copy
    move_reg = "move(\d*)from(\d*)to(\d*)"
    for line in move_list.split("\n"):
        if "move" not in line:
            continue
        stacks = stacks.replace(line, "")
        move = re.search(move_reg, line.replace(" ", "")).groups()
        moves.append({"count": int(move[0]), "from": int(move[1]), "to": int(move[2])})

    # Collect stacks (remove all empty new lines)
    stacks = re.sub(r"^$\n", "", stacks, flags=re.MULTILINE)

    # First collect non string columns to determine position of other items
    column_index_stack_map = {}
    for item in stacks.split("\n"):
        for index, content in enumerate(item):
            try:
                stack = int(content)
                column_index_stack_map[index] = stack
            except ValueError:
                continue

    # Iterate back through items and collect alphanums into their stacks.
    stacks_dict = {value: [] for _, value in column_index_stack_map.items()}
    for item in stacks.split("\n"):
        for index, content in enumerate(item):
            if content.isupper():
                index = column_index_stack_map.get(index)
                stacks_dict[index].append(content)

    return stacks_dict, moves


def part_one(stacks_dict, moves):
    for move in moves:
        items_to_remove = stacks_dict[move["from"]][:move["count"]]
        stacks_dict[move["from"]] = stacks_dict[move["from"]][move["count"]:]
        items_to_remove.reverse()
        stacks_dict[move["to"]] = [*items_to_remove, *stacks_dict[move["to"]]]

    word = ""
    for i in range(1, 10):
        word = f"{word}{stacks_dict[i][0]}"

    return word

def part_two(stacks_dict, moves):
    for move in moves:
        items_to_remove = stacks_dict[move["from"]][:move["count"]]
        stacks_dict[move["from"]] = stacks_dict[move["from"]][move["count"]:]
        stacks_dict[move["to"]] = [*items_to_remove, *stacks_dict[move["to"]]]

    word = ""
    for i in range(1, 10):
        word = f"{word}{stacks_dict[i][0]}"

    return word

stacks, moves = parse_input()
print(part_one(stacks, moves))

stacks, moves = parse_input()
print(part_two(stacks, moves))