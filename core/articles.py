"""
Cyber English AI Tutor - Articles Module
Loads articles from markdown files in data/articles/<category>/.
File-based storage ensures articles persist across Streamlit Cloud redeploys.
"""

import re
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"

CATEGORIES = [
    "Daily News", "Technology", "AI", "Cybersecurity",
    "Business", "Science", "Finance", "Culture",
]

_articles_cache = None


def parse_article_md(content: str, path: Path) -> dict | None:
    """Parse a markdown article file with YAML-like frontmatter."""
    # Frontmatter: ---\nkey: value\n---\ncontent
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not m:
        return None

    meta_text, body = m.groups()
    meta = {}
    for line in meta_text.strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip().strip('"').strip("'")

    title = meta.get("title", path.stem.replace("-", " ").title())
    category = meta.get("category", "General")
    difficulty = meta.get("difficulty", "Intermediate")

    # Extract key vocabulary section
    vocab = []
    vocab_match = re.search(r"Key vocabulary:\s*(.+)", body, re.IGNORECASE)
    if vocab_match:
        vocab = [v.strip() for v in vocab_match.group(1).split(",") if v.strip()]
        # Remove the key vocabulary line from body
        body = re.sub(r"(?m)^Key vocabulary:.*$", "", body)

    return {
        "title": title,
        "category": category,
        "difficulty": difficulty,
        "content": body.strip(),
        "vocabulary": vocab,
        "source": "file",
    }


def load_articles() -> list[dict]:
    """Load all articles from files, organized by category."""
    global _articles_cache
    if _articles_cache is not None:
        return _articles_cache

    articles = []
    if ARTICLES_DIR.exists():
        for md_file in sorted(ARTICLES_DIR.rglob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8")
                article = parse_article_md(content, md_file)
                if article:
                    articles.append(article)
            except Exception:
                continue

    _articles_cache = articles
    return articles


def get_articles(category: str = "") -> list[dict]:
    """Get articles, optionally filtered by category."""
    articles = load_articles()
    if category and category != "All":
        return [a for a in articles if a["category"] == category]
    return articles


def get_categories_with_articles() -> list[str]:
    """Get categories that actually have articles."""
    articles = load_articles()
    cats = sorted(set(a["category"] for a in articles))
    return cats if cats else CATEGORIES
