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


def coord_to_number_dict():
    number_dict = {}
    for y, row in enumerate(engine_matrix):
        number_string = ""
        coords = []
        for x, item in enumerate(row):
            if item.isdecimal():
                number_string += item
                coords.append((x, y))
            elif number_string != "":
                for _x, _y in coords:
                    number_dict[(_x, _y)] = int(number_string)
                number_string = ""
                coords = []

    return number_dict


def get_nums_from_row(x, y, number_dict):
    nums = []
    row_len = len(engine_matrix[0])
    left_point = (x - 1, y)
    middle_point = (x, y)
    right_point = (x + 1, y)

    if x > 0 and left_point in number_dict:
        nums.append(number_dict[left_point])
        if middle_point not in number_dict and right_point in number_dict:
            nums.append(number_dict[right_point])
        return nums
    if middle_point in number_dict:
        nums.append(number_dict[middle_point])
        return nums
    if x < (row_len - 1) and right_point in number_dict:
        nums.append(number_dict[right_point])
        return nums

    return nums


def get_multiple_if_gear(x, y, number_dict):
    nums = []
    row_len = len(engine_matrix[0])
    col_len = len(engine_matrix)
    left_point = (x - 1, y)
    right_point = (x + 1, y)

    if y > 0:
        nums.extend(get_nums_from_row(x, y - 1, number_dict))
    if x > 0 and left_point in number_dict:
        nums.append(number_dict[left_point])
    if x < (row_len - 1) and right_point in number_dict:
        nums.append(number_dict[right_point])
    if y < (col_len - 1):
        nums.extend(get_nums_from_row(x, y + 1, number_dict))

    print(f"Nums for * at ({x}, {y}) is: {nums}")
    if len(nums) == 2:
        return nums[0] * nums[1]

    return 0


def get_gear_ratio_sum():
    result = 0
    for y, row in enumerate(engine_matrix):
        for x, item in enumerate(row):
            if item == "*":
                result += get_multiple_if_gear(x, y, number_dict)

    return result


with open("03_gear_ratios/input.txt", "r") as file:
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

number_dict = coord_to_number_dict()
gear_ratio_sum = get_gear_ratio_sum()

print(f"The sum of gear ratios is: {gear_ratio_sum}")
