# Advanced Python Calculator – Midterm Project

this project is an advanced command-line calculator with plugin support, history tracking, and REPL interaction, developed for the IS218 Building Web Applications midterm

---

### Command Pattern
each calculator operation is implemented as a Command object with a `.name()` and `.execute()` method. this allows for the REPL to treat all commands the same and easily register new ones.

---

### Facade Pattern
the `HistoryFacade` class provides a more simplified interface to Pandas operations like loading, saving, clearing, and displaying calculation history.
