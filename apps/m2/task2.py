print(">>> task2.py 正在執行 <<<")
import sys
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup, SoupStrainer



def pick_parser(p: Path) -> str:
    
    return "xml" if p.suffix.lower() == ".xml" else "html.parser"

def main():
    if not (2 <= len(sys.argv) <= 3):
        print("Usage: python task2.py <input.html|input.xml> [base_url]", file=sys.stderr)
        sys.exit(2)

    p = Path(sys.argv[1])
    base = sys.argv[2] if len(sys.argv) == 3 else None
    if not p.exists():
        print(f"Error: file not found -> {p}", file=sys.stderr)
        sys.exit(3)

 
    raw = p.read_text(encoding="utf-8", errors="ignore")

  
    only_links = SoupStrainer(name="a")
    soup = BeautifulSoup(raw, features=pick_parser(p), parse_only=only_links)

    tags = soup.find_all("a", href=True)
    print(f"[INFO] <a> count via SoupStrainer: {len(tags)}", file=sys.stderr)

    if len(tags) == 0:
        soup_full = BeautifulSoup(raw, features=pick_parser(p))
        tags = soup_full.find_all("a", href=True)
        print(f"[INFO] fallback (full parse) <a> count: {len(tags)}", file=sys.stderr)

    n = 0
    for a in tags:
        text = " ".join(a.get_text(strip=True).split())
        href = a["href"].strip()
        if base and not href.lower().startswith(("http://", "https://", "mailto:", "tel:")):
            href = urljoin(base, href)
        print(f"{text or '[no text]'} -> {href}")
        n += 1

    print(f"[INFO] total printed: {n}", file=sys.stderr)

if __name__ == "__main__":
    main()



