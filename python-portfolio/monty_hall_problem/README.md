# Monty Hall Game Simulation

## Description
This is the implementation of the famous Monty Hall Probelm. You can see the statistics of playing the game in numerous runs of switching and not switching the doors.

## Project Structure
```
├─ README.md
├─ requirements.txt
└─ src
   ├─ monty_hall.py
```
- `requirements.txt`: Contains all the required modules and libraries needed to run the project
- `src/monty_hall_probelm.py`: Contains the Python program to simulate the Monty Hall game

## Requirements

- Python 3.7 or higher
To install necessary packages, run `pip install -r requirements.txt`.

## Usage

You can play the Monty Hall game simulation by adding the `src` directory to the PYTHONPATH and running:

`python3 src/monty_hall.py`

## Results

You should get something like the following:

```
Winning percentage without switching doors: 31.80%
Winning percentage with    switching doors: 68.20%
```