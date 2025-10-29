from bs4 import BeautifulSoup, SoupReplacer

html = "<p>Hello <b>world</b> and <B>UCI</B></p>"
soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
print(soup.prettify())
