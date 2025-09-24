# Number to Word Converter

A Python program that converts integers into their word representations. This utility can handle numbers from 0 to 999,999,999,999 (999 billion).

## Features

- Converts integers to their English word equivalents
- Supports numbers from 0 to 999,999,999,999
- Recursive algorithm for handling large numbers
- Clean, modular code structure with separate constants file

## Project Structure

```
number_to_word/
├── README.md
└── src/
    ├── constants.py      # Word mappings for numbers
    └── num_to_word.py    # Main conversion logic
```

## How It Works

The program uses a recursive approach to convert numbers to words:

1. **Numbers 0-19**: Direct lookup from `UNDER_20` array
2. **Numbers 20-99**: Combines tens and units using `TENS` array
3. **Numbers 100+**: Uses recursive calls with `ABOVE_100` mappings for hundreds, thousands, millions, and billions

## Usage

### Interactive Mode
Run the script directly to enter a number interactively:

```bash
python src/num_to_word.py
```

### As a Module
Import and use the `num_to_word` function in your own code:

```python
from src.num_to_word import num_to_word

# Convert numbers to words
print(num_to_word(42))        # "Forty Two"
print(num_to_word(123))       # "One Hundred Twenty Three"
print(num_to_word(1234567))   # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

## Examples

| Number | Word Representation |
|--------|-------------------|
| 0 | Zero |
| 15 | Fifteen |
| 42 | Forty Two |
| 100 | One Hundred |
| 123 | One Hundred Twenty Three |
| 1,000 | One Thousand |
| 1,234 | One Thousand Two Hundred Thirty Four |
| 1,000,000 | One Million |
| 1,234,567 | One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven |
| 1,000,000,000 | One Billion |

## Requirements

- Python 3.6 or higher
- No external dependencies

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the script directly or import as a module

## Limitations

- Only supports numbers from 0 to 999,999,999,999
- Numbers outside this range will display "Number out of range"
- Currently only supports English word representations

## Code Structure

### `constants.py`
Contains the word mappings:
- `UNDER_20`: Numbers 0-19
- `TENS`: Tens place values (20, 30, 40, etc.)
- `ABOVE_100`: Large number units (Hundred, Thousand, Million, Billion)

### `num_to_word.py`
Main conversion logic with the `num_to_word()` function that handles the recursive conversion process.

