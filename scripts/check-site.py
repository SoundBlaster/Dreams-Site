#!/usr/bin/env python3
"""Dependency-free structure/link check; does not claim visual or hosting validation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "website"

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.languages = set()
        self.title = False
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.title = True
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport = True
        if "data-language" in attrs:
            self.languages.add(attrs["data-language"])
        for name in ("href", "src"):
            if name in attrs:
                self.links.append(attrs[name])

pages = sorted((ROOT / "dreams").rglob("*.html"))
assert len(pages) == 3, "Expected landing, support and privacy pages"
for path in pages:
    parsed = Page()
    parsed.feed(path.read_text())
    assert parsed.title and parsed.viewport, f"Missing title/viewport: {path}"
    assert parsed.languages == {"en", "ru"}, f"Missing translation: {path}"
    for link in parsed.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (ROOT / unquote(url.path.lstrip("/")) if url.path.startswith("/")
                  else path.parent / unquote(url.path)).resolve()
        assert target.is_relative_to(ROOT.resolve()), f"Link leaves website: {link}"
        if target.is_dir():
            target = target / "index.html"
        assert target.is_file(), f"Broken local link in {path}: {link}"
print(f"PASS: {len(pages)} EN/RU pages, titles, viewports and local links")
