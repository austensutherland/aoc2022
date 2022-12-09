import pathlib
import string

path =  pathlib.Path(__file__).resolve().parent

def part_one():
    ruckked = 0
    with open(f"{path}/input.txt", "r") as infile:
        packs = infile.read().split("\n")

    overlapping_items = []
    for pack in packs:
        one, two = pack[int(len(pack)/2):], pack[:int(len(pack)/2)]
        overlapping_items += list(set([i for i in one if i in two]))

    for overlap in overlapping_items:
        if overlap.isupper():
            result = (string.ascii_uppercase.index(overlap) + 1) + 26
        else:
            result = (string.ascii_lowercase.index(overlap) + 1)

        ruckked += result

    return ruckked

print(part_one())

def part_two():
    ruckked = 0
    with open(f"{path}/input.txt", "r") as infile:
        packs = infile.read().split("\n")

    previous_range = 0
    characters = []
    for i in range(3, len(packs) + 3, 3):
        pack_set = packs[previous_range:i]
        char = [i for i in pack_set[0] if i in pack_set[1] and i in pack_set[2]]
        characters += list(set(char))
        previous_range = i

    for overlap in characters:
        if overlap.isupper():
            result = (string.ascii_uppercase.index(overlap) + 1) + 26
        else:
            result = (string.ascii_lowercase.index(overlap) + 1)

        ruckked += result

    return ruckked

print(part_two())
