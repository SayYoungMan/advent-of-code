def first_digit(search_string: str):
    for ch in search_string:
        if ch.isnumeric():
            return ch


def last_digit(search_string: str):
    for ch in reversed(search_string):
        if ch.isnumeric():
            return ch

with open("trebuchet/input.txt", "r") as file:
    result = 0

    for line in file:
        calibration_number = first_digit(line) + last_digit(line)
        result += int(calibration_number)

    print(f"The calibration result for first part is: {result}")
