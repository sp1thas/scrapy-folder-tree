import datetime
import os

from . import TreeBase


class DateTree(TreeBase):
    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        today = datetime.date.today()
        return os.path.join(
            dir_name, f"{today.year}", f"{today.month}", f"{today.day}", filename
        )


class TimeTree(TreeBase):
    def build_path(self, filepath) -> str:
        filename = os.path.basename(filepath)
        dir_name = os.path.dirname(filepath)
        now = datetime.datetime.now()
        return os.path.join(
            dir_name, f"{now.hour}", f"{now.minute}", f"{now.second}", filename
        )
