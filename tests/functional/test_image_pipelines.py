import os
import subprocess
from typing import Type

import pytest
import scrapy
from scrapy.pipelines.files import FilesPipeline

from scrapy_folder_tree import ImagesHashTreePipeline, ImagesDateTreePipeline, ImagesTimeTreePipeline

DEFAULT_FEED_URI = 'foo.json'


def default_settings(tmpdir, tree_pipeline: Type[FilesPipeline]) -> list:
    settings = {
            'FEED_URI': os.path.join(str(tmpdir), DEFAULT_FEED_URI),
            'FEED_FORMAT': 'json',
            'IMAGES_STORE': str(tmpdir),
            'ITEM_PIPELINES': {
                f'scrapy_folder_tree.{tree_pipeline.__name__}': 300,
                'scrapy.pipelines.images.ImagesPipeline': 100,
            },
    }
    settings_args = []
    for k, v in settings.items():
        settings_args.append('-s')
        settings_args.append(f'{k}={v}')
    return settings_args


class TestSpider(scrapy.Spider):
    name = 'test_spider'

    start_urls = ['https://books.toscrape.com']

    def parse(self, response, **kwargs):
        yield {'image_urls': [
                f'https://books.toscrape.com/{url_path}'
                for url_path in response.xpath('//div[@class="image_container"]/a/img/@src').getall()
            ]}


@pytest.mark.parametrize('spider', [ImagesHashTreePipeline, ImagesDateTreePipeline, ImagesTimeTreePipeline])
def test_pipelines(spider, tmpdir):
    settings = default_settings(tmpdir, spider)
    print(settings)

    p = subprocess.Popen([
        'scrapy', 'runspider', '-a', 'TestSpider', 'test_image_pipelines.py', *settings
    ])
    print(p.stdout)
