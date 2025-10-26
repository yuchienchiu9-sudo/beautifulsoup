import sys
import re
from pathlib import Path
# 強制使用本地的 beautifulsoup
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from bs4 import BeautifulSoup, SoupReplacer
import time


def make_big_html(sections=300, paras=5, links=6):
    """快速生成多段 HTML 測資"""
    html_parts = ["<!doctype html><html><body>"]
    for s in range(sections):
        html_parts.append(f"<section id='sec{s}'>")
        for p in range(paras):
            html_parts.append(
                f"<p>Section <b>{s}</b> paragraph <b>{p}</b> with <i>italic</i> text.<br/></p>"
            )
        html_parts.append("<ul>")
        for l in range(links):
            html_parts.append(f"<li><a href='#l{s}-{l}'><b>Link{l}</b></a></li>")
        html_parts.append("</ul></section>")
    html_parts.append("</body></html>")
    return "".join(html_parts)

def main():
    print("== Building big HTML sample ==")
    html = make_big_html(sections=400, paras=5, links=8)  # 可調大產更大檔
    print(f"Generated HTML length: {len(html)/1_000_000:.2f} MB")

    r = SoupReplacer("b", "blockquote")

    print("== Parsing with SoupReplacer ==")
    start = time.time()
    soup = BeautifulSoup(html, "html.parser", replacer=r)
    elapsed = time.time() - start

    out_path = Path(__file__).with_name("output_big.html")
    out_path.write_text(soup.prettify(), encoding="utf-8")

    print(f"[OK] Parsed and wrote -> {out_path}")
    print(f"[TIME] {elapsed:.2f}s")

    # 驗證結果
    out_text = out_path.read_text(encoding="utf-8", errors="ignore")
    b_tags = len(re.findall(r"<\s*b(\s|>)", out_text))
    blockquote_tags = len(re.findall(r"<\s*blockquote(\s|>)", out_text))
    print("\n== Result check ==")
    print(f"<b> count after parsing: {b_tags}")
    print(f"<blockquote> count after parsing: {blockquote_tags}")
    print("✅ All <b> replaced successfully!" if b_tags == 0 and blockquote_tags > 0 else "⚠️ Something went wrong.")

if __name__ == "__main__":
    main()
