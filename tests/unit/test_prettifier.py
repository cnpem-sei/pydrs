import unittest
from unittest.mock import call, patch

from pydrs.utils import prettier_print


class TestPrettifier(unittest.TestCase):
    @patch("builtins.print")
    def test_root(self, print):
        prettier_print({"Hello": "World", "Testing": 123})
        print.assert_has_calls([call("Hello: World"), call("Testing: 123")])

    @patch("builtins.print")
    def test_list(self, print):
        prettier_print({"Hello": ["1", "2", "3"]})
        print.assert_called_with("Hello: ['1', '2', '3']")

    @patch("builtins.print")
    def test_first_degree_recursion(self, print):
        prettier_print({"parent": {"child": "abc"}})
        print.assert_called_with("PARENT Child: abc")

    @patch("builtins.print")
    def test_first_degree_recursion_with_space(self, print):
        prettier_print({"parent_space": {"child": "abc"}})
        print.assert_called_with("PARENT SPACE Child: abc")

    @patch("builtins.print")
    def test_second_degree_recursion(self, print):
        """Tests if parent, children and grandchildren are printed correctly"""
        prettier_print({"parent": {"child": {"grandchild": "abc"}}})
        print.assert_called_with("PARENT CHILD Grandchild: abc")


if __name__ == "__main__":
    unittest.main()
