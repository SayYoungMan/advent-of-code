winning_numbers = []
have_numbers = []


def take_out_card_info(line: str):
    return line.split(":")[1].strip()


def separate_winning_have(info: str):
    splitted = info.split("|")
    return (splitted[0].strip(), splitted[1].strip())


def process_as_number_list(part: str):
    return [int(x) for x in part.split(" ") if x != ""]


def process_data(line: str):
    info_part = take_out_card_info(line)
    winning_part, have_part = separate_winning_have(info_part)

    winning_numbers.append(set(process_as_number_list(winning_part)))
    have_numbers.append(process_as_number_list(have_part))


with open("04_scratchcards/input.txt", "r") as file:
    for line in file:
        process_data(line)

won_count_list = []
result = 0
for i, numbers in enumerate(have_numbers):
    won_count = 0
    for n in numbers:
        if n in winning_numbers[i]:
            won_count += 1

    if won_count != 0:
        result += 2 ** (won_count - 1)

    won_count_list.append(won_count)

print(f"The sum of points for all scratchcards are {result}")

games_playcount = len(winning_numbers)

result = [1] * games_playcount

for i in range(games_playcount):
    won = won_count_list[i]
    if won <= 0:
        continue

    for j in range(i + 1, min(i + won + 1, games_playcount)):
        result[j] += result[i]

print(f"The sum of total scratchcards are {sum(result)}")
