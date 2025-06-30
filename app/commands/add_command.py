from app.command import Command

class AddCommand(Command):
    def name(self):
        return "add"

    def execute(self, args: list[str]) -> float:
        if len(args) != 2:
            raise ValueError("Add command requires exactly two numbers.")
        return float(args[0]) + float(args[1])
