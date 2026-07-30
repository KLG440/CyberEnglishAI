"""
Cyber English AI Tutor - Text Analysis Utilities
"""

import re
import pandas as pd
from pathlib import Path


# Load vocabulary data
DATA_DIR = Path(__file__).parent.parent / "data"
VOCAB_PATH = DATA_DIR / "vocabulary.csv"

_vocab_df = None


def load_vocabulary() -> pd.DataFrame:
    """Load vocabulary from CSV file."""
    global _vocab_df
    if _vocab_df is not None:
        return _vocab_df
    
    if VOCAB_PATH.exists():
        _vocab_df = pd.read_csv(VOCAB_PATH)
    else:
        _vocab_df = pd.DataFrame(columns=[
            "word", "phonetic", "meaning", "level", "category",
            "example", "related_words", "part_of_speech", "root"
        ])
    return _vocab_df


def lookup_word(word: str) -> dict | None:
    """
    Look up a word in the local vocabulary database.
    Returns word data dict or None if not found.
    """
    df = load_vocabulary()
    if df.empty:
        return None
    
    word = word.strip().lower()
    match = df[df["word"].str.lower() == word]
    
    if not match.empty:
        row = match.iloc[0]
        return {
            "word": row["word"],
            "phonetic": row["phonetic"],
            "meaning": row["meaning"],
            "level": row["level"],
            "category": row["category"],
            "example": row["example"],
            "related_words": [w.strip() for w in str(row["related_words"]).split(",")],
            "part_of_speech": row["part_of_speech"],
            "root": row["root"],
            "source": "local"
        }
    return None


def search_words(query: str = "", category: str = "", level: str = "") -> pd.DataFrame:
    """Search vocabulary by query, category, or level."""
    df = load_vocabulary()
    if query:
        df = df[df["word"].str.contains(query, case=False, na=False)]
    if category:
        df = df[df["category"].str.contains(category, case=False, na=False)]
    if level:
        df = df[df["level"].str.contains(level, case=False, na=False)]
    return df


def extract_vocabulary_from_text(text: str) -> list[str]:
    """Extract potential vocabulary words from text."""
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
    return list(set(w.lower() for w in words))


def get_categories() -> list[str]:
    """Get unique vocabulary categories."""
    df = load_vocabulary()
    if df.empty:
        return []
    return sorted(df["category"].unique().tolist())
