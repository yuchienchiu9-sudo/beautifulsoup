# beautifulsoup/bs4/soup_replacer.py
from typing import Callable, Optional, Mapping, Tuple, Any, Dict

class SoupReplacer:
  
    def __init__(self, *args,
                 name_xformer: Optional[Callable[[Any], str]] = None,
                 attrs_xformer: Optional[Callable[[Any], Mapping]] = None,
                 xformer: Optional[Callable[[Any], None]] = None):
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

        # Back-compat: SoupReplacer("old", "new")
        self._pair_og = None
        self._pair_alt = None
        if len(args) == 2 and all(isinstance(a, str) for a in args):
            og, alt = args
            self._pair_og = (og or "").strip().lower()
            self._pair_alt = (alt or "").strip().lower()

            
            if self.name_xformer is None:
                def _nx(tag):
                    name = getattr(tag, "name", None)
                    if not name:
                        return name
                    return self._pair_alt if name.lower() == self._pair_og else name
                self.name_xformer = _nx
        elif len(args) != 0:
            raise TypeError("Invalid positional args. Use (old, new) or keyword transformers.")

    # ======= M3: pre/post hooks =======

    def transform_name_attrs(self, name: str, attrs: Mapping) -> Tuple[str, Mapping]:
        
        fake = _FakeTag(name, dict(attrs))
        new_name = self.name_xformer(fake) if self.name_xformer else name
        new_attrs = self.attrs_xformer(fake) if self.attrs_xformer else attrs
        return new_name, new_attrs

    def transform_tag(self, tag_obj) -> None:
        
        if self.xformer:
            self.xformer(tag_obj)

    # ======= M2: legacy API (for compatibility with old builder wiring) =======

    def translate(self, tag_name: str) -> str:
        
        if not tag_name:
            return tag_name
        if self.name_xformer is not None:
            return self.name_xformer(_FakeTag(tag_name, {}))  
        if self._pair_og is not None:
            return self._pair_alt if tag_name.strip().lower() == self._pair_og else tag_name
        return tag_name


class _FakeTag:

    def __init__(self, name: str, attrs: Dict):
        self.name = name
        self.attrs = attrs
