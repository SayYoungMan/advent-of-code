from math import sqrt


def convert_str_list_to_int_list(lis: list[str]):
    return [int(x) for x in lis]


with open("06_wait/input.txt", "r") as file:
    lines = list(file)
    time, distance = map(lambda x: x.split(":")[1].split(), lines)
    time = convert_str_list_to_int_list(time)
    distance = convert_str_list_to_int_list(distance)

# Assume t seconds to speed up,
# total n ms given for race,
# and b mm is the best score

# Then, it can travel for (n - t) ms
# with speed of t m/s
# Therefore, it can travel t(n - t) mm in total.

# To find the t at current best distance,
# we have to solve t(n - t) = b
# => t^2 - nt + b = 0
# => t = (n ± sqrt(n^2 - 4b)) / 2 will give you two ways.
# Therefore, all integers in between two roots will be the possible ways.


def get_solutions(n, b):
    sqrt_part = sqrt(n**2 - 4 * b)
    max_wait = (n + sqrt_part) / 2
    min_wait = (n - sqrt_part) / 2

    if (max_wait == int(max_wait)) and min_wait == int(min_wait):
        max_wait -= 1

    return round(max_wait - min_wait)


result = 1
for n, b in zip(time, distance):
    result *= get_solutions(n, b)

print(f"Number of possible ways all multiplied together is: {result}")
