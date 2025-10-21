from bs4 import BeautifulSoup, SoupStrainer
import sys, pathlib, urllib.parse

def main():
    if len(sys.argv) < 3:
        print("用法: python task4.py <input.html> <base_url>")
        sys.exit(1)

    file = pathlib.Path(sys.argv[1])
    base = sys.argv[2]

    only_img = SoupStrainer("img")
    with file.open("rb") as f:
        soup = BeautifulSoup(f, "html.parser", parse_only=only_img)

    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            full = urllib.parse.urljoin(base, src)
            alt = img.get("alt") or ""
            print(f"{full}\t{alt}")

if __name__ == "__main__":
    main()
