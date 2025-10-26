# BeautifulSoup (Milestone-2 Extension)

Adds **SoupReplacer(og_tag, alt_tag)** to BeautifulSoup so tag replacement happens **during parsing**.

## 1) Installation & Environment
- Requires **Python 3.8+** and **git**.
- Use the **local** `bs4` under this repo; **不要** `pip install beautifulsoup4`.

### Get the code
#### A. 你要把現有作業資料夾上傳到 GitHub
```bash
cd "<path-to>/Milestone-2"      # 進入 Milestone-2 根目錄
git init
git add .
git commit -m "M2: add SoupReplacer, tests, and task6 app"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main


if already have GitHub repo then
cd "<path-to>/Milestone-2"
git checkout -b m2-soupreplacer
git add beautifulsoup/bs4/__init__.py beautifulsoup/test/*.py beautifulsoup/apps/m2/task6.py apps/m2/M2-README.md beautifulsoup/README.md
git commit -m "Add SoupReplacer + tests + task6"
git push -u origin m2-soupreplacer



Test the new API (unit tests)

first go to milestone-2 than try below cpde
python -X utf8 beautifulsoup/test/testsample1.py
python -X utf8 beautifulsoup/test/testsample2.py
