# Python Projects Portfolio

Welcome to my collection of beginner-friendly Python projects! This portfolio showcases a variety of practical applications, games, and utilities that demonstrate fundamental programming concepts and real-world problem-solving skills.

## 🚀 Projects Overview

This portfolio contains **8 diverse Python projects** ranging from simple command-line utilities to interactive web applications. Each project is designed to be educational, practical, and fun to use.

## 📁 Project Directory

| Project | Description | Technology | Difficulty |
|---------|-------------|------------|------------|
| [Contact Book](#contact-book) | Personal contact management system | Python CLI | ⭐ |
| [Currency Converter](#currency-converter) | Real-time currency conversion | Python + API | ⭐⭐ |
| [Happy Numbers](#happy-numbers) | Mathematical number theory checker | Python + Streamlit | ⭐⭐ |
| [Monty Hall Problem](#monty-hall-problem) | Probability simulation game | Python | ⭐⭐ |
| [Number to Word](#number-to-word) | Integer to text converter | Python | ⭐ |
| [Password Generator](#password-generator) | Secure password creation tool | Python + Streamlit | ⭐⭐ |
| [Rock Paper Scissors](#rock-paper-scissors) | Classic game implementation | Python | ⭐ |
| [Tic Tac Toe](#tic-tac-toe) | Interactive board game | Python + Streamlit | ⭐⭐ |

---

## 📋 Project Details

### Contact Book
**📞 Personal Contact Management System**

A command-line application for managing personal contacts with full CRUD operations.

**Features:**
- Add, edit, view, and delete contacts
- Store name, phone, email, and address
- Interactive menu system
- Data persistence during session

**Tech Stack:** Python 3.x, No external dependencies

**Quick Start:**
```bash
cd contact_book
python src/contact_book.py
```

---

### Currency Converter
**💱 Real-time Currency Exchange**

An interactive dashboard for converting between different currencies using live exchange rates.

**Features:**
- Real-time exchange rates
- Multiple currency support
- Interactive web interface
- Historical rate tracking

**Tech Stack:** Python, Streamlit, API integration

**Quick Start:**
```bash
cd currency_convertor
streamlit run src/dashboard.py
```

---

### Happy Numbers
**🔢 Mathematical Number Theory Explorer**

An interactive web application that determines whether a number is "happy" using mathematical algorithms.

**Features:**
- Step-by-step calculation visualization
- Educational content about happy numbers
- Real-time number checking
- Beautiful web interface

**Tech Stack:** Python, Streamlit

**Quick Start:**
```bash
cd happy_numbers
pip install streamlit
streamlit run src/app.py
```

**What are Happy Numbers?**
A happy number is defined by repeatedly replacing it with the sum of squares of its digits until it reaches 1 or enters a cycle.

---

### Monty Hall Problem
**🎲 Probability Simulation Game**

A statistical simulation of the famous Monty Hall problem, demonstrating probability theory through game theory.

**Features:**
- Monte Carlo simulation
- Statistical analysis
- Educational probability concepts
- Performance comparison (switching vs. not switching)

**Tech Stack:** Python, Statistical analysis

**Quick Start:**
```bash
cd monty_hall_problem
pip install -r requirements.txt
python src/monty_hall_problem.py
```

**Expected Results:**
- Without switching: ~33% win rate
- With switching: ~67% win rate

---

### Number to Word
**🔤 Integer to Text Converter**

A utility that converts integers into their English word representations, supporting numbers up to 999 billion.

**Features:**
- Supports numbers 0 to 999,999,999,999
- Recursive algorithm implementation
- Clean, modular code structure
- Interactive and programmatic usage

**Tech Stack:** Python 3.6+

**Quick Start:**
```bash
cd number_to_word
python src/num_to_word.py
```

**Example:**
- 42 → "Forty Two"
- 1,234,567 → "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

---

### Password Generator
**🔐 Secure Password Creation Tool**

A comprehensive password generation system with multiple strategies for different security needs.

**Features:**
- Random password generation
- Memorable word-based passwords
- PIN code generation
- Customizable length and complexity
- Interactive web dashboard

**Tech Stack:** Python, Streamlit, NLTK

**Quick Start:**
```bash
cd password_generator
pip install -r requirements.txt
streamlit run src/dashboard.py
```

---

### Rock Paper Scissors
**✂️ Classic Game Implementation**

A command-line implementation of the popular Rock, Paper, Scissors game with computer opponent.

**Features:**
- Human vs. computer gameplay
- Score tracking
- Interactive game loop
- Object-oriented design

**Tech Stack:** Python 3.7+

**Quick Start:**
```bash
cd rock_paper_scissors
python src/game.py
```

---

### Tic Tac Toe
**⭕ Interactive Board Game**

A web-based implementation of the classic Tic Tac Toe game with an intuitive interface.

**Features:**
- Interactive web interface
- Player vs. player gameplay
- Game state management
- Responsive design

**Tech Stack:** Python, Streamlit

**Quick Start:**
```bash
cd tic_tac_toe
streamlit run src/app.py
```

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd projects_portfolio/python-portfolio
   ```

2. **Install global dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Navigate to any project:**
   ```bash
   cd <project-name>
   ```

4. **Follow project-specific instructions** in each project's README

### Project-Specific Requirements

Some projects have their own requirements files:
- `happy_numbers/requirements.txt`
- `monty_hall_problem/requirements.txt`
- `password_generator/requirements.txt`

Install them with:
```bash
pip install -r requirements.txt
```

**Happy Coding!** 🐍✨

*Built with Python and lots of curiosity*
