from abc import ABC, abstractmethod
import string
import random
import nltk


class PasswordGenerator:
    @abstractmethod
    def generate(self) -> str:
        pass

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = True, include_symbols: bool = True ):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if self.include_numbers:
            self.characters += string.digits
        if self.include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])

class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
        
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, number_of_words, seperator: str = '-', capitalization: bool = False):
        self.number_of_words = number_of_words
        self.seperator = seperator
        self.capitalization = capitalization

    def generate(self):
        words = [random.choice(nltk.corpus.words.words()) for _ in range(self.number_of_words)]
        if self.capitalization:
            # Convert to uppercase
            words = [word.upper() for word in words]
        else:
            # Convert to lowercase
            words = [word.lower() for word in words]
            
        return self.seperator.join(words)
