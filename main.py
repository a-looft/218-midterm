from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.plugin_loader import load_plugins
from app.history_facade import HistoryFacade
from app.logger_setup import setup_logging
import logging

def main():
    print("Welcome to the Calculator.")
    print("Type 'exit' to quit.")

    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Calculator started")

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

        logger.info(f"Received command: {cmd_name} with args: {args}")

        if cmd_name == "history":
            logger.info("Displayed history")
            history.print_history()
            continue

        if cmd_name == "save":
            history.save()
            logger.info("Saved history")
            print("History saved.")
            continue

        if cmd_name == "clear":
            history.clear()
            logger.info("Cleared history")
            print("History cleared.")
            continue

        if cmd_name == "load":
            history.load()
            logger.info("Loaded history from file")
            print("History loaded from file.")
            continue

        if cmd_name == "delete":
            history.delete()
            logger.info("Deleted history file")
            print("History file deleted and cleared.")
            continue

        command = command_map.get(cmd_name)
        if not command:
            logger.warning(f"Unknown command: {cmd_name}")
            print(f"unknown command: {cmd_name}")
            continue

        try:
            result = command.execute(args)
            logger.info(f"Executed {cmd_name} with result: {result}")
            print(f"Result: {result}")
            history.add_record(cmd_name, args, result)
        except Exception as e:
            logger.error(f"Error executing {cmd_name}: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
