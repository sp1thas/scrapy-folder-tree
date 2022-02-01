from abc import ABC, abstractmethod


class HierarchyBase(ABC):
    @abstractmethod
    def build_path(self, filepath: str):
        pass
