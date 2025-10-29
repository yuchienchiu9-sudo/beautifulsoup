import unittest
from bs4 import BeautifulSoup, SoupReplacer

class TestSoupReplacerBasic(unittest.TestCase):
    """Verify that SoupReplacer correctly replaces tags during parsing."""

    def test_case_insensitive_replacement(self):
        html = "<div><b>hi</b> <B>there</B></div>"
        soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))

       
        self.assertIsNone(soup.find("b"))

       
        blocks = soup.find_all("blockquote")
        self.assertEqual(len(blocks), 2)
        self.assertEqual([t.get_text(strip=True) for t in blocks], ["hi", "there"])

    def test_no_replacement_for_other_tags(self):
        html = "<p><i>ok</i><br/></p>"
        soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))

      
        self.assertIsNotNone(soup.find("i"))
        self.assertIsNotNone(soup.find("br"))

if __name__ == "__main__":
    unittest.main()
