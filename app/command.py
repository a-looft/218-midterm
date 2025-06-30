from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, args: list[str]) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    def help(self) -> str:
        return f"{self.name()} [num1] [num2]"
