import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from bs4 import BeautifulSoup, SoupReplacer
import bs4  

html = "<div><b class='x'>hi</b><i>ok</i><br/></div>"

r = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(html, "html.parser", replacer=r)

print("== prettify ==")
print(soup.prettify().rstrip())  
print("== assertions ==")
bb = soup.find("blockquote")
print("blockquote found? ", bb is not None)
print("class preserved? ", (bb is not None) and (bb.get("class") == ["x"]))
print("text OK? ", (bb is not None) and (bb.text == "hi"))
print("i unchanged? ", soup.find('i') is not None)
print("br still there? ", soup.find('br') is not None)


print("Using:", Path(bs4.__file__).resolve())
