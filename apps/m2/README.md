## Part-1 
Task 2 — Extract all hyperlinks

    Open a terminal and navigate to the **beautifulsoup/apps/m2** directory:
    cd "Milestone-2\beautifulsoup\apps\m2"
    
    or (for your own test file): python task2.py <input.html or input.xml> <base_url> > links.txt(put the new test html or XML name to replace input.html or input.xml)
    

=================================================================================================

Task 3 — Extract all headings (h1–h6)

     (for your own test file): python task3.py <input.html or input.xml> > headings.txt (put the new test html or XMLname to replace input.html or input.xml)


=================================================================================================

Task 4 — Extract all images

    python task4.py "United States - Wikipedia.html" "https://en.wikipedia.org" > images.txt 
    (for your own test file) : python task4.py <input.html or input.xml> <base_url> > images.txt (put the new test html or XMLname to replace input.html or input.xml)

=================================================================================================
## Part-3 
Task 6 — SoupReplacer


    Run the program on an HTML file
    1.Open a terminal in: cd Milestone-2/beautifulsoup/apps/m2
    2. (for your own test file): python task6.py <input.html> (put the new test html or XMLname to replace input.html or input.xml)


    Expected output:
    [OK] Replaced <b> with <blockquote> during parsing
    [OK] Wrote -> D:\vscode\advanced programming\Milestone-2\beautifulsoup\apps\m2\United States - Wikipedia.b2blockquote.html

    Notes:On Windows, use UTF-8 mode to avoid encoding errors: python -X utf8 task6.py 