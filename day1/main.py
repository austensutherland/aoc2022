import pathlib

path = pathlib.Path(__file__).resolve().parent


def part_one():
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read().replace("\n", ",").split(",,")
        elf_total_cals = [sum([int(i) for i in item.split(",")]) for item in content]

    return max(elf_total_cals)


def part_two():
    elf_total_cals = []
    with open(f"{path}/input.txt", "r") as infile:
        content = infile.read().replace("\n", ",").split(",,")
        elf_total_cals = [sum([int(i) for i in item.split(",")]) for item in content]

    elf_total_cals.sort(reverse=True)
    return sum(elf_total_cals[:3])


print(part_one())
print(part_two())
