# scrapy-files-hierarchy

This is a scrapy pipeline that provides an easy way to store files and images using various folder structures.


## Supported folder structures:

Given this scraped file: `05b40af07cb3284506acbf395452e0e93bfc94c8.jpg`, you can choose the folloing folder structures:

### `scrapy_files_hierarchy.ImagesHierarchyPipeline`

```
full
├── 0
.   ├── 5
.   .   ├── b
.   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
```

### `scrapy_files_hierarchy.ImagesDateHierarchyPipeline`
```
full
├── 2022
.   ├── 1
.   .   ├── 27
.   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
```

### `scrapy_files_hierarchy.ImagesTimeHierarchyPipeline`
```
full
├── 0
.   ├── 11
.   .   ├── 48
.   .   .   ├── 05b40af07cb3284506acbf395452e0e93bfc94c8.jpg
```


## Installation

```shell
pip install scrapy-files-hierarchy
```

## Usage

```python
ITEM_PIPELINES = {
    'scrapy_files_hierarchy.FileHierarchyPipeline': 300
}

FOLDER_HIERARCHY_DEPTH = 3
```