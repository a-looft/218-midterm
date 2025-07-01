from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand

def test_add():
    command = AddCommand()
    result = command.execute(["5", "3"])
    assert result == 8.0

def test_subtract():
    command = SubtractCommand()
    result = command.execute(["10", "4"])
    assert result == 6.0
