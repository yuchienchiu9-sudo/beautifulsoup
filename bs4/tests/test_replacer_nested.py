import unittest
from bs4 import BeautifulSoup, SoupReplacer

class TestSoupReplacerNested(unittest.TestCase):
    """Check nested tag handling and attribute preservation."""

    def test_nested_and_attribute_preservation(self):
        html = "<div><b class='x'>hi</b><i>ok</i><br/></div>"
        soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))

        bb = soup.find("blockquote")
        self.assertIsNotNone(bb)
        self.assertEqual(bb.get("class"), ["x"])     
        self.assertEqual(bb.text, "hi")              
        self.assertIsNotNone(soup.find("i"))         
        self.assertIsNotNone(soup.find("br"))        

    def test_deeply_nested_tags(self):
        html = "<p><b><span><b>inner</b></span></b></p>"
        soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
        blocks = soup.find_all("blockquote")
       
        self.assertEqual(len(blocks), 2)
        self.assertIn("inner", soup.prettify())

if __name__ == "__main__":
    unittest.main()
