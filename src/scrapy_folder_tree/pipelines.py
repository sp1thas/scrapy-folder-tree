from abc import ABC

from scrapy.pipelines.files import FilesPipeline  # type: ignore
from scrapy.pipelines.images import ImagesPipeline  # type: ignore
from scrapy.settings import Settings  # type: ignore

from scrapy_folder_tree.config import FOLDER_CONFIG
from scrapy_folder_tree.trees import TreeBase
from scrapy_folder_tree.trees.date import DateTree, TimeTree
from scrapy_folder_tree.trees.hash import HashTree


class FilesTreeBasePipeline(FilesPipeline, ABC):
    tree: TreeBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(
            FOLDER_CONFIG.TREE_DEPTH_NAME, FOLDER_CONFIG.TREE_DEPTH_DEFAULT_VALUE
        )
        self.LENGTH = settings.getint(
            FOLDER_CONFIG.TREE_FOLDER_LENGTH, FOLDER_CONFIG.TREE_LENGTH_DEFAULT_VALUE
        )
        self.date_format = settings.get(
            FOLDER_CONFIG.TREE_DATE_FORMAT_NAME, FOLDER_CONFIG.TREE_DATE_FORMAT_DEFAULT
        )
        self.time_format = settings.get(
            FOLDER_CONFIG.TREE_TIME_FORMAT_NAME, FOLDER_CONFIG.TREE_TIME_FORMAT_DEFAULT
        )
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, request, response=None, info=None, *, item=None):
        return self.tree.build_path(super().file_path(request, response, info, item=item))


class ImagesTreeBasePipeline(ImagesPipeline, ABC):
    tree: TreeBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(
            FOLDER_CONFIG.TREE_DEPTH_NAME, FOLDER_CONFIG.TREE_DEPTH_DEFAULT_VALUE
        )
        self.LENGTH = settings.getint(
            FOLDER_CONFIG.TREE_FOLDER_LENGTH, FOLDER_CONFIG.TREE_LENGTH_DEFAULT_VALUE
        )
        self.date_format = settings.get(
            FOLDER_CONFIG.TREE_DATE_FORMAT_NAME, FOLDER_CONFIG.TREE_DATE_FORMAT_DEFAULT
        )
        self.time_format = settings.get(
            FOLDER_CONFIG.TREE_TIME_FORMAT_NAME, FOLDER_CONFIG.TREE_TIME_FORMAT_DEFAULT
        )
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, request, response=None, info=None, *, item=None):
        return self.tree.build_path(super().file_path(request, response, info, item=item))

    def thumb_path(self, request, thumb_id, response=None, info=None, *, item=None):
        return self.tree.build_path(super().thumb_path(request, thumb_id, response, info, item=item))


class FilesHashTreePipeline(FilesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = HashTree(self.depth, self.LENGTH)


class FilesDateTreePipeline(FilesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = DateTree(self.date_format)


class FilesTimeTreePipeline(FilesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = TimeTree(self.time_format)


class ImagesHashTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = HashTree(self.depth, self.LENGTH)


class ImagesDateTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = DateTree(self.date_format)


class ImagesTimeTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = TimeTree(self.time_format)


__all__ = [
    FilesHashTreePipeline.__name__,
    FilesDateTreePipeline.__name__,
    FilesTimeTreePipeline.__name__,
    ImagesHashTreePipeline.__name__,
    ImagesDateTreePipeline.__name__,
    ImagesTimeTreePipeline.__name__,
]
