import os
from argparse import Namespace

FOLDER_CONFIG = Namespace(
    TREE_DEPTH_NAME="FOLDER_TREE_DEPTH",
    TREE_DEPTH_DEFAULT_VALUE=3,
    TREE_DATE_FORMAT_NAME="FOLDER_TREE_DATE_FORMAT",
    TREE_DATE_FORMAT_DEFAULT=os.path.join("%Y", "%m", "%d"),
    TREE_TIME_FORMAT_NAME="FOLDER_TREE_TIME_FORMAT",
    TREE_TIME_FORMAT_DEFAULT=os.path.join("%H", "%M", "%S"),
)
