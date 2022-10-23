import datetime
import unittest.mock

from scrapy_folder_tree.config import FOLDER_CONFIG
from scrapy_folder_tree.trees import TreeBase
from scrapy_folder_tree.trees.date import DateTree, TimeTree
from scrapy_folder_tree.trees.hash import HashTree


class TestDateTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = DateTree(FOLDER_CONFIG.TREE_DATE_FORMAT_DEFAULT)

    def test_object_attributes(self) -> None:
        self.assertEqual(self.tree.FORMAT, FOLDER_CONFIG.TREE_DATE_FORMAT_DEFAULT)

    def test_build(self) -> None:
        self.assertEqual(
            self.tree.build_path("randomname.ext"),
            f"{datetime.date.today().strftime('%Y/%m/%d')}/randomname.ext",
        )


class TestHashTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = HashTree(
            FOLDER_CONFIG.TREE_DEPTH_DEFAULT_VALUE,
            FOLDER_CONFIG.TREE_LENGTH_DEFAULT_VALUE,
        )

    def test_object_attributes(self) -> None:
        self.assertEqual(self.tree.DEPTH, 3)
        self.assertEqual(self.tree.LENGTH, 1)

    def test_build(self) -> None:
        self.assertEqual(self.tree.build_path("randomname.ext"), "r/a/n/randomname.ext")


class TestTimeTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = TimeTree(FOLDER_CONFIG.TREE_TIME_FORMAT_DEFAULT)

    def test_object_attributes(self) -> None:
        self.assertEqual(self.tree.FORMAT, FOLDER_CONFIG.TREE_TIME_FORMAT_DEFAULT)

    @unittest.mock.patch("scrapy_folder_tree.trees.date.datetime", autospec=True)
    def test_build(self, mocked_datetime) -> None:
        mocked_datetime.datetime.now.return_value = datetime.datetime(2022, 1, 1)
        self.assertEqual(
            self.tree.build_path("randomname.ext"), "00/00/00/randomname.ext"
        )


class TestTreeAbstract(unittest.TestCase):
    def test_raise_error(self) -> None:
        with self.assertRaises(TypeError):
            TreeBase()
