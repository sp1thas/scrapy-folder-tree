import unittest

from scrapy_folder_tree.pipelines import *


def test_pipelines(tmp_path) -> None:
    FilesTimeTreePipeline(store_uri=str(tmp_path))
    ImagesTimeTreePipeline(store_uri=str(tmp_path))
    FilesDateTreePipeline(store_uri=str(tmp_path))
    ImagesDateTreePipeline(store_uri=str(tmp_path))
    FilesHashTreePipeline(store_uri=str(tmp_path))
    ImagesHashTreePipeline(store_uri=str(tmp_path))
