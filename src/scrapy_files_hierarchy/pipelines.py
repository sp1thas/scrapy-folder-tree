from abc import ABC

from scrapy.pipelines.files import FilesPipeline  # type: ignore
from scrapy.pipelines.images import ImagesPipeline  # type: ignore
from scrapy.settings import Settings  # type: ignore

from . import config
from .hierarchies import HierarchyBase
from .hierarchies.date import DateHierarchy, TimeHierarchy
from .hierarchies.hash import HashHierarchy


class FolderHierarchyBasePipeline(FilesPipeline, ABC):

    hierarchy: HierarchyBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(config.FOLDER_HIERARCHY_DEPTH, 3)
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, *args, **kwargs):
        return self.hierarchy.build_path(super().file_path(*args, **kwargs))


class ImagesHierarchyBasePipeline(ImagesPipeline, ABC):

    hierarchy: HierarchyBase

    def __init__(self, store_uri, download_func=None, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.depth = settings.getint(config.FOLDER_HIERARCHY_DEPTH, 3)
        super().__init__(store_uri, download_func=download_func, settings=settings)

    def file_path(self, *args, **kwargs):
        return self.hierarchy.build_path(super().file_path(*args, **kwargs))

    def thumb_path(self, *args, **kwargs):
        return self.hierarchy.build_path(super().thumb_path(*args, **kwargs))


class FilesHashHierarchyPipeline(FolderHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = HashHierarchy(self.depth)


class FilesDateHierarchyPipeline(FolderHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = DateHierarchy()


class FilesTimeHierarchyPipeline(FolderHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = TimeHierarchy()


class ImagesHashHierarchyPipeline(ImagesHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = HashHierarchy(self.depth)


class ImagesDateHierarchyPipeline(ImagesHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = DateHierarchy()


class ImagesTimeHierarchyPipeline(ImagesHierarchyBasePipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hierarchy = TimeHierarchy()


__all__ = [
    FilesHashHierarchyPipeline.__name__,
    FilesDateHierarchyPipeline.__name__,
    FilesTimeHierarchyPipeline.__name__,
    ImagesHashHierarchyPipeline.__name__,
    ImagesDateHierarchyPipeline.__name__,
    ImagesTimeHierarchyPipeline.__name__,
]
