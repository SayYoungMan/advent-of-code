from math import sqrt


with open("06_wait/input.txt", "r") as file:
    lines = list(file)
    time, distance = map(lambda x: int(x.split(":")[1].strip().replace(" ", "")), lines)

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


result = get_solutions(time, distance)

print(f"Number the all the possible ways is: {result}")
