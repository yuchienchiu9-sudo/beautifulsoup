import unittest
from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

class TestSoupReplacerM3(unittest.TestCase):
    def test_1_name_xformer_simple(self):
        html = "<p>hi <b>world</b></p>"
        r = SoupReplacer(name_xformer=lambda t: "strong" if t.name == "b" else t.name)
        s = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(s.find("b"))
        self.assertIsNotNone(s.find("strong"))
        self.assertEqual(s.find("strong").text, "world")

    def test_2_attrs_xformer_remove_class_and_style(self):
        html = '<p class="x y" id="p1">t</p><b style="c:1">z</b>'
        def drop(tag):
            return {k: v for k, v in tag.attrs.items() if k not in ("class", "style")}
        s = BeautifulSoup(html, "html.parser", replacer=SoupReplacer(attrs_xformer=drop))
        p = s.find("p"); b = s.find("b")
        self.assertEqual(p.get("id"), "p1")
        self.assertIsNone(p.get("class"))
        self.assertIsNone(b.get("style"))

    def test_3_xformer_side_effect_add_attr(self):
        html = "<div><span>mark</span><em>keep</em></div>"
        def mark_span(tag):
            if tag.name == "span":
                tag.attrs["data-marked"] = "1"
        s = BeautifulSoup(html, "html.parser", replacer=SoupReplacer(xformer=mark_span))

        span = s.find("span")
        self.assertIsNotNone(span)
        self.assertEqual(span.get("data-marked"), "1")
        self.assertIsNotNone(s.find("em"))

    def test_4_all_transformers_and_order(self):
        html = '<b class="c">x</b>'
        def nx(t):  # name
            return "strong" if t.name == "b" else t.name
        def ax(t):  # attrs
            out = {k: v for k, v in t.attrs.items() if k != "class"}
            out["data-m3"] = "1"
            return out
        def xx(t):  # post side-effect
            if t.name == "strong":
                t.attrs["role"] = "note"
        s = BeautifulSoup(html, "html.parser",
                          replacer=SoupReplacer(name_xformer=nx, attrs_xformer=ax, xformer=xx))
        strong = s.find("strong")
        self.assertIsNotNone(strong)
        self.assertIsNone(strong.get("class"))
        self.assertEqual(strong.get("data-m3"), "1")
        self.assertEqual(strong.get("role"), "note")

    def test_5_legacy_pair_constructor_compat(self):
        html = "<b>z</b><i>y</i>"
        s = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
        self.assertIsNone(s.find("b"))
        self.assertIsNotNone(s.find("blockquote"))
        self.assertIsNotNone(s.find("i"))

    def test_6_self_closing_tag_pre_post(self):
        html = '<div><img class="thumb" src="x.png"/></div>'
        def ax(t):
            out = {k: v for k, v in t.attrs.items() if k != "class"}
            out["data-processed"] = "1"
            return out
        def xx(t):
            if t.name == "img":
                t.attrs["alt"] = "ok"
        s = BeautifulSoup(html, "html.parser",
                          replacer=SoupReplacer(attrs_xformer=ax, xformer=xx))
        img = s.find("img")
        self.assertIsNotNone(img)
        self.assertIsNone(img.get("class"))
        self.assertEqual(img.get("data-processed"), "1")
        self.assertEqual(img.get("alt"), "ok")

if __name__ == "__main__":
    unittest.main()
