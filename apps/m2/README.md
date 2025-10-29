# Milestone-2

---

## Part-1 
### Task 2 — Extract all hyperlinks
Open a terminal and navigate to the **beautifulsoup/apps/m2** directory:

```bash
cd "Milestone-2\beautifulsoup\apps\m2"
python task2.py <input.html or input.xml> <base_url> > links.txt
```
(for your own test file: replace <input.html> or <input.xml> with your file name)

### Task 3 — Extract all headings (h1–h6)
```bash
python task3.py <input.html or input.xml> > headings.txt
```
### Task 4 — Extract all images
```bash
python task4.py "United States - Wikipedia.html" "https://en.wikipedia.org" > images.txt
# or (for your own test file)
python task4.py <input.html or input.xml> <base_url> > images.txt
```
(for your own test file: replace <input.html> or <input.xml> with your file name)

## Part-2
API Definition Map (BeautifulSoup Original Source)

All file paths and line numbers refer to the unmodified source from the provided beautifulsoup.zip.

BeautifulSoup version (from bs4/__init__.py): 4.13.0

Each line number is the first line of the class/function definition.
| API used               | Defined in (file) | Line #               | Description                                                   |
| ---------------------- | ----------------- | -------------------- | ------------------------------------------------------------- |
| `BeautifulSoup()`      | bs4/**init**.py   | 133                  | `class BeautifulSoup` constructor                             |
| `SoupStrainer()`       | bs4/filter.py     | 313                  | parsing filter for selective parsing                          |
| `find()`               | bs4/element.py    | 2684                 | `Tag.find` method                                             |
| `find_all()`           | bs4/element.py    | 2715                 | `Tag.find_all` method                                         |
| `select()`             | bs4/element.py    | 160                  | `Tag.select` (CSS selector via soupsieve)                     |
| `select_one()`         | bs4/element.py    | 178                  | `Tag.select_one` (single element via CSS selector)            |
| `get_text()`           | bs4/element.py    | 524                  | `Tag.get_text` extracts text from tags                        |
| `__getitem__()`        | bs4/element.py    | 2203                 | `Tag.__getitem__` enables attribute access like `tag['href']` |
| `get()`                | bs4/element.py    | 2160                 | `Tag.get` safely retrieves attribute values                   |
| `find_parent()`        | bs4/element.py    | 992                  | `Tag.find_parent` finds closest parent tag                    |
| `find_next_siblings()` | bs4/element.py    | 827                  | `Tag.find_next_siblings` retrieves following siblings         |
| `has_attr()`           | bs4/element.py    | 2196                 | `Tag.has_attr` checks if tag has a given attribute            |
| `prettify()`           | bs4/element.py    | 2601                 | pretty-printing of HTML/XML tree                              |
| `tag.name / tag.attrs` | bs4/element.py    | *(within Tag class)* | tag metadata properties (element name, attributes)            |
Notes

select() and select_one() are also imported from bs4/css.py, but the main public API used by BeautifulSoup is implemented in bs4/element.py.

All line numbers are based on the unmodified BeautifulSoup v4.13.0 source code.

## Part-3
### Task 6 — SoupReplacer

Run the program on an HTML file:
```bash
cd Milestone-2/beautifulsoup/apps/m2
python task6.py <input.html>
```
Notes:
On Windows, use UTF-8 mode to avoid encoding errors:
python -X utf8 task6.py
