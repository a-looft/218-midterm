from app.command import Command

class SubtractCommand(Command):
    def name(self):
        return "subtract"

    def execute(self, args: list[str]) -> float:
        if len(args) != 2:
            raise ValueError("Subtract command requires exactly two numbers.")
        return float(args[0]) - float(args[1])
