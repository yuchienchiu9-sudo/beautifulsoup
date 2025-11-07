# apps/m3/task7.py
import sys, os
from pathlib import Path

# 先把專案根目錄加進 sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer
def p_set_class_test(tag):
    """
    只處理 <p>：把 class 設為 'test'（覆蓋或新增）
    其他 tag 原樣回傳屬性（不動）。
    """
    if tag.name == "p":
        new_attrs = dict(tag.attrs)
        new_attrs["class"] = "test"   # BeautifulSoup 允許字串或 list
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
        # 示範 name_xformer：b -> blockquote
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name,
        # 示範 attrs_xformer：只對 <p> 設 class="test"
        attrs_xformer=p_set_class_test,
        # 這裡不做全域副作用，避免刪掉其他元素的 class
        xformer=None,
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # 寫出完整結果
    out_path = os.path.join(base_dir, "task7-output.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    # 顯示重點統計（符合 M1 的 task-7 要求）
    total_p = len(soup.find_all("p"))
    test_p = len(soup.find_all("p", class_="test"))
    print(f"[OK] Wrote: {out_path}")
    print("[Stats] blockquote tags:", len(soup.find_all("blockquote")))
    print(f"[Stats] <p> total: {total_p}")
    print(f"[Stats] <p class='test'>: {test_p}")
    print("[OK] p tags all set to class='test'?:", total_p == test_p)


if __name__ == "__main__":
    main()
