def is_happy(n: int) -> bool:
    """
    Checks whether a given number is happy or not.

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits in base-ten, and repeat the process
    until the number either equals 1 (where it will stay), or it loops
    endlessly in a cycle that does not include 1. Those numbers for
    which this process ends in 1 are happy numbers.

    Args:
        n: The number to check (must be a positive integer)

    Returns:
        True if the number is a happy number, False otherwise

    Examples:
        >>> is_happy(19)
        True
        >>> is_happy(2)
        False
        >>> is_happy(1)
        True
    """
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1