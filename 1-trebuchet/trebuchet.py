def part_one(filename):
    file = open(filename, "r")
    sum = 0
    for line in file:
        line_tuple = [int(x) for x in list(line) if x.isdigit()]
        if not len(line_tuple) == 0:
            sum += int(str(line_tuple[0]) + str(line_tuple[len(line_tuple) - 1]))

    return sum


def part_two(filename):
    file = open(filename, "r")
    sum = 0
    number_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for line in file:
        for word, number in number_dict.items():
            line = line.replace(word, number)
        line_tuple = [int(x) for x in list(line) if x.isdigit()]
        if not len(line_tuple) == 0:
            sum += int(str(line_tuple[0]) + str(line_tuple[len(line_tuple) - 1]))

    return sum


if __name__ == "__main__":
    print("---------- Part One ----------")
    print("Answer: " + str(part_one("input.txt")))
    print("---------- Part Two ----------")
    print("Answer: " + str(part_two("input.txt")))
