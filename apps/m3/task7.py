import sys, os
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer
def p_set_class_test(tag):
   
    if tag.name == "p":
        new_attrs = dict(tag.attrs)
        new_attrs["class"] = "test"   
        return new_attrs
    return tag.attrs


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    m2_dir = os.path.join(os.path.dirname(base_dir), "m2")
    sample_html_path = os.path.join(m2_dir, "United States - Wikipedia.html")

    if not os.path.exists(sample_html_path):
        html = (
            "<div>"
            "<p>para1</p>"
            "<p class='old'>para2</p>"
            "<b class='emph'>Hello</b> "
            "<a href='#' class='link'>world</a>"
            "</div>"
        )
    else:
        with open(sample_html_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

    replacer = SoupReplacer(
        
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name,
        
        attrs_xformer=p_set_class_test,
        
        xformer=None,
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    
    out_path = os.path.join(base_dir, "task7-output.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    
    total_p = len(soup.find_all("p"))
    test_p = len(soup.find_all("p", class_="test"))
    print(f"[OK] Wrote: {out_path}")
    print("[Stats] blockquote tags:", len(soup.find_all("blockquote")))
    print(f"[Stats] <p> total: {total_p}")
    print(f"[Stats] <p class='test'>: {test_p}")
    print("[OK] p tags all set to class='test'?:", total_p == test_p)


if __name__ == "__main__":
    main()
