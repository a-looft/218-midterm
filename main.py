from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.plugin_loader import load_plugins

def main():
    print("Welcome to the Calculator.")
    print("Type 'exit' to quit.")
    commands = [AddCommand(), SubtractCommand()]
    command_map = {cmd.name(): cmd for cmd in commands}

    while True:
        raw_input = input("> ").strip()
        if raw_input == "exit":
            break
        if not raw_input:
            continue

        parts = raw_input.split()
        cmd_name = parts[0]
        args = parts[1:]

        command = command_map.get(cmd_name)
        if not command:
            print(f"unknown command: {cmd_name}")
            continue

        try:
            result = command.execute(args)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
