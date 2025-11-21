import unittest
from collections.abc import Iterator

from bs4 import BeautifulSoup, NavigableString, Comment, Tag


class TestIterableSoupM4(unittest.TestCase):

    def test_simple_document_includes_root_and_tags(self):
        html = "<html><body><p>Hi</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)

        self.assertGreaterEqual(len(nodes), 5)
        self.assertIs(nodes[0], soup)
        p_tags = [n for n in nodes if getattr(n, "name", None) == "p"]
        self.assertEqual(len(p_tags), 1)
        self.assertEqual(p_tags[0].string, "Hi")

    def test_traversal_order_is_preorder_like(self):
        html = "<html><body><p>A <b>B</b></p></body></html>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)

        tag_names = [n.name for n in nodes if isinstance(n, Tag)]

        self.assertEqual(tag_names[0:5], ["[document]", "html", "body", "p", "b"])

    def test_includes_text_and_comment_nodes(self):
        html = "<div><!--hi--><p>Hello <b>world</b></p></div>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)
        strings = [n for n in nodes if isinstance(n, NavigableString)]
        comments = [n for n in nodes if isinstance(n, Comment)]

        joined = "".join(str(s) for s in strings)
        self.assertIn("Hello", joined)
        self.assertIn("world", joined)

        self.assertEqual(len(comments), 1)
        self.assertIn("hi", comments[0])

    def test_empty_document_still_yields_root(self):
        soup = BeautifulSoup("", "html.parser")
        nodes = list(soup)

        self.assertGreaterEqual(len(nodes), 1)
        self.assertIs(nodes[0], soup)

    def test_iter_returns_iterator_not_list(self):
        html = "<p>Hi</p>"
        soup = BeautifulSoup(html, "html.parser")

        it = iter(soup)

        self.assertIsInstance(it, Iterator)
        self.assertNotIsInstance(it, list)

        first = next(it)
        self.assertIs(first, soup)


if __name__ == "__main__":
    unittest.main()
