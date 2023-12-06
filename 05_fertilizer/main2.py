def get_seeds(line: str):
    seed_nums = line.split(":")[1].strip()
    seed_nums = [int(x) for x in seed_nums.split(" ")]

    res = []
    for start, length in zip(*[iter(seed_nums)] * 2):
        res.append((start, start + length))

    return res


with open("05_fertilizer/input.txt", "r") as file:
    current_map_idx = 0
    guide_map = {}
    mapping_list = []
    started_writing = False
    for i, line in enumerate(file):
        if i == 0:
            seed_range = get_seeds(line)
            continue
        if line == "\n" and started_writing:
            mapping_list = sorted(mapping_list, key=lambda d: d["from"])
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


def new_seed_ranges_from_map(ran: tuple, m: dict):
    start, end = ran

    # If the range does not overlap with m, ignore
    if end < m["from"] or start >= m["to"]:
        return [], [ran]
    # If whole range is inside m, process all
    if start >= m["from"] and end <= m["to"]:
        processed = (start + m["diff"], end + m["diff"])
        return [processed], []
    # If starts before m but ends inside m, divide to two
    if start < m["from"] and end <= m["to"]:
        processed = (m["from"] + m["diff"], end + m["diff"])
        remaining = (start, m["from"])
        return [processed], [remaining]
    # If starts inside m and ends outside, divide to two
    if start >= m["from"] and end > m["to"]:
        processed = (start + m["diff"], m["to"] + m["diff"])
        remaining = (m["to"], end)
        return [processed], [remaining]
    # If starts before m and ends after m, divide to three
    if start < m["from"] and end > m["to"]:
        processed = (m["from"] + m["diff"], m["to"] + m["diff"])
        remaining_left = (start, m["from"])
        remaining_right = (m["to"], end)
        return [processed], [remaining_left, remaining_right]
    else:
        print("THIS SHOULD NOT HAPPEN")


for maps in guide_map.values():
    processed_ranges = []
    remaining_ranges = []
    for m in maps:
        for ran in seed_range:
            p, r = new_seed_ranges_from_map(ran, m)
            processed_ranges.extend(p)
            remaining_ranges.extend(r)

        seed_range = remaining_ranges
        remaining_ranges = []

    processed_ranges.extend(seed_range)
    seed_range = processed_ranges

lowest_location_number = min(seed_range, key=lambda x: x[0])[0]
print(f"The lowest location number is: {lowest_location_number}")
