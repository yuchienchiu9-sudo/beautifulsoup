import unittest
from bs4 import BeautifulSoup, SoupReplacer


class TestSoupReplacerTransformers(unittest.TestCase):
    def test_name_xformer_basic(self):
        html = "<div><b>hi</b><i>ok</i></div>"
        r = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("i"))
        self.assertEqual([t.name for t in soup.div.children if getattr(t, 'name', None)], ["blockquote", "i"])

    def test_attrs_xformer_replaces_attrs(self):
        def swap_attrs(tag):
            if tag.name == "a":
                return {"href": "https://example.com", "rel": ["noopener"]}
            return tag.attrs

        html = '<div><a class="x" href="#">link</a></div>'
        r = SoupReplacer(attrs_xformer=swap_attrs)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        a = soup.find("a")
        self.assertEqual(a.get("href"), "https://example.com")
        self.assertEqual(a.get("rel"), ["noopener"])
        self.assertIsNone(a.get("class"))

    def test_xformer_side_effect_removes_class(self):
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]

        html = "<div><p class='keep'>a</p><span class='gone'>b</span></div>"
        r = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(soup.find("p").get("class"))
        self.assertIsNone(soup.find("span").get("class"))

    def test_combined_transformers(self):
        def name_x(tag):
            return "em" if tag.name == "i" else tag.name

        def attrs_x(tag):
            if tag.name == "em":
                return {"data-x": "1"}
            return tag.attrs

        def any_x(tag):
            if tag.name == "strong":
                tag.attrs["role"] = "strong"

        html = "<div><i>hi</i><strong>ok</strong></div>"
        r = SoupReplacer(name_xformer=name_x, attrs_xformer=attrs_x, xformer=any_x)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(soup.find("i"))
        em = soup.find("em")
        self.assertEqual(em.get("data-x"), "1")
        strong = soup.find("strong")
        self.assertEqual(strong.get("role"), "strong")

    def test_end_tag_renamed_matches(self):
        # Ensure renamed start tags are properly closed and nested
        r = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        html = "<div><b><span>t</span></b></div>"
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNotNone(soup.find("blockquote"))
        self.assertEqual(soup.find("blockquote").span.text, "t")

    def test_noop_replacer(self):
        soup = BeautifulSoup("<div><u>x</u></div>", "html.parser", replacer=SoupReplacer())
        self.assertIsNotNone(soup.find("u"))


if __name__ == "__main__":
    unittest.main()


