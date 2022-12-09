import pathlib

path =  pathlib.Path(__file__).resolve().parent

convert_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def part_one():
    results = [[], [], []] # draw / loss / win
    with open(f"{path}/input.txt", "r") as infile:
        plays = [i.split(' ') for i in infile.read().split("\n")]
        for play in plays:
            result = convert_map.get(play[0]) - convert_map.get(play[1])
            results[result].append(convert_map.get(play[1]))

    moves_total = sum([play for plays in results for play in plays])
    draws = 3 * len(results[0])
    wins = 6 * len(results[2])

    return moves_total + draws + wins

print(part_one())

result_map = {
    "Y": [0],
    "X": [1, -2],
    "Z": [2, -1]
}

def part_two():
    results = [[], [], []] # draw / loss / win
    with open(f"{path}/input.txt", "r") as infile:
        plays = [i.split(' ') for i in infile.read().split("\n")]
        for play in plays:
            their_play = convert_map.get(play[0])
            result_range = result_map.get(play[1])
            for i in [1, 2, 3]:
                if their_play - i in result_range:
                    results[their_play - i].append(i)


    moves_total = sum([play for plays in results for play in plays])
    draws = 3 * len(results[0])
    wins = 6 * len(results[2])

    return moves_total + draws + wins

print(part_two())