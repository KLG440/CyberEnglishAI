"""
Cyber English AI Tutor
Main entry point — bilingual (中文/English).
"""

import streamlit as st
from core.i18n import t, lang_selector

st.set_page_config(
    page_title="Cyber English AI Tutor",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -- Sidebar --
with st.sidebar:
    st.markdown("# 🌐 Cyber English AI Tutor")
    
    # Language selector at top
    lang_selector()
    st.markdown("---")
    
    nav_label = t("nav_modules")
    st.markdown(f"### {nav_label}")
    
    st.page_link("app.py", label=t("nav_home"), icon="🏠")
    st.page_link("pages/dashboard.py", label=t("nav_dashboard"), icon="📊")
    st.page_link("pages/vocabulary.py", label=t("nav_vocabulary"), icon="📖")
    st.page_link("pages/conversation.py", label=t("nav_conversation"), icon="💬")
    st.page_link("pages/reading.py", label=t("nav_reading"), icon="📚")
    st.page_link("pages/sentence.py", label=t("nav_sentence"), icon="✍️")
    
    st.markdown("---")
    st.caption(t("nav_version"))


def main():
    st.title(t("home_title"))
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(t("home_welcome"))
        st.markdown(t("home_module_header"))
        
        st.markdown(f"""
        | {t('nav_dashboard')} | {t('home_module_desc_dashboard')} |
        | {t('nav_vocabulary')} | {t('home_module_desc_vocab')} |
        | {t('nav_conversation')} | {t('home_module_desc_conv')} |
        | {t('nav_reading')} | {t('home_module_desc_read')} |
        | {t('nav_sentence')} | {t('home_module_desc_sentence')} |
        """)
    
    with col2:
        st.container(border=True)
        st.markdown(t("home_quick_stats"))
        st.markdown(t("home_words_learned"))
        st.markdown(t("home_articles_read"))
        st.markdown(t("home_conversations"))
        st.markdown(t("home_current_level"))
        
        st.markdown("---")
        st.markdown(t("home_getting_started"))
        st.markdown(t("home_gs_step1"))
        st.markdown(t("home_gs_step2"))
        st.markdown(t("home_gs_step3"))
    
    st.markdown("---")
    st.info(t("home_sidebar_hint"))


if __name__ == "__main__":
    main()
