# def roll_the_dice(dice: str):
#     """
#     non bonus version.
#     """
#     from random import randint
#     amount, size = dice.split("d")
#     result = 0

#     for i in range(1, int(amount) + 1):
#         result += randint(1, int(size))

#     return result

def roll_the_dice(dice: str):
    """
    bonus version.
    """
    from random import randint
    amount, size = dice.split("d")
    results = []

    print
    for i in range(1, int(amount) + 1):
        results.append(randint(1, int(size)))

    result = str(sum(results)) + ":"
    for each in results:
        result += " "
        result += str(each)

    return result

if __name__ == "__main__":
    for example in ('3d6', '4d12', '1d10', '5d4'):
        print(example, roll_the_dice(example))
