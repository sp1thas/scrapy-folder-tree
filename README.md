# scrapy-folder-tree

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sp1thas/scrapy-folder-tree/master.svg)](https://results.pre-commit.ci/latest/github/sp1thas/scrapy-folder-tree/master)
[![codecov](https://codecov.io/gh/sp1thas/scrapy-folder-tree/branch/master/graph/badge.svg?token=Y4LGLWOD11)](https://codecov.io/gh/sp1thas/scrapy-folder-tree)
![PyPI](https://img.shields.io/pypi/v/scrapy-folder-tree)
[![GitHub license](https://img.shields.io/github/license/sp1thas/scrapy-folder-tree)](https://github.com/sp1thas/scrapy-folder-tree/blob/master/LICENSE)
![PyPI - Format](https://img.shields.io/pypi/format/scrapy-folder-tree)
![PyPI - Status](https://img.shields.io/pypi/status/scrapy-folder-tree)

This is a scrapy pipeline that provides an easy way to store files and images using various folder structures.


## Supported folder structures:

Given this scraped file: `05b40af07cb3284506acbf395452e0e93bfc94c8.jpg`, you can choose the following folder structures:


<details>
  <summary>Using the file name</summary>

  class: `scrapy-folder-tree.ImagesHashTreePipeline`

  ```
  full
  ├── 0
  .   ├── 5
  .   .   ├── b
  .   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
  ```
</details>


<details>
  <summary>Using the crawling time</summary>

  class: `scrapy-folder-tree.ImagesTimeTreePipeline`

  ```
  full
  ├── 0
  .   ├── 11
  .   .   ├── 48
  .   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
  ```
</details>


<details>
  <summary>Using the crawling date</summary>

  class: `scrapy-folder-tree.ImagesDateTreePipeline`

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
pip install scrapy-folder-tree
```

## Usage

Use the following settings in your project:
```python
ITEM_PIPELINES = {
    'scrapy_folder_tree.FilesHashTreePipeline': 300
}
```

