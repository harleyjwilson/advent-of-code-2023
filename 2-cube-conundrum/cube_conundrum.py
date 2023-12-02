def part_one(filename):
    file = open(filename, "r")
    sum = 0
    answer_dict = {"red": 12, "green": 13, "blue": 14}
    for line in file:
        game_no = int(line.split(":")[0].split(" ")[1])
        turn_list = line.split(":")[1].split(";")
        valid_game = True
        for turn in turn_list:
            colour_list = turn.split(",")
            for colour_parts in colour_list:
                num = int(colour_parts.strip().split(" ")[0])
                colour = colour_parts.strip().split(" ")[1]
                for key, value in answer_dict.items():
                    if colour == key and num > value:
                        valid_game = False
        if valid_game:
            sum += game_no

    return sum


def part_two(filename):
    file = open(filename, "r")
    sum = 0
    for line in file:
        tally_dict = {"red": 0, "green": 0, "blue": 0}
        for turn in line.split(":")[1].split(";"):
            turn_dict = {}
            for colour_parts in turn.split(","):
                num = int(colour_parts.strip().split(" ")[0])
                colour = colour_parts.strip().split(" ")[1]
                turn_dict[colour] = num
            for key, value in turn_dict.items():
                if turn_dict.get(key) and turn_dict[key] > tally_dict[key]:
                    tally_dict[key] = turn_dict[key]

        for key, value in tally_dict.items():
            if value == 0:
                tally_dict[key] = 1

        sum += tally_dict["red"] * tally_dict["green"] * tally_dict["blue"]

    return sum


if __name__ == "__main__":
    print("---------- Part One ----------")
    print("Answer: " + str(part_one("input.txt")))
    print("---------- Part Two ----------")
    print("Answer: " + str(part_two("input.txt")))
