"""
Cyber English AI Tutor - Database Module
SQLite-based user history, vocabulary tracking, and learning records.
"""

import sqlite3
import json
from datetime import datetime, date
from pathlib import Path
from typing import Optional
from core.config import Config


class Database:
    """SQLite database for user learning records."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or Config.DATABASE_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _get_conn(self):
        """Get a database connection."""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self):
        """Initialize database tables."""
        conn = self._get_conn()
        try:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS user_profile (
                    user_id INTEGER PRIMARY KEY DEFAULT 1,
                    english_level TEXT DEFAULT 'Intermediate',
                    grammar_errors TEXT DEFAULT '[]',
                    vocabulary_size INTEGER DEFAULT 0,
                    learning_history TEXT DEFAULT '[]',
                    interests TEXT DEFAULT '[]',
                    profession TEXT DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS vocabulary_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    status TEXT DEFAULT 'learning',
                    bookmarked INTEGER DEFAULT 0,
                    learned_at TIMESTAMP,
                    review_count INTEGER DEFAULT 0,
                    next_review TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(word)
                );

                CREATE TABLE IF NOT EXISTS conversation_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS learning_stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    words_learned INTEGER DEFAULT 0,
                    articles_read INTEGER DEFAULT 0,
                    conversation_minutes INTEGER DEFAULT 0,
                    sentences_analyzed INTEGER DEFAULT 0,
                    score INTEGER DEFAULT 0,
                    UNIQUE(date)
                );

                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    content TEXT NOT NULL,
                    difficulty TEXT DEFAULT 'Intermediate',
                    source TEXT DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                -- Ensure default user profile exists
                INSERT OR IGNORE INTO user_profile (user_id) VALUES (1);
            """)
            conn.commit()
        finally:
            conn.close()

    # ── User Profile ──

    def get_profile(self) -> dict:
        """Get user profile."""
        conn = self._get_conn()
        try:
            row = conn.execute("SELECT * FROM user_profile WHERE user_id = 1").fetchone()
            if row:
                return {
                    "english_level": row["english_level"],
                    "grammar_errors": json.loads(row["grammar_errors"]),
                    "vocabulary_size": row["vocabulary_size"],
                    "learning_history": json.loads(row["learning_history"]),
                    "interests": json.loads(row["interests"]),
                    "profession": row["profession"],
                }
            return {}
        finally:
            conn.close()

    def update_profile(self, **kwargs):
        """Update user profile fields."""
        allowed = ["english_level", "grammar_errors", "vocabulary_size", 
                   "learning_history", "interests", "profession"]
        updates = {k: v for k, v in kwargs.items() if k in allowed}
        if not updates:
            return
        for key in ["grammar_errors", "learning_history", "interests"]:
            if key in updates and isinstance(updates[key], (list, dict)):
                updates[key] = json.dumps(updates[key])
        updates["updated_at"] = datetime.now().isoformat()
        
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        values = list(updates.values()) + [1]
        
        conn = self._get_conn()
        try:
            conn.execute(f"UPDATE user_profile SET {set_clause} WHERE user_id = ?", values)
            conn.commit()
        finally:
            conn.close()

    # ── Vocabulary Records ──

    def add_vocabulary_record(self, word: str, status: str = "learning"):
        """Add or update a vocabulary record."""
        conn = self._get_conn()
        try:
            conn.execute(
                """INSERT INTO vocabulary_records (word, status, learned_at, next_review)
                   VALUES (?, ?, datetime('now'), datetime('now', '+1 day'))
                   ON CONFLICT(word) DO UPDATE SET status = excluded.status""",
                (word, status)
            )
            if status == "learned":
                conn.execute(
                    "UPDATE vocabulary_records SET learned_at = datetime('now') WHERE word = ?",
                    (word,)
                )
                # Update vocabulary size in profile
                count = conn.execute(
                    "SELECT COUNT(*) FROM vocabulary_records WHERE status = 'learned'"
                ).fetchone()[0]
                conn.execute(
                    "UPDATE user_profile SET vocabulary_size = ?, updated_at = datetime('now') WHERE user_id = 1",
                    (count,)
                )
            conn.commit()
        finally:
            conn.close()

    def toggle_bookmark(self, word: str) -> bool:
        """Toggle bookmark status. Returns new state."""
        conn = self._get_conn()
        try:
            current = conn.execute(
                "SELECT bookmarked FROM vocabulary_records WHERE word = ?", (word,)
            ).fetchone()
            if current:
                new_state = 0 if current["bookmarked"] else 1
                conn.execute(
                    "UPDATE vocabulary_records SET bookmarked = ? WHERE word = ?",
                    (new_state, word)
                )
            else:
                conn.execute(
                    "INSERT INTO vocabulary_records (word, bookmarked) VALUES (?, 1)",
                    (word,)
                )
                new_state = 1
            conn.commit()
            return bool(new_state)
        finally:
            conn.close()

    def get_learned_words(self) -> list[str]:
        """Get list of learned words."""
        conn = self._get_conn()
        try:
            rows = conn.execute(
                "SELECT word FROM vocabulary_records WHERE status = 'learned' ORDER BY word"
            ).fetchall()
            return [r["word"] for r in rows]
        finally:
            conn.close()

    def get_bookmarked_words(self) -> list[str]:
        """Get list of bookmarked words."""
        conn = self._get_conn()
        try:
            rows = conn.execute(
                "SELECT word FROM vocabulary_records WHERE bookmarked = 1 ORDER BY word"
            ).fetchall()
            return [r["word"] for r in rows]
        finally:
            conn.close()

    # ── Learning Stats ──

    def update_stats(self, date_str: str = "", words: int = 0, articles: int = 0,
                     conversation_min: int = 0, sentences: int = 0, score: int = 0):
        """Update daily learning statistics."""
        if not date_str:
            date_str = date.today().isoformat()
        
        conn = self._get_conn()
        try:
            conn.execute("""
                INSERT INTO learning_stats (date, words_learned, articles_read, 
                    conversation_minutes, sentences_analyzed, score)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(date) DO UPDATE SET
                    words_learned = words_learned + ?,
                    articles_read = articles_read + ?,
                    conversation_minutes = conversation_minutes + ?,
                    sentences_analyzed = sentences_analyzed + ?,
                    score = MAX(score, ?)
            """, (date_str, words, articles, conversation_min, sentences, score,
                  words, articles, conversation_min, sentences, score))
            conn.commit()
        finally:
            conn.close()

    def get_today_stats(self) -> dict:
        """Get today's learning statistics."""
        today = date.today().isoformat()
        conn = self._get_conn()
        try:
            row = conn.execute(
                "SELECT * FROM learning_stats WHERE date = ?", (today,)
            ).fetchone()
            if row:
                return {
                    "vocabulary": row["words_learned"],
                    "reading": row["articles_read"],
                    "conversation_minutes": row["conversation_minutes"],
                    "sentences": row["sentences_analyzed"],
                    "score": row["score"],
                }
            return {"vocabulary": 0, "reading": 0, "conversation_minutes": 0,
                    "sentences": 0, "score": 0}
        finally:
            conn.close()

    def get_weekly_stats(self) -> list[dict]:
        """Get last 7 days of learning stats."""
        conn = self._get_conn()
        try:
            rows = conn.execute("""
                SELECT * FROM learning_stats 
                WHERE date >= date('now', '-7 days')
                ORDER BY date
            """).fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()

    # ── Conversation History ──

    def save_conversation(self, session_id: str, role: str, content: str):
        """Save a conversation message."""
        conn = self._get_conn()
        try:
            conn.execute(
                "INSERT INTO conversation_history (session_id, role, content) VALUES (?, ?, ?)",
                (session_id, role, content)
            )
            conn.commit()
        finally:
            conn.close()

    # ── Articles ──

    def save_article(self, title: str, category: str, content: str, 
                     difficulty: str = "Intermediate", source: str = ""):
        """Save an article."""
        conn = self._get_conn()
        try:
            conn.execute(
                "INSERT INTO articles (title, category, content, difficulty, source) VALUES (?, ?, ?, ?, ?)",
                (title, category, content, difficulty, source)
            )
            conn.commit()
        finally:
            conn.close()

    def get_articles(self, category: str = "") -> list[dict]:
        """Get articles, optionally filtered by category."""
        conn = self._get_conn()
        try:
            if category:
                rows = conn.execute(
                    "SELECT * FROM articles WHERE category = ? ORDER BY created_at DESC",
                    (category,)
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM articles ORDER BY created_at DESC"
                ).fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()


# Singleton
_db_instance: Optional[Database] = None


def get_db() -> Database:
    """Get or create the database singleton."""
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance
