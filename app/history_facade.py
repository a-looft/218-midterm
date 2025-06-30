import pandas as pd
import os

class HistoryFacade:
    def __init__(self, filepath: str = "data/history.csv"):
        self.filepath = filepath
        if os.path.exists(filepath):
            self.df = pd.read_csv(filepath)
        else:
            self.df = pd.DataFrame(columns=["command", "args", "result"])

    def add_record(self, command: str, args: list[str], result: float):
        new_row = {"command": command, "args": " ".join(args), "result": result}
        self.df.loc[len(self.df)] = new_row

    def save(self):
        self.df.to_csv(self.filepath, index=False)

    def load(self):
        if os.path.exists(self.filepath):
            self.df = pd.read_csv(self.filepath)
        else:
            self.df = pd.DataFrame(columns=["command", "args", "result"])

    def clear(self):
        self.df = pd.DataFrame(columns=["command", "args", "result"])
        self.save()

    def delete(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
            self.clear()

    def print_history(self):
        if self.df.empty:
            print("No history.")
        else:
            print(self.df.to_string(index=False))
