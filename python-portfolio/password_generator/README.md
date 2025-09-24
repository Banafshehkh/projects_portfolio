# Password Generator Dashboard

## Project Overview
The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. The user is able to either generate the password randomly, as a memorable sequence of words, or as a pin code.

## Project Structure
The project has the following structure:

- `password_generators.py`: A Python module containing the password generators classes; `RandomPasswordGenerator`, `MemorablePasswordGenerator`, and `PinCodeGenerator`.
- `dashboard.py`: A Python script using Streamlit to create a web app interface for the password generators.
- `README.md`: Documentation for the project solution.

## Getting Started

Follow the instructions below to run the code.

### Prerequisites

- Python 3.6 or later
- Streamlit
- NLTK

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

Then install Streamlit using pip:

```bash
pip install streamlit
```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```sh
streamlit run dashboard.py
```

This will open a web page in your default browser running on your localhost.