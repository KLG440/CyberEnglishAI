"""
Cyber English AI Tutor - Sentence Analysis Module
Grammar checking, vocabulary breakdown, difficulty assessment, and improvement suggestions
"""


import streamlit as st
from core.llm import get_llm_client
from utils.english_level import assess_sentence_difficulty
from utils.text_analysis import lookup_word
from core.i18n import t


def show():
    st.title("✍️ Sentence Analysis")
    st.markdown("---")

    # ── Input ──
    sentence = st.text_area(
        "Enter an English sentence to analyze:",
        placeholder="e.g. The vulnerability was exploited by attackers.",
        height=120,
        key="sentence_input"
    )

    if sentence:
        col1, col2 = st.columns([3, 1])
        with col1:
            analyze_btn = st.button("🔍 Analyze Sentence", type="primary", use_container_width=True)
        with col2:
            if st.button("🔄 Try Example", use_container_width=True):
                st.session_state.sentence_input = "The vulnerability was exploited by attackers."
                st.rerun()

        if analyze_btn or st.session_state.get("auto_analyze"):
            st.session_state.auto_analyze = False

            with st.spinner("🔍 Analyzing sentence..."):
                # Try AI analysis first
                client = get_llm_client()
                if client.is_available:
                    ai_analysis = client.analyze_sentence(sentence)
                    st.markdown("### 🤖 AI Analysis")
                    st.markdown(ai_analysis)
                else:
                    # Offline analysis
                    show_offline_analysis(sentence)

                # Always show local vocabulary breakdown
                show_vocabulary_breakdown(sentence)

                # Track stats
                from core.database import get_db
                get_db().update_stats(sentences=1)
    else:
        # Show info when no input
        st.info("Enter a sentence above and click **Analyze Sentence** to get started!")

        with st.expander("💡 Try these example sentences:"):
            examples = [
                "Firewall protect computer from unauthorized access.",
                "The company implement new security measures last week.",
                "She have been working on the project for two months.",
                "Despite the complexity of the system, the team successfully completed the migration.",
                "If I would have known about the vulnerability, I would report it immediately.",
            ]
            for ex in examples:
                if st.button(ex, key=f"ex_{ex[:20]}", use_container_width=True):
                    st.session_state.sentence_input = ex
                    st.session_state.auto_analyze = True
                    st.rerun()


def show_offline_analysis(sentence: str):
    """Offline sentence analysis without AI."""
    import re

    st.markdown(f"### {t('sent_grammar_offline')}")

    # Basic analysis
    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence)
    
    analysis_findings = []

    # Check for basic grammar issues
    # 1. Subject-verb agreement
    for i, w in enumerate(words):
        w_lower = w.lower()
        if w_lower in ['he', 'she', 'it'] and i + 1 < len(words):
            next_w = words[i + 1].lower().strip('.,!?;"\'()')
            if next_w not in ['is', 'was', 'has', 'does', 'can', 'will', 'could', 
                            'would', 'should', 'may', 'might', 'must', 'had', 'did']:
                if not next_w.endswith('s'):
                    analysis_findings.append(t('sent_subject_verb_detail').format(w=w, next_w=next_w))
    
    # 2. Check for missing articles
    has_article = bool(re.search(r'\b(a|an|the)\b', sentence.lower()))
    # Check for singular countable nouns without articles
    singular_nouns = ['computer', 'system', 'network', 'program', 'project', 'report', 'user']
    for noun in singular_nouns:
        if noun in sentence.lower() and not has_article:
            analysis_findings.append(t('sent_missing_article').format(noun=noun))
            break
    
    # 3. Tense consistency
    if 'have' in sentence.lower() and 'ed' not in sentence.lower() and 'been' not in sentence.lower():
        analysis_findings.append(t('sent_tense_check'))
    
    # 4. Check for sentence fragments
    if word_count < 3:
        analysis_findings.append(t('sent_short_sentence'))

    # 5. Passive voice detection
    passive_pattern = re.search(r'\b(was|were|is|are|been|being)\s+\w+ed\b', sentence.lower())
    if passive_pattern:
        analysis_findings.append(t('sent_passive_voice'))

    if analysis_findings:
        for finding in analysis_findings:
            st.markdown(finding)
    else:
        st.markdown(t('sent_no_issues'))

    # Difficulty assessment
    difficulty = assess_sentence_difficulty(sentence)
    st.markdown(f"**{t('sent_difficulty')}:** `{difficulty}`")

    # Basic stats
    punct_count = sum(1 for c in sentence if c in ',;:')
    st.markdown(t('sent_stats_detail').format(
        word_count=word_count, char_count=char_count, punct_count=punct_count
    ))

    # Better expression suggestion (rule-based)
    st.markdown(f"### {t('sent_better')}")
    corrections = []
    
    # Passive to active suggestions
    if 'was exploited by' in sentence.lower():
        corrections.append(t('sent_active_exploited'))
    if 'was implemented by' in sentence.lower():
        corrections.append(t('sent_active_implemented'))
    
    if corrections:
        for c in corrections:
            st.markdown(c)
    else:
        st.markdown(t('sent_ai_offline'))


def show_vocabulary_breakdown(sentence: str):
    """Show vocabulary breakdown from local database."""
    import re
    
    words = re.findall(r'\b[a-zA-Z]{3,}\b', sentence.lower())
    unique_words = sorted(set(words))
    
    vocab_entries = []
    for w in unique_words:
        data = lookup_word(w)
        if data:
            vocab_entries.append(data)
    
    if vocab_entries:
        st.markdown("---")
        st.markdown(f"### {t('sent_vocab_in_sentence')}")
        
        for entry in vocab_entries:
            with st.container(border=True):
                col_v1, col_v2 = st.columns([1, 3])
                with col_v1:
                    st.markdown(f"**{entry['word']}**")
                    st.caption(entry['phonetic'])
                with col_v2:
                    st.markdown(f"*{entry['meaning']}* — `{entry['level']}`")
                    st.caption(entry['part_of_speech'])


if __name__ == "__main__":
    show()
