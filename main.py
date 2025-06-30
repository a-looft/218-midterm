from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.plugin_loader import load_plugins
from app.history_facade import HistoryFacade

def main():
    print("Welcome to the Calculator.")
    print("Type 'exit' to quit.")
    commands = [AddCommand(), SubtractCommand()] + load_plugins()
    command_map = {cmd.name(): cmd for cmd in commands}
    history = HistoryFacade()

    while True:
        raw_input = input("> ").strip()
        if raw_input == "exit":
            break
        if not raw_input:
            continue


        parts = raw_input.split()
        cmd_name = parts[0]
        args = parts[1:]


        if cmd_name == "history":
            history.print_history()
            continue

        if cmd_name == "save":
            history.save()
            print("History saved.")
            continue

        if cmd_name == "clear":
            history.clear()
            print("History cleared.")
            continue

        if cmd_name == "load":
            history.load()
            print("History loaded from file.")
            continue

        if cmd_name == "delete":
            history.delete()
            print("History file deleted and cleared.")
            continue


        command = command_map.get(cmd_name)
        if not command:
            print(f"unknown command: {cmd_name}")
            continue

        try:
            result = command.execute(args)
            print(f"Result: {result}")
            history.add_record(cmd_name, args, result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
