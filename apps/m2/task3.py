from bs4 import BeautifulSoup, SoupStrainer
import sys, pathlib

HEADINGS = ["h1","h2","h3","h4","h5","h6"]

def main():
    if len(sys.argv) < 2:
        print("用法: python task3.py <input.html>")
        sys.exit(1)

    file = pathlib.Path(sys.argv[1])
    only_headings = SoupStrainer(HEADINGS) 
    with file.open("rb") as f:
        soup = BeautifulSoup(f, "html.parser", parse_only=only_headings)

    n = 0
    for tag in soup.find_all(HEADINGS):
        text = " ".join(tag.get_text(strip=True).split())
        print(f"{tag.name.upper()}\t{text}")
        n += 1
    print(f"[INFO] total headings: {n}", file=sys.stderr)

if __name__ == "__main__":
    main()
