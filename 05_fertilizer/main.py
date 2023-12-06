def get_seeds(line: str):
    seed_nums = line.split(":")[1].strip()
    return [int(x) for x in seed_nums.split(" ")]


with open("05_fertilizer/input.txt", "r") as file:
    current_map_idx = 0
    guide_map = {}
    mapping_list = []
    started_writing = False
    for i, line in enumerate(file):
        if i == 0:
            seed_nums = get_seeds(line)
            continue
        if line == "\n" and started_writing:
            guide_map[current_map_idx] = mapping_list
            mapping_list = []
            current_map_idx += 1
            continue

        if line == "\n" or line[0].isalpha():
            continue

        started_writing = True
        dest, source, length = [int(x) for x in line.strip().split(" ")]
        mapping_list.append(
            {
                "from": source,
                "to": source + length,
                "diff": dest - source,
            }
        )

# print(guide_map)


def next_dest(source: int, maps: list[dict]):
    for m in maps:
        if source >= m["from"] and source < m["to"]:
            return source + m["diff"]

    return source


for stage, maps in guide_map.items():
    # print(seed_nums)
    seed_nums = [next_dest(seed, maps) for seed in seed_nums]

# print(seed_nums)
print(f"The lowest location number is {min(seed_nums)}")
