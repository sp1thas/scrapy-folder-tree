## File name

This group of pipelines uses a folder structure based on crawling date.

 - `scrapy_folder_tree.FilesTimeTreePipeline`
 - `scrapy_folder_tree.ImagesTimeTreePipeline`

## Example

A file called `fh1udj1.png` and crawled at `13:52:20`, will be stored using the following folder structure:

```
13
└── 52
    └── 20
        └── fh1udj1.png
```

## Configuration

You can configure the following in the Scrapy project settings:

 - `FOLDER_TREE_TIME_FORMAT` (default: `%H/%M/%S`): Specify a custom date format.