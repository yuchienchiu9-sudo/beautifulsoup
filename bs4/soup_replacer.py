# bs4/soup_replacer.py
class SoupReplacer:
    """During-parsing tag replacer: og_tag -> alt_tag."""
    def __init__(self, og_tag: str, alt_tag: str):
        self.og = (og_tag or "").strip().lower()
        self.alt = (alt_tag or "").strip().lower()

    def translate(self, tag_name: str) -> str:
        if not tag_name:
            return tag_name
        return self.alt if tag_name.lower() == self.og else tag_name
