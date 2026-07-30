"""
Cyber English AI Tutor - Configuration Module
Loads settings from: Streamlit secrets > .env file > environment variables
"""

import os
from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# ── Helper: resolve a config value from multiple sources ──
def _get_config(key: str, default: str = "") -> str:
    """
    Resolve configuration value with priority:
    1. Streamlit secrets (when deployed on Streamlit Cloud)
    2. Environment variables
    3. .env file (local development fallback)
    """
    # Try Streamlit secrets first (only available during streamlit run)
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            try:
                if key in st.secrets:
                    return st.secrets[key]
            except Exception:
                pass
    except (ImportError, RuntimeError):
        pass

    # Try environment variable
    val = os.getenv(key)
    if val:
        return val

    # Try .env file
    dotenv_path = ROOT_DIR / ".env"
    if dotenv_path.exists():
        with open(dotenv_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == key:
                        return v.strip().strip("\"'")

    return default


class Config:
    # LLM Provider
    LLM_PROVIDER = _get_config("LLM_PROVIDER", "deepseek")

    # OpenAI
    OPENAI_API_KEY = _get_config("OPENAI_API_KEY", "")
    OPENAI_API_BASE = _get_config("OPENAI_API_BASE", "https://api.openai.com/v1")
    OPENAI_MODEL = _get_config("OPENAI_MODEL", "gpt-4o-mini")

    # DeepSeek
    DEEPSEEK_API_KEY = _get_config("DEEPSEEK_API_KEY", "")
    DEEPSEEK_API_BASE = _get_config("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
    DEEPSEEK_MODEL = _get_config("DEEPSEEK_MODEL", "deepseek-chat")

    # Qwen
    QWEN_API_KEY = _get_config("QWEN_API_KEY", "")
    QWEN_API_BASE = _get_config("QWEN_API_BASE", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    QWEN_MODEL = _get_config("QWEN_MODEL", "qwen-plus")

    # Database
    DATABASE_PATH = ROOT_DIR / "data" / "user_history.db"

    # Default English level
    DEFAULT_LEVEL = "Intermediate"

    @classmethod
    def get_active_provider_config(cls) -> dict:
        provider = cls.LLM_PROVIDER.lower()
        configs = {
            "openai": {
                "api_key": cls.OPENAI_API_KEY,
                "api_base": cls.OPENAI_API_BASE,
                "model": cls.OPENAI_MODEL,
            },
            "deepseek": {
                "api_key": cls.DEEPSEEK_API_KEY,
                "api_base": cls.DEEPSEEK_API_BASE,
                "model": cls.DEEPSEEK_MODEL,
            },
            "qwen": {
                "api_key": cls.QWEN_API_KEY,
                "api_base": cls.QWEN_API_BASE,
                "model": cls.QWEN_MODEL,
            },
        }
        return configs.get(provider, configs["deepseek"])
