"""
Cyber English AI Tutor - Vocabulary Learning Module
支持本地词汇查询、收藏、标记已学、自动复习
"""

import streamlit as st
import pandas as pd
from core.i18n import t
from utils.text_analysis import lookup_word, search_words, get_categories, load_vocabulary
from utils.english_level import get_level_description

# NOTE: New i18n keys added — copy these to core/i18n.py DICT
# vocab_learned_label = {"en": "✅ Learned!", "zh": "✅ 已学!"}
# vocab_memory_tip_ai = {"en": "AI-powered memory tips will appear here once LLM is connected.", "zh": "AI记忆方法将在连接LLM后显示。"}
# vocab_col_word = {"en": "Word", "zh": "单词"}
# vocab_col_phonetic = {"en": "Phonetic", "zh": "音标"}
# vocab_col_meaning = {"en": "Meaning", "zh": "含义"}
# vocab_col_level = {"en": "Level", "zh": "等级"}
# vocab_col_category = {"en": "Category", "zh": "分类"}
# vocab_status_none = {"en": "—", "zh": "—"}
# vocab_showing_count = {"en": "Showing {} of {} words", "zh": "显示 {} / {} 个单词"}
# vocab_no_match = {"en": "No words found matching your filters.", "zh": "没有匹配筛选条件的单词。"}
# vocab_category_filter = {"en": "Category", "zh": "分类"}
# vocab_level_filter = {"en": "Level", "zh": "等级"}
# vocab_bookmarked_title = {"en": "Bookmarked Words", "zh": "已收藏的单词"}


def show():
    st.title(t("vocab_title"))
    st.markdown("---")

    # Initialize session state for bookmarks and learned words
    if "bookmarked_words" not in st.session_state:
        st.session_state.bookmarked_words = set()
    if "learned_words" not in st.session_state:
        st.session_state.learned_words = set()

    # ---- Tab layout ----
    tab1, tab2, tab3, tab4 = st.tabs([
        t("vocab_tab_lookup"), t("vocab_tab_browse"),
        t("vocab_tab_bookmarks"), t("vocab_tab_review")
    ])

    # ========== TAB 1: Look Up ==========
    with tab1:
        col_input, col_info = st.columns([1, 1])

        with col_input:
            word_input = st.text_input(
                t("vocab_enter_word"),
                placeholder=t("vocab_placeholder"),
                key="word_search_input"
            )

            if word_input:
                word_data = lookup_word(word_input)

                if word_data:
                    # Display word details
                    st.success(t("vocab_found_local"))

                    # Word header
                    st.markdown(f"## {word_data['word']}")
                    st.markdown(f"**{t('vocab_phonetic')}:** {word_data['phonetic']}")
                    st.markdown(f"**{t('vocab_pos')}:** {word_data['part_of_speech']}")

                    # Action buttons
                    col_b1, col_b2 = st.columns(2)
                    with col_b1:
                        if word_data["word"] not in st.session_state.learned_words:
                            if st.button(t("vocab_mark_learned"), key=f"learn_{word_data['word']}", use_container_width=True):
                                st.session_state.learned_words.add(word_data["word"])
                                st.rerun()
                        else:
                            st.success(t("vocab_learned_label"))
                    with col_b2:
                        if word_data["word"] not in st.session_state.bookmarked_words:
                            if st.button(t("vocab_bookmark"), key=f"bookmark_{word_data['word']}", use_container_width=True):
                                st.session_state.bookmarked_words.add(word_data["word"])
                                st.rerun()
                        else:
                            if st.button(t("vocab_bookmarked"), key=f"unbookmark_{word_data['word']}", use_container_width=True):
                                st.session_state.bookmarked_words.discard(word_data["word"])
                                st.rerun()

                else:
                    st.warning(f"'{word_input}' {t('vocab_not_found')}")
                    st.info(t("vocab_ai_hint"))

        with col_info:
            if word_input:
                word_data = lookup_word(word_input)
                if word_data:
                    with st.container(border=True):
                        st.markdown(f"### {t('vocab_details')}")

                        # Meaning
                        st.markdown(f"**{t('vocab_meaning')}:** {word_data['meaning']}")
                        st.markdown(f"**{t('vocab_level')}:** {word_data['level']}")
                        level_desc = get_level_description(word_data["level"])
                        if level_desc:
                            st.caption(level_desc)

                        # Category
                        st.markdown(f"**{t('vocab_category')}:** `{word_data['category']}`")

                        # Word Root
                        st.markdown(f"**{t('vocab_root')}:** {word_data['root']}")

                        # Example
                        st.markdown(f"**{t('vocab_example')}:**")
                        st.info(word_data["example"])

                        # Related Words
                        st.markdown(f"**{t('vocab_related')}:**")
                        related = word_data.get("related_words", [])
                        cols = st.columns(min(len(related), 4))
                        for i, rw in enumerate(related):
                            with cols[i % 4]:
                                if st.button(rw, key=f"related_{rw}", use_container_width=True):
                                    st.session_state.word_search_input = rw
                                    st.rerun()

                        # Memory tip placeholder
                        st.markdown(f"**{t('vocab_memory_tip')}:**")
                        st.caption(t("vocab_memory_tip_ai"))

    # ========== TAB 2: Browse All ==========
    with tab2:
        st.markdown(f"### {t('vocab_browse_title')}")

        col_filter1, col_filter2, col_filter3 = st.columns(3)
        with col_filter1:
            search_query = st.text_input(t("vocab_search"), placeholder=t("vocab_filter_placeholder"))
        with col_filter2:
            categories = [t("vocab_all")] + get_categories()
            cat_filter = st.selectbox(t("vocab_category_filter"), categories)
        with col_filter3:
            level_filter = st.selectbox(
                t("vocab_level_filter"),
                [t("vocab_all"), "CET4", "CET6", "IELTS", "TOEFL"]
            )

        df = load_vocabulary()

        # Apply filters
        if search_query:
            df = df[df["word"].str.contains(search_query, case=False, na=False) |
                     df["meaning"].str.contains(search_query, na=False)]
        if cat_filter != t("vocab_all"):
            df = df[df["category"] == cat_filter]
        if level_filter != t("vocab_all"):
            df = df[df["level"] == level_filter]

        # Display table
        if not df.empty:
            display_cols = ["word", "phonetic", "meaning", "level", "category"]
            display_df = df[display_cols].copy()
            display_df.columns = [
                t("vocab_col_word"), t("vocab_col_phonetic"),
                t("vocab_col_meaning"), t("vocab_col_level"),
                t("vocab_col_category")
            ]

            # Add status columns
            display_df[t("vocab_status")] = display_df[t("vocab_col_word")].apply(
                lambda w: t("vocab_learned_status") if w in st.session_state.learned_words
                else (t("vocab_bookmarked_status") if w in st.session_state.bookmarked_words else t("vocab_status_none"))
            )

            st.dataframe(display_df, use_container_width=True, hide_index=True)
            st.caption(t("vocab_showing_count").format(len(df), len(load_vocabulary())))
        else:
            st.info(t("vocab_no_match"))

    # ========== TAB 3: Bookmarks ==========
    with tab3:
        st.markdown(f"### {t('vocab_bookmarked_title')}")
        if st.session_state.bookmarked_words:
            for word in sorted(st.session_state.bookmarked_words):
                data = lookup_word(word)
                if data:
                    with st.container(border=True):
                        col_w1, col_w2, col_w3 = st.columns([2, 4, 1])
                        with col_w1:
                            st.markdown(f"**{word}**")
                            st.caption(data["phonetic"])
                        with col_w2:
                            st.markdown(f"*{data['meaning']}* — {data['level']}")
                        with col_w3:
                            if st.button(t("remove"), key=f"rm_bm_{word}"):
                                st.session_state.bookmarked_words.discard(word)
                                st.rerun()
        else:
            st.info(t("vocab_no_bookmarks"))

    # ========== TAB 4: Review ==========
    with tab4:
        st.markdown(f"### {t('vocab_review_title')}")
        if st.session_state.learned_words:
            st.markdown(t("vocab_learned_count").format(len(st.session_state.learned_words)))

            review_word = st.selectbox(
                t("vocab_select_review"),
                sorted(st.session_state.learned_words),
                key="review_select"
            )
            if review_word:
                data = lookup_word(review_word)
                if data:
                    with st.container(border=True):
                        st.markdown(f"### {data['word']}")
                        st.markdown(f"**{t('vocab_meaning')}:** {data['meaning']}")
                        st.markdown(f"**{t('vocab_phonetic')}:** {data['phonetic']}")
                        st.markdown(f"**{t('vocab_example')}:** {data['example']}")
                        st.caption(t("vocab_recall_hint"))
        else:
            st.info(t("vocab_no_learned"))


if __name__ == "__main__":
    show()
