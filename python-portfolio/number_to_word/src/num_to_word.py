from constants import ABOVE_100, TENS, UNDER_20


def num_to_word(num):
    """This function converts an integer to words.

    Args:
        num (int): The number to be converted to words.

    Returns:
        str: 
    """

    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        return TENS[num//10 - 2] + ("" if remainder == 0 else " " + UNDER_20[remainder])
    # For numbers 100 and above, calculate words recursively.
    pivot = max([key for key in ABOVE_100 if key <= num])

    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    if num % pivot == 0:
        return f'{p1} {p2}'

    return f'{p1} {p2} {num_to_word(num % pivot)}'


if __name__ == "__main__":
    # Get number from user.
    num = int(input("Enter a Number: "))
    # Check if number is in acceptable range.
    if num >= 0 and num <= 999_999_999_999:
        # Print number in words.
        print(num_to_word(num))
    else:
        print("Number out of range")