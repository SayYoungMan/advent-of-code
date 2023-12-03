MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_game_possible(game: str):
    tries = game.split(",")
    for t in tries:
        [amount, color] = t.strip().split(" ")
        if int(amount) > MAX_CUBES[color]:
            return False

    return True


def get_game_power(games: list[str]):
    maximum_dict = {
        "red": -1,
        "green": -1,
        "blue": -1,
    }

    for game in games:
        tries = game.split(",")
        for t in tries:
            [amount, color] = t.strip().split(" ")
            maximum_dict[color] = max(maximum_dict[color], int(amount))

    return maximum_dict["red"] * maximum_dict["green"] * maximum_dict["blue"]


with open("cube_conundrum/input.txt", "r") as file:
    result = 0
    power_sum = 0
    for i, line in enumerate(file):
        game_no = i + 1

        game_info = line.split(":")[1].strip()
        games = game_info.split(";")

        power_sum += get_game_power(games)

        possible = True
        for game in games:
            if not is_game_possible(game):
                possible = False
                break

        if possible:
            result += game_no

    print(f"The sum of all possible game numbers are: {result}")
    print(f"The sum of all the powers are: {power_sum}")
