"""
Cyber English AI Tutor - English Level Assessment Utilities
"""


# Common vocabulary sizes by CEFR level
CEFR_VOCABULARY_SIZE = {
    "A1 (Beginner)": 500,
    "A2 (Elementary)": 1000,
    "B1 (Intermediate)": 2000,
    "B2 (Upper Intermediate)": 4000,
    "C1 (Advanced)": 8000,
    "C2 (Proficient)": 16000,
}

# Chinese education system mapping
CHINESE_LEVEL_MAP = {
    "CET4": "B1 (Intermediate)",
    "CET6": "B2 (Upper Intermediate)",
    "TEM4": "B2 (Upper Intermediate)",
    "TEM8": "C1 (Advanced)",
    "IELTS 5.0": "B1 (Intermediate)",
    "IELTS 6.0": "B2 (Upper Intermediate)",
    "IELTS 7.0": "C1 (Advanced)",
    "TOEFL 80": "B2 (Upper Intermediate)",
    "TOEFL 100": "C1 (Advanced)",
}


def estimate_level(known_words_count: int) -> str:
    """Estimate English level based on known vocabulary size."""
    if known_words_count < 500:
        return "A1 (Beginner)"
    elif known_words_count < 1000:
        return "A2 (Elementary)"
    elif known_words_count < 2000:
        return "B1 (Intermediate)"
    elif known_words_count < 4000:
        return "B2 (Upper Intermediate)"
    elif known_words_count < 8000:
        return "C1 (Advanced)"
    else:
        return "C2 (Proficient)"


def get_level_description(level: str) -> str:
    """Get description of a CEFR level."""
    descriptions = {
        "A1 (Beginner)": "Can understand and use familiar everyday expressions.",
        "A2 (Elementary)": "Can communicate in simple, routine tasks.",
        "B1 (Intermediate)": "Can deal with most situations while traveling.",
        "B2 (Upper Intermediate)": "Can interact with a degree of fluency.",
        "C1 (Advanced)": "Can express ideas fluently and spontaneously.",
        "C2 (Proficient)": "Can understand virtually everything heard or read.",
    }
    return descriptions.get(level, "")


def assess_sentence_difficulty(sentence: str) -> str:
    """Roughly assess sentence difficulty by length and word complexity."""
    words = sentence.split()
    word_count = len(words)
    
    # Simple heuristic
    long_words = sum(1 for w in words if len(w) > 8)
    
    if word_count < 5 and long_words == 0:
        return "A1 (Beginner)"
    elif word_count < 10 and long_words <= 1:
        return "A2 (Elementary)"
    elif word_count < 20 and long_words <= 3:
        return "B1 (Intermediate)"
    elif word_count < 30 and long_words <= 5:
        return "B2 (Upper Intermediate)"
    else:
        return "C1 (Advanced)"
