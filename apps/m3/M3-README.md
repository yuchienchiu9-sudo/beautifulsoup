### Milestone 3 – SoupReplacer API brief

## Overview
The Milestone 2 API exposed a simple mapping interface (`SoupReplacer(og_tag, alt_tag)`) that renamed tags during parsing. It was easy to use and safe, but limited to 1:1 name remapping.

## Milestone 3 extends this with transformer callables: `SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`.
- name_xformer(tag) -> str: compute a new `tag.name`.
- attrs_xformer(tag) -> dict: return replacement attributes.
- xformer(tag) -> None: arbitrary side-effects on the Tag object.

Recommendation
- Keep the simple (og, alt) constructor for common cases and backwards compatibility.
- Prefer the transformer API for power users who need context-sensitive changes (rename by tag, rewrite attributes, cleanup, enrichment).
- Apply `name_xformer` both pre-creation (to align start/end names) and post-creation (final authority), with post-creation taking precedence. This preserves correctness of stack operations while still allowing context-aware adjustments.
- Execute user transformers inside a best-effort guard to avoid breaking parsing if a transformer raises unexpectedly.

Pros vs Cons
- Pros: Expressive, single-pass transformation during parse, avoids extra tree walks, supports complex cleanup/enrichment.
- Cons: More surface for user errors; side effects can be surprising. To mitigate, scope changes to the current tag, and document best practices.

Usage Example
```
def remove_class(tag):
  tag.attrs.pop('class', None)

replacer = SoupReplacer(
  name_xformer=lambda t: 'blockquote' if t.name == 'b' else t.name,
  attrs_xformer=lambda t: {**t.attrs, **({'rel': ['noopener']} if t.name == 'a' else {})},
  xformer=remove_class,
)

soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
print(soup.prettify())
```
## Run & Verification (for TA)
  Environment
```bash
cd beautifulsoup
```
 
## Run Unit Tests
All six required test cases for the new SoupReplacer API are implemented in: `beautifulsoup/bs4/tests/test_replacer_m3.py`
To verify all new API behaviors:
```bash
python -m unittest bs4.tests.test_replacer_m3 -t . -v
```
## expect to see

test_1_name_xformer_simple (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_1_name_xformer_simple) ... ok
test_2_attrs_xformer_remove_class_and_style (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_2_attrs_xformer_remove_class_and_style) ... ok
test_3_xformer_side_effect_add_attr (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_3_xformer_side_effect_add_attr) ... ok
test_4_all_transformers_and_order (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_4_all_transformers_and_order) ... ok
test_5_legacy_pair_constructor_compat (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_5_legacy_pair_constructor_compat) ... ok
test_6_self_closing_tag_pre_post (bs4.tests.test_replacer_m3.TestSoupReplacerM3.test_6_self_closing_tag_pre_post) ... ok

## purpose
| # | Test              | What it checks                             | Expected result                                                         |
| - | ----------------- | ------------------------------------------ | ----------------------------------------------------------------------- |
| 1 | name_xformer      | Can rename tags (like `<b>` → `<strong>`)  | `<strong>` appears                                                      |
| 2 | attrs_xformer     | Can change or remove attributes            | `class` attribute removed                                               |
| 3 | xformer           | Can do side effects (like delete a tag)    | `<span>` is removed                                                     |
| 4 | all combined      | All 3 transformers work together           | `<b>` becomes `<blockquote>`, links add `rel=noopener`, no `class` left |
| 5 | backward compat   | Old `(og_tag, alt_tag)` syntax still works | `<b>` → `<blockquote>`                                                  |
| 6 | self-closing tags | Works on tags like `<img/>` too            | `<img alt="ok" src="x.png"/>`                                           |


Run Application Demo (Task 7)
To see a real HTML transformation using Wikipedia data:
```bash
python apps/m3/task7.py
```
Expected Output:
[OK] Wrote: D:\vscode\advanced programming\Milestone-3\beautifulsoup\apps\m3\task7-output.html
[Stats] blockquote tags: 803
[Stats] links with rel=noopener: 6151
[Stats] any element still has 'class'?: False


## Technical Brief – SoupReplacer (M2 vs M3)

In Milestone 2, `SoupReplacer(og_tag, alt_tag)` could only rename tags (e.g. `<b>` → `<blockquote>`).  
In Milestone 3, we extend it with three optional transformers:
- `name_xformer` – change tag names dynamically  
- `attrs_xformer` – modify or remove attributes  
- `xformer` – perform side effects on Tag objects  

This makes tag transformation more flexible and efficient because it happens **during parsing** instead of after building the tree.  
I recommend keeping the simple M2 API for quick use, but using M3’s transformer version for complex, context-aware editing.
