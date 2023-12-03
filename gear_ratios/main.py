engine_matrix = []


def is_symbol(x, y):
    item = engine_matrix[y][x]
    if item.isdecimal():
        return False
    elif item == ".":
        return False
    elif item == "\n":
        return False

    print(f"The following symbol detected: {item}")
    return True


def get_searchable_positions(x, y):
    to_search = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    to_include = []

    for i, (_x, _y) in enumerate(to_search):
        if (
            _x >= 0
            and _y >= 0
            and _x < len(engine_matrix[0])
            and _y < len(engine_matrix)
        ):
            to_include.append(i)

    return [to_search[i] for i in to_include]


def is_part_number(to_search):
    for _x, _y in to_search:
        if is_symbol(_x, _y):
            return True

    return False


with open("gear_ratios/input.txt", "r") as file:
    for line in file:
        engine_matrix.append([x for x in line])

result = 0
for y, row in enumerate(engine_matrix):
    number_string = ""
    to_search = []
    for x, item in enumerate(row):
        if item.isdecimal():
            number_string += item
            to_search.extend(get_searchable_positions(x, y))
        elif number_string != "":
            if is_part_number(to_search):
                print(f"This is part number: {number_string}")
                result += int(number_string)
            else:
                print(f"This is not a part number: {number_string}")
            number_string = ""
            to_search = []

print(f"The sum of all of the part numbers in the engine schematic is: {result}")
