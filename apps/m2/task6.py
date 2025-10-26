import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "beautifulsoup"))
try:
    from bs4 import BeautifulSoup, SoupReplacer
except ImportError:
    print("Error: local BeautifulSoup not found (bs4). Check sys.path injection.")
    sys.exit(1)

def pick_parser(p: Path) -> str:
    return "xml" if p.suffix.lower() == ".xml" else "html.parser"

def main():
   
    args = sys.argv[1:]
    if not args:
        print("Usage: python task6.py <input.html|input.xml> [og_tag alt_tag] [-o out.html] [--stdout]")
        sys.exit(2)

    
    in_path = Path(args[0]); args = args[1:]
    if not in_path.exists():
        print(f"Error: file not found -> {in_path}")
        sys.exit(3)

 
    if len(args) >= 2 and not args[0].startswith('-') and not args[1].startswith('-'):
        og_tag, alt_tag = args[0], args[1]
        args = args[2:]
    else:
        og_tag, alt_tag = "b", "blockquote"

    out_to_stdout = False
    out_path = None
    i = 0
    while i < len(args):
        if args[i] in ("-o", "--out"):
            if i + 1 >= len(args):
                print("Error: -o/--out requires a filename")
                sys.exit(4)
            out_path = Path(args[i+1])
            i += 2
        elif args[i] == "--stdout":
            out_to_stdout = True
            i += 1
        else:
            print(f"Unknown option: {args[i]}")
            sys.exit(2)

    html = in_path.read_text(encoding="utf-8", errors="ignore")

    replacer = SoupReplacer(og_tag, alt_tag)
    soup = BeautifulSoup(html, features=pick_parser(in_path), replacer=replacer)
    rendered = soup.prettify()

    if out_to_stdout:
        
        sys.stdout.write(rendered)
    else:
        if out_path is None:
    
            out_path = in_path.with_suffix(f".{og_tag}2{alt_tag}.html")
        out_path.write_text(rendered, encoding="utf-8")
        print(f"[OK] Replaced <{og_tag}> with <{alt_tag}> during parsing")
        print(f"[OK] Wrote -> {out_path.resolve()}")

if __name__ == "__main__":
    main()
