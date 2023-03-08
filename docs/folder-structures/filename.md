## File name

This group of pipelines uses a folder structure based on the file's name.

 - `scrapy_folder_tree.FilesHashTreePipeline`
 - `scrapy_folder_tree.ImagesHashTreePipeline`

## Example

`fh1udj1.png` file will be stored using the following folder structure:

```
f
└── h
    └── 1
        └── fh1udj1.png
```

## Configuration

You can configure the following in the Scrapy project settings:

 - `FOLDER_TREE_DEPTH` (default: `3`): Specify the folder depth.
 - `FOLDER_TREE_LENGTH` (default: `1`): Specify the folder length.