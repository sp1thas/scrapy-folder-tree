# scrapy-files-hierarchy

 [![build](https://github.com/sp1thas/scrapy-files-hierarchy/actions/workflows/build.yml/badge.svg)](https://github.com/sp1thas/scrapy-files-hierarchy/actions/workflows/build.yml) ![PyPI](https://img.shields.io/pypi/v/scrapy-files-hierarchy) [![GitHub license](https://img.shields.io/github/license/sp1thas/scrapy-files-hierarchy)](https://github.com/sp1thas/scrapy-files-hierarchy/blob/master/LICENSE) ![PyPI - Format](https://img.shields.io/pypi/format/scrapy-files-hierarchy) ![PyPI - Status](https://img.shields.io/pypi/status/scrapy-files-hierarchy) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg) ![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg) ![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)

This is a scrapy pipeline that provides an easy way to store files and images using various folder structures.


## Supported folder structures:

Given this scraped file: `05b40af07cb3284506acbf395452e0e93bfc94c8.jpg`, you can choose the following folder structures:


<details>
  <summary>Using file name</summary>

  class: `scrapy_files_hierarchy.ImagesHashHierarchyPipeline`
  
  ```
  full
  ├── 0
  .   ├── 5
  .   .   ├── b
  .   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
  ```
</details>


<details>
  <summary>Using crawling time</summary>

  class: `scrapy_files_hierarchy.ImagesTimeHierarchyPipeline`
  
  ```
  full
  ├── 0
  .   ├── 11
  .   .   ├── 48
  .   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
  ```
</details>


<details>
  <summary>Using crawling date</summary>

  class: `scrapy_files_hierarchy.ImagesDateHierarchyPipeline`
  
  ```
  full
  ├── 2022
  .   ├── 1
  .   .   ├── 24
  .   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
  ```
</details>


## Installation

```shell
pip install scrapy-files-hierarchy
```

## Usage

Use the following settings in your project:
```python
ITEM_PIPELINES = {
    'scrapy_files_hierarchy.FilesHierarchyPipeline': 300
}

FOLDER_HIERARCHY_DEPTH = 3
```