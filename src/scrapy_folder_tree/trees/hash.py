import os

from . import TreeBase


class HashTree(TreeBase):
    def __init__(self, depth: int, length: int) -> None:
        self.DEPTH = depth
        self.LENGTH = length

    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        return os.path.join(
            dir_name,
            *[
                filename[i : i + self.LENGTH]
                for i in range(0, self.DEPTH * self.LENGTH, self.LENGTH)
            ],
            filename
        )
