from functools import cmp_to_key

hand_bids: list[tuple[str, int]] = []
card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
type_order = ["five", "four", "full", "three", "two", "one", "high"]


def make_hand_dict(hand):
    res = {}
    for card in hand:
        if card not in res:
            res[card] = 1
        else:
            res[card] += 1
    return res


def is_higher_card(main, sub):
    if main == sub:
        raise Exception("Can't compare same cards", main, sub)
    for c in card_order:
        if main == c:
            return True
        elif sub == c:
            return False
    raise Exception("Card did not match any from the lists", main, sub)


def get_hand_type(hand_dict: dict):
    vals = hand_dict.values()
    max_dups = max(vals)
    if max_dups == 5:
        return "five"
    elif max_dups == 4:
        return "four"
    elif max_dups == 3:
        if 2 in vals:
            return "full"
        else:
            return "three"
    elif max_dups == 2:
        if len(vals) == 3:
            return "two"
        else:
            return "one"
    else:
        return "high"


def is_greater_hand(hand1: str, hand2: str):
    hand_dict1 = make_hand_dict(hand1)
    hand_dict2 = make_hand_dict(hand2)

    hand_type1 = get_hand_type(hand_dict1)
    hand_type2 = get_hand_type(hand_dict2)

    if hand_type1 != hand_type2:
        for t in type_order:
            if hand_type1 == t:
                return True
            elif hand_type2 == t:
                return False
        raise Exception("hands did not match any type", hand_type1, hand_type2)

    for a, b in zip(hand1, hand2):
        if a == b:
            continue
        if is_higher_card(a, b):
            return True
        return False


def hand_comparator(a: tuple[str, int], b: tuple[str, int]):
    hand1 = a[0]
    hand2 = b[0]

    if hand1 == hand2:
        return 0
    elif is_greater_hand(hand1, hand2):
        return 1
    else:
        return -1


with open("07_camel_card/input.txt", "r") as file:
    for line in file:
        hand, bid = line.split()

        hand_bids.append((hand, int(bid)))

hand_bids.sort(key=cmp_to_key(hand_comparator))

winning = 0
for i, (_, bid) in enumerate(hand_bids):
    winning += (i + 1) * bid

print(f"The total winnings are {winning}")
