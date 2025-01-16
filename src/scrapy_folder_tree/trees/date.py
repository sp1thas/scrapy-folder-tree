import datetime
import os

from scrapy_folder_tree.trees import TreeBase


class DateTree(TreeBase):
    def __init__(self, format: str) -> None:
        self.FORMAT = format

    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        return os.path.join(
            dir_name, datetime.date.today().strftime(self.FORMAT), filename
        )


class TimeTree(TreeBase):
    def __init__(self, format: str) -> None:
        self.FORMAT = format

    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        return os.path.join(
            dir_name, datetime.datetime.now().strftime(self.FORMAT), filename
        )
