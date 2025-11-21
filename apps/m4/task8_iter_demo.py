import sys
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) < 2:
        print("Usage: python task8_iter_demo.py <input.html>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    for node in soup:
        print(repr(node))


if __name__ == "__main__":
    main()
