import string
import random
import nltk

vocabs = nltk.corpus.words.words()

def pin_generator(length: int) -> str:
    """
    Generates a random pin code of a given length.
    Args:
        length (int): The length of the pin code to generate.
    Returns:
        str: A random pin code of the given length.
    """
    return ''.join(random.choices(string.digits, k = length))

def random_password_generator(length: int, include_numbers: bool = False, include_symbols: bool = False) -> str:
    """generates a random password of a given length.

        Args:
            length (int): _description_
            include_numbers (bool, optional): Adds numbers to the password. Defaults to False.
            include_symbols (bool, optional): Adds symbols to the password. Defaults to False.

        Returns:
            str: A random password of a given length.
        """
        
    characters: str = string.ascii_letters
    # add numbers to the characters
    if include_numbers:
        characters += string.digits
    # add symbols to the characters
    if include_symbols:
        characters += string.punctuation
    return ''.join(random.choices(characters, k = length))

def memorable_password(num_of_words: int, seperator: str = "-", capitalization: bool = False) -> str:
    """generates a memorable password from a list of vocabulary words.

    Args:
        num_of_words (int): The number of words in the password.
        seperator (str): The seperator between the words.
        capitalization (bool): Whether to capitalize the first letter of each word."""

    vocab_list = random.choices(vocabs, k = num_of_words)
    if capitalization:
        vocab_list = seperator.join(word.upper() for word in vocab_list)
    return vocab_list

if __name__ == "__main__":
    memorable_password(3, '-', True)