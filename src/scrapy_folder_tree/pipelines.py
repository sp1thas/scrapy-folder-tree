from abc import ABC

from scrapy.pipelines.files import FilesPipeline  # type: ignore
from scrapy.pipelines.images import ImagesPipeline  # type: ignore
from scrapy.settings import Settings  # type: ignore

from . import config
from .trees import TreeBase
from .trees.date import DateTree, TimeTree
from .trees.hash import HashTree


class FolderTreeBasePipeline(FilesPipeline, ABC):

    tree: TreeBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(config.FOLDER_TREE_DEPTH, 3)
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, *args, **kwargs):
        return self.tree.build_path(super().file_path(*args, **kwargs))


class ImagesTreeBasePipeline(ImagesPipeline, ABC):

    tree: TreeBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(config.FOLDER_TREE_DEPTH, 3)
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, *args, **kwargs):
        return self.tree.build_path(super().file_path(*args, **kwargs))

    def thumb_path(self, *args, **kwargs):
        return self.tree.build_path(super().thumb_path(*args, **kwargs))


class FilesHashTreePipeline(FolderTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = HashTree(self.depth)


class FilesDateTreePipeline(FolderTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = DateTree()


class FilesTimeTreePipeline(FolderTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = TimeTree()


class ImagesHashTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = HashTree(self.depth)


class ImagesDateTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = DateTree()


class ImagesTimeTreePipeline(ImagesTreeBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = TimeTree()


__all__ = [
    FilesHashTreePipeline.__name__,
    FilesDateTreePipeline.__name__,
    FilesTimeTreePipeline.__name__,
    ImagesHashTreePipeline.__name__,
    ImagesDateTreePipeline.__name__,
    ImagesTimeTreePipeline.__name__,
]
