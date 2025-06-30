import importlib.util
import os
from app.command import Command

def load_plugins(plugin_folder: str = "plugins") -> list[Command]:
    plugins = []
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module_path = os.path.join(plugin_folder, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for obj in module.__dict__.values():
                if isinstance(obj, type) and issubclass(obj, Command) and obj is not Command:
                    plugins.append(obj())
    return plugins
