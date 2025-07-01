# Advanced Python Calculator – Midterm Project

this project is an advanced command-line calculator with plugin support, history tracking, and REPL interaction, developed for the IS218 Building Web Applications midterm

---

### Command Pattern
each calculator operation is implemented as a Command object with a `.name()` and `.execute()` method. this allows for the REPL to treat all commands the same and easily register new ones.

---

### Facade Pattern
the `HistoryFacade` class provides a more simplified interface to Pandas operations like loading, saving, clearing, and displaying calculation history.

---

### Logging and Environment Config

logging is configured using pythons built-in `logging` module, with settings dynamically loaded from environment variables and a configuration file.

- `LOG_FILE` and `LOG_LEVEL` are defined in `.env`
- log output goes to both `calc.log` and the terminal
- the `logging.conf` file sets the format and output destinations

---

### How to Run the Calculator

run the program with:
python3 main.py

example commands to type in REPL:
add 5 3
square 4
history
save
clear
exit

---

### Demo Video

[Watch Demo Video](https://drive.google.com/file/d/1vLR0Mt7LMZ-GZm9TPlRnHOlwoaMXlTO2/view?usp=sharing)
