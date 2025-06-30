from app.command import Command

class SquareCommand(Command):
    def name(self):
        return "square"

    def execute(self, args: list[str]) -> float:
        if len(args) != 1:
            raise ValueError("Square command requires exactly one number.")
        return float(args[0]) ** 2
