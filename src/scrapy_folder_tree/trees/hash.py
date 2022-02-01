import os

from . import TreeBase


class HashTree(TreeBase):
    def __init__(self, depth: int) -> None:
        self.DEPTH = depth

    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        return os.path.join(dir_name, *[_ for _ in filename[: self.DEPTH]], filename)
