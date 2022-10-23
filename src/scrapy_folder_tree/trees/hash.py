import os

from . import TreeBase


class HashTree(TreeBase):
    def __init__(self, depth: int, length: int) -> None:
        self.DEPTH = depth
        self.LENGTH = length

    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        return os.path.join(*[filename[i:i + self.LENGTH] for i in range(0, self.DEPTH * self.LENGTH, self.LENGTH)], filename)
