"""
Cyber English AI Tutor - LLM Interface
支持 OpenAI、DeepSeek、通义千问 API，接口可替换。
无 API Key 时使用本地规则提供基础分析。
"""

import json
from typing import Optional
from core.config import Config


class LLMClient:
    """Unified LLM client supporting multiple providers."""

    def __init__(self, provider: str = ""):
        self._provider = provider.lower() if provider else Config.LLM_PROVIDER
        self._config = Config.get_active_provider_config()
        self._client = None
        self._setup_client()

    def _setup_client(self):
        """Initialize the OpenAI-compatible client."""
        api_key = self._config.get("api_key", "")
        if not api_key:
            self._client = None
            return

        try:
            from openai import OpenAI
            self._client = OpenAI(
                api_key=api_key,
                base_url=self._config.get("api_base", ""),
            )
        except ImportError:
            self._client = None

    @property
    def is_available(self) -> bool:
        """Check if LLM is available (API key configured)."""
        return self._client is not None and bool(self._config.get("api_key", ""))

    @property
    def provider(self) -> str:
        return self._provider

    def chat(self, messages: list[dict], temperature: float = 0.7) -> str:
        """
        Send a chat completion request.

        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Response creativity (0.0-1.0)

        Returns:
            Response text from the LLM
        """
        if not self.is_available:
            return "⚠️ LLM not available. Please configure your API key in .env file."

        try:
            response = self._client.chat.completions.create(
                model=self._config.get("model", "deepseek-chat"),
                messages=messages,
                temperature=temperature,
                max_tokens=2048,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"❌ API Error: {str(e)}"

    def analyze_word(self, word: str) -> str:
        """
        AI-powered word analysis.
        
        Returns detailed information about the word including:
        pronunciation, meaning, etymology, examples, usage tips.
        """
        if not self.is_available:
            return "⚠️ AI word analysis requires an API key. Configure in .env and restart."

        prompt = f"""You are an English teacher specializing in cybersecurity and technical English.

Please analyze the English word "{word}" and provide the following in Chinese-friendly format:

1. **Pronunciation** (IPA phonetics)
2. **Part of Speech**
3. **Chinese Meaning** (中文含义)
4. **English Definition** (英文解释)
5. **Word Root** (词根词缀分析)
6. **Example Sentence** (英文例句 + 中文翻译)
7. **Related Words** (相关词汇, 列出3-5个)
8. **Memory Tip** (记忆方法)
9. **CEFR Level** (A1-C2)

Format with clear markdown headers."""

        return self.chat([
            {"role": "system", "content": "You are a knowledgeable English tutor specializing in technical and cybersecurity English vocabulary."},
            {"role": "user", "content": prompt}
        ], temperature=0.3)

    def chat_tutor(self, user_message: str, history: list[dict], level: str = "Intermediate") -> str:
        """
        AI English tutor conversation.

        Args:
            user_message: The user's message in English
            history: Previous conversation history
            level: User's English level

        Returns:
            Tutor response with corrections and suggestions
        """
        if not self.is_available:
            return "⚠️ AI conversation requires an API key. Configure in .env and restart."

        system_prompt = f"""You are an AI English tutor. The user's English level is {level}.

Your teaching methodology:
1. First, gently correct any grammar or spelling mistakes in their message
2. Explain WHY it's wrong (grammar rule)
3. Offer a better/natural expression
4. End with a follow-up question to keep the conversation going

Keep responses encouraging and educational. When the user writes something, always provide:
- **Correction:** (if needed)
- **Explanation:** (why it's wrong)
- **Better Expression:** 
- **Follow-up Question:"""

        messages = [
            {"role": "system", "content": system_prompt},
        ]
        # Add history (last 10 messages)
        for msg in history[-10:]:
            messages.append(msg)
        messages.append({"role": "user", "content": user_message})

        return self.chat(messages, temperature=0.5)

    def analyze_sentence(self, sentence: str) -> str:
        """
        AI-powered sentence analysis.
        
        Analyzes grammar, vocabulary, difficulty, and suggests improvements.
        """
        if not self.is_available:
            return "⚠️ AI sentence analysis requires an API key. Configure in .env and restart."

        prompt = f"""Analyze this English sentence and provide:

Sentence: "{sentence}"

1. **Grammar Analysis** (grammar structures used, tenses, voice)
2. **Vocabulary Breakdown** (key words and their difficulty level)
3. **Difficulty Assessment** (A1-C2 level)
4. **Accuracy Score** (0-100)
5. **Better Expression** (a more natural or advanced version)
6. **Learning Tips** (what to focus on)

Format with clear markdown headers."""

        return self.chat([
            {"role": "system", "content": "You are an expert English grammar and writing analyst."},
            {"role": "user", "content": prompt}
        ], temperature=0.3)

    def analyze_article(self, article_text: str) -> str:
        """
        AI-powered article analysis.
        
        Provides summary, key vocabulary, grammar highlights, and learning suggestions.
        """
        if not self.is_available:
            return "⚠️ AI article analysis requires an API key. Configure in .env and restart."

        prompt = f"""Analyze this English article and provide a learning-oriented analysis:

Article:
\"\"\"
{article_text[:3000]}
\"\"\"

Please provide:
1. **Summary** (2-3 sentences in Chinese)
2. **Key Vocabulary** (important words with meanings)
3. **Grammar Highlights** (notable grammar structures)
4. **Reading Difficulty** (A1-C2 level)
5. **Learning Suggestions** (how to practice with this article)
6. **Discussion Questions** (2-3 questions to practice speaking)"""

        return self.chat([
            {"role": "system", "content": "You are an English reading tutor who helps students understand and learn from articles."},
            {"role": "user", "content": prompt}
        ], temperature=0.4)


# Singleton for reuse
_client_instance: Optional[LLMClient] = None


def get_llm_client(provider: str = "") -> LLMClient:
    """Get or create the LLM client singleton."""
    global _client_instance
    if _client_instance is None or (provider and provider != _client_instance.provider):
        _client_instance = LLMClient(provider)
    return _client_instance
