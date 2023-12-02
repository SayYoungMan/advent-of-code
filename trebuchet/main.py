def first_digit(search_string: str):
    for ch in search_string:
        if ch.isnumeric():
            return ch


def last_digit(search_string: str):
    for ch in reversed(search_string):
        if ch.isnumeric():
            return ch


word_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_fixed_calibration_number(search_string: str):
    calibration_number_str = ["", ""]
    first_digit_index = float("inf")
    last_digit_index = -1

    for i, ch in enumerate(search_string):
        if ch.isnumeric():
            if i < first_digit_index:
                first_digit_index = i
                calibration_number_str[0] = ch
            if i > last_digit_index:
                last_digit_index = i
                calibration_number_str[1] = ch

    for word in word_dict.keys():
        found_index = search_string.find(word)
        if found_index != -1 and found_index < first_digit_index:
            first_digit_index = found_index
            calibration_number_str[0] = word

        back_found_index = search_string.rfind(word)
        if back_found_index != -1 and back_found_index > last_digit_index:
            last_digit_index = back_found_index
            calibration_number_str[1] = word

    calibration_number = convert_calibration_str_to_number(
        calibration_number_str[0]
    ) * 10 + convert_calibration_str_to_number(calibration_number_str[1])

    return calibration_number


def convert_calibration_str_to_number(calibration):
    if calibration.isnumeric():
        return int(calibration)

    return word_dict[calibration]


with open("trebuchet/input.txt", "r") as file:
    result = 0
    new_result = 0

    for line in file:
        calibration_number = first_digit(line) + last_digit(line)
        result += int(calibration_number)

        new_result += get_fixed_calibration_number(line)

    print(f"The calibration result for first part is: {result}")
    print(f"The calibration result for second part is: {new_result}")
