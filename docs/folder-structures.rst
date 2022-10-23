Folder structures
=================

This scrapy pipelines provides the following folder structures

File name
---------
This group of pipelines uses a folder structure based on the file's name.

pipeline classes:

- :code:`scrapy_folder_tree.FilesHashTreePipeline`
- :code:`scrapy_folder_tree.ImagesHashTreePipeline`

Configuration
+++++++++++++

:code:`FOLDER_TREE_DEPTH` (default :code:`3`): Specify the folder depth.
:code:`FOLDER_TREE_LENGTH` (default :code:`1`): Specify the folder length.

Crawling date
-------------

This group of pipelines uses a folder structure based on crawling date.

- :code:`scrapy_folder_tree.FilesDateTreePipeline`
- :code:`scrapy_folder_tree.ImagesDateTreePipeline`

Configuration
+++++++++++++

:code:`FOLDER_TREE_DATE_FORMAT` (default :code:`%Y/%m/%d`): Specify a custom date format.

Crawling time
-------------

This group of pipelines uses a folder structure based on crawling time.

- :code:`scrapy_folder_tree.FilesTimeTreePipeline`
- :code:`scrapy_folder_tree.ImagesTimeTreePipeline`

Configuration
+++++++++++++

:code:`FOLDER_TREE_TIME_FORMAT` (default :code:`%H/%M/%S`): Specify a custom date format.