# Password Generator - OOP Approach

The purpose of this project is to build a password generator in three different ways:

1. Random Passwords
2. Memorable Passwords
3. Pin Codes

## How It Works

The password generator uses the Python `random` module to generate passwords based on user preferences. TEach class is representing a different type of password generation:

1. `RandomPasswordGenerator` generates a completely random password of a specified length, optional with numbers, and symbols.
2. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and use capitalized words.
3. `PinCodeGenerator` creates a numeric password of a specified length.

Each generator class inherits from a base `PasswordGenerator` class. They each override the base class's `generate()` method in order to provide their own unique password generation functionality.

## Requirements

- Python 3.7+
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

## Running the Project

Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python main.py
```

Be sure to replace `/your/path/to/main/directory` with the actual path to the directory containing your project.

## Testing

The `main.py` script also includes test cases for each password generator. The script will print out a test password for each generator and run checks to make sure the password matches the expected format.
