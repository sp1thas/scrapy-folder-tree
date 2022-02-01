from abc import ABC, abstractmethod


class TreeBase(ABC):
    @abstractmethod
    def build_path(self, filepath: str):
        pass
