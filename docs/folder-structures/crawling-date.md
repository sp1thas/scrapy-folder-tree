## File name

This group of pipelines uses a folder structure based on crawling date.

 - `scrapy_folder_tree.FilesDateTreePipeline`
 - `scrapy_folder_tree.ImagesDateTreePipeline`

## Example

A file called `fh1udj1.png` and crawled at `2022-01-02`, will be stored using the following folder structure:

```
2022
└── 01
    └── 02
        └── fh1udj1.png
```

## Configuration

You can configure the following in the Scrapy project settings:

 - `FOLDER_TREE_DEPTH` (default: `3`): Specify the folder depth.
 - `FOLDER_TREE_LENGTH` (default: `1`): Specify the folder length.