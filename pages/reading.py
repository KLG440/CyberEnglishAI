"""
Cyber English AI Tutor - Reading Module
Multi-domain articles with AI-powered reading assistance
"""

import streamlit as st
from core.database import get_db
from core.articles import get_articles as load_file_articles, get_categories_with_articles
from core.i18n import t
from utils.text_analysis import lookup_word
from core.llm import get_llm_client




def show():
    st.title(t("read_title"))
    st.markdown("---")

    db = get_db()

    # ── Category selector ──
    categories = ["All"] + get_categories_with_articles()

    col_cat, col_article = st.columns([1, 3])

    with col_cat:
        st.markdown(t("read_categories"))
        selected_category = st.radio(
            t("read_choose_category"),
            categories,
            index=0,
            label_visibility="collapsed"
        )

        # Refresh button
        if st.button(t("read_refresh"), use_container_width=True):
            st.rerun()

    with col_article:
        # Load articles
        articles = load_file_articles(category=selected_category)

        if not articles:
            st.info(t("read_no_articles").format(selected_category))
            st.markdown(f"""
            {t("read_tips_title")}

            {t("read_tip1")}
            {t("read_tip2")}
            {t("read_tip3")}
            {t("read_tip4")}
            """)
        else:
            # Article selector
            article_titles = [a["title"] for a in articles]
            selected_title = st.selectbox(
                t("read_select_article"),
                article_titles,
                label_visibility="collapsed"
            )

            article = next(a for a in articles if a["title"] == selected_title)

            # ── Display article ──
            st.markdown(f"## {article['title']}")
            col_meta1, col_meta2, col_meta3 = st.columns(3)
            with col_meta1:
                st.markdown(t("read_meta_category").format(article["category"]))
            with col_meta2:
                st.markdown(t("read_meta_difficulty").format(article["difficulty"]))
            with col_meta3:
                st.markdown(t("read_meta_date").format("📁"))

            st.markdown("---")

            # Article content (clickable words)
            content = article["content"]
            article_vocab = article.get("vocabulary", [])

            # Split into paragraphs
            paragraphs = content.split("\n\n")
            for para in paragraphs:
                st.markdown(para)

            # ── Key vocabulary buttons (from frontmatter) ──
            if article_vocab:
                st.markdown(f"### {t('read_key_vocab')}")
                cols = st.columns(min(len(article_vocab), 4))
                for i, vw in enumerate(article_vocab):
                    with cols[i % 4]:
                        btn_label = t("read_vocab_btn").format(vw)
                        if st.button(btn_label, key=f"vocab_{vw}_{article['title']}", use_container_width=True):
                            st.session_state["reading_vocab_popup"] = vw

            # ── Word popup ──
            if "reading_vocab_popup" in st.session_state:
                popup_word = st.session_state.reading_vocab_popup
                word_data = lookup_word(popup_word)
                if word_data:
                    with st.expander(t("read_vocab_btn").format(popup_word), expanded=True):
                        col_w1, col_w2 = st.columns([2, 1])
                        with col_w1:
                            st.markdown(f"**{word_data['word']}**  {word_data['phonetic']}")
                            st.markdown(f"*{word_data['meaning']}* ({word_data['part_of_speech']})")
                            st.markdown(f"**{t('read_word_example')}:** {word_data['example']}")
                        with col_w2:
                            st.markdown(f"**{t('read_word_level')}:** {word_data['level']}")
                            st.markdown(f"**{t('read_word_category')}:** {word_data['category']}")
                        if st.button(t("close"), key="close_vocab_popup"):
                            del st.session_state.reading_vocab_popup
                            st.rerun()
                else:
                    with st.expander(t("read_vocab_btn").format(popup_word), expanded=True):
                        st.info(t("read_vocab_no_api").format(popup_word))
                        if st.button(t("close"), key="close_vocab_popup2"):
                            del st.session_state.reading_vocab_popup
                            st.rerun()

            # ── AI Analysis button ──
            st.markdown("---")
            col_ai1, col_ai2 = st.columns([1, 3])
            with col_ai1:
                if st.button(t("read_ai_analysis"), use_container_width=True, type="primary"):
                    with st.spinner(t("read_analyzing")):
                        client = get_llm_client()
                        if client.is_available:
                            analysis = client.analyze_article(content)
                        else:
                            analysis = get_offline_article_analysis(content)
                    st.session_state["article_analysis"] = analysis

            with col_ai2:
                if st.button(t("read_mark_read"), use_container_width=True):
                    db.update_stats(articles=1)
                    st.success(t("read_marked"))

            # Display analysis
            if "article_analysis" in st.session_state:
                with st.expander(t("read_ai_analysis_title"), expanded=True):
                    st.markdown(st.session_state.article_analysis)
                    if st.button(t("read_clear_analysis")):
                        del st.session_state["article_analysis"]
                        st.rerun()

            # ── Reading progress ──
            st.markdown("---")
            st.markdown(t("read_progress"))
            today_stats = db.get_today_stats()
            st.progress(
                min(today_stats.get("reading", 0) / 3, 1.0),
                text=t("read_today_progress").format(today_stats.get("reading", 0))
            )


def get_offline_article_analysis(content: str) -> str:
    """Generate basic article analysis without AI."""
    import re

    words = re.findall(r'\b[a-zA-Z]{3,}\b', content)
    unique_words = set(w.lower() for w in words)
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    analysis = f"""{t("read_offline_title")}

{t("read_offline_summary")}
{t("read_offline_stats").format(len(words), len(unique_words))}

{t("read_offline_vocab")}
"""
    # Find vocabulary words that are in our database
    from utils.text_analysis import lookup_word
    vocab_found = []
    for w in sorted(unique_words):
        data = lookup_word(w)
        if data:
            vocab_found.append(f"- **{w}**: {data['meaning']} ({data['level']})")

    if vocab_found:
        analysis += "\n".join(vocab_found[:10])
    else:
        analysis += t("read_offline_no_api")

    avg_words = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
    if avg_words < 10:
        difficulty = t("read_level_beginner")
    elif avg_words < 18:
        difficulty = t("read_level_intermediate")
    else:
        difficulty = t("read_level_advanced")
    avg_len_str = t("read_offline_avg_len").format(f"{avg_words:.0f}")

    analysis += f"""
{t("read_offline_difficulty").format(difficulty)}
{t("read_offline_sent_count").format(len(sentences))}
{avg_len_str}

{t("read_offline_suggestions")}
{t("read_offline_sug1")}
{t("read_offline_sug2")}
{t("read_offline_sug3")}
{t("read_offline_sug4")}

{t("read_offline_api_hint")}
"""
    return analysis


if __name__ == "__main__":
    show()
