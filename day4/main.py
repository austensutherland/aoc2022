import pathlib

path = pathlib.Path(__file__).resolve().parent


def part_one():
    with open(f"{path}/input.txt", "r") as infile:
        pairs = [p.split(",") for p in infile.read().split("\n")]
        pairs = [(sublist[0].split("-"), sublist[1].split("-")) for sublist in pairs]

    overlapping_items = 0
    for first_pair, second_pair in pairs:
        min_first_id = min([int(first_pair[0]), int(second_pair[0])])
        max_second_id = max([int(first_pair[1]), int(second_pair[1])])
        if any(
            item == [str(min_first_id), str(max_second_id)]
            for item in [first_pair, second_pair]
        ):
            overlapping_items += 1

    return overlapping_items


print(part_one())


def part_two():
    with open(f"{path}/input.txt", "r") as infile:
        pairs = [p.split(",") for p in infile.read().split("\n")]
        pairs = [(sublist[0].split("-"), sublist[1].split("-")) for sublist in pairs]

    overlapping_items = 0
    for first_pair, second_pair in pairs:
        first_pair = [
            int(first_pair[0]) + i
            for i in range((int(first_pair[1]) - int(first_pair[0])) + 1)
        ]
        second_pair = [
            int(second_pair[0]) + i
            for i in range((int(second_pair[1]) - int(second_pair[0])) + 1)
        ]
        if any(p in second_pair for p in first_pair):
            overlapping_items += 1

    return overlapping_items


print(part_two())
