"""
Cyber English AI Tutor - Dashboard Module
首页展示学习统计信息，连接数据库
"""

import streamlit as st
from datetime import datetime
from core.database import get_db
from utils.text_analysis import load_vocabulary
from utils.english_level import get_level_description
from core.i18n import t

# NOTE: New i18n keys added — copy these to core/i18n.py DICT
# dash_learner: {"en": "Learner", "zh": "学习者"}
# dash_min: {"en": "min", "zh": "分钟"}
# dash_level_beginner: {"en": "Beginner (A1)", "zh": "初级 (A1)"}
# dash_level_elementary: {"en": "Elementary (A2)", "zh": "基础 (A2)"}
# dash_level_intermediate: {"en": "Intermediate (B1)", "zh": "中级 (B1)"}
# dash_level_upper_intermediate: {"en": "Upper Intermediate (B2)", "zh": "中高级 (B2)"}
# dash_level_advanced: {"en": "Advanced (C1)", "zh": "高级 (C1)"}
# dash_level_proficient: {"en": "Proficient (C2)", "zh": "精通 (C2)"}
# dash_interest_cybersecurity: {"en": "Cybersecurity", "zh": "网络安全"}
# dash_interest_technology: {"en": "Technology", "zh": "科技"}
# dash_interest_ai: {"en": "AI", "zh": "人工智能"}
# dash_interest_business: {"en": "Business", "zh": "商业"}
# dash_interest_science: {"en": "Science", "zh": "科学"}
# dash_interest_daily_news: {"en": "Daily News", "zh": "每日新闻"}
# dash_interest_finance: {"en": "Finance", "zh": "金融"}
# dash_interest_culture: {"en": "Culture", "zh": "文化"}


def show():
    st.title(t("dash_title"))
    st.markdown("---")

    db = get_db()
    profile = db.get_profile()
    today_stats = db.get_today_stats()

    # ── Welcome + Date ──
    col_w, col_d = st.columns([3, 1])
    with col_w:
        st.markdown(f"### 👋 {datetime.now().strftime('%A, %B %d, %Y')}")
    with col_d:
        profession = profile.get("profession", t("dash_learner"))
        st.markdown(f"### 🎯 {profession}")

    # ── Today's Stats ──
    st.markdown(f"### 📈 {t('dash_today')}")

    cols = st.columns(5)
    metrics = [
        (f"📖 {t('dash_words')}", today_stats.get("vocabulary", 0), 20),
        (f"📚 {t('dash_articles')}", today_stats.get("reading", 0), 3),
        (f"💬 {t('dash_speaking')}", f"{today_stats.get('conversation_minutes', 0)} {t('dash_min')}", f"15 {t('dash_min')}"),
        (f"✍️ {t('dash_sentences')}", today_stats.get("sentences", 0), 10),
        (f"🏆 {t('dash_score')}", f"{today_stats.get('score', 0)}", "100"),
    ]
    for col, label, value, goal in [(cols[i], *m) for i, m in enumerate(metrics)]:
        with col:
            st.container(border=True)
            st.metric(label=label, value=value)

    # ── Daily Progress ──
    st.markdown(f"### 🎯 {t('dash_daily_goals')}")
    pg1, pg2, pg3 = st.columns(3)

    with pg1:
        v = today_stats.get("vocabulary", 0) / 20
        st.markdown(f"**{t('dash_vocab_goal')}**")
        st.progress(min(v, 1.0), text=f"{today_stats.get('vocabulary', 0)}/20")
    with pg2:
        v = today_stats.get("reading", 0) / 3
        st.markdown(f"**{t('dash_reading_goal')}**")
        st.progress(min(v, 1.0), text=f"{today_stats.get('reading', 0)}/3")
    with pg3:
        v = today_stats.get("conversation_minutes", 0) / 15
        st.markdown(f"**{t('dash_conv_goal')}**")
        st.progress(min(v, 1.0), text=f"{today_stats.get('conversation_minutes', 0)}/15 {t('dash_min')}")

    # ── User Profile ──
    st.markdown("---")
    col_prof1, col_prof2 = st.columns(2)

    with col_prof1:
        st.markdown(f"### {t('dash_english_level')}")
        level = profile.get("english_level", "Intermediate (B1)")
        st.markdown(t("dash_current_level").format(level))
        st.caption(get_level_description(level))
        st.markdown(t("dash_vocab_size").format(profile.get("vocabulary_size", 0)))

        # Level selector
        levels = [
            "Beginner (A1)",
            "Elementary (A2)",
            "Intermediate (B1)",
            "Upper Intermediate (B2)",
            "Advanced (C1)",
            "Proficient (C2)",
        ]
        level_keys = [
            "dash_level_beginner",
            "dash_level_elementary",
            "dash_level_intermediate",
            "dash_level_upper_intermediate",
            "dash_level_advanced",
            "dash_level_proficient",
        ]
        level_labels = [t(k) for k in level_keys]

        idx = levels.index(level) if level in levels else 2
        selected_label = st.selectbox(
            t("dash_update_level"),
            level_labels,
            index=idx,
            key="level_selector",
        )
        selected_idx = level_labels.index(selected_label)
        new_level = levels[selected_idx]
        if new_level != level:
            db.update_profile(english_level=new_level)
            st.rerun()

    with col_prof2:
        st.markdown(f"### {t('dash_profile')}")
        new_profession = st.text_input(
            t("dash_profession"),
            value=profile.get("profession", ""),
            placeholder=t("dash_profession_placeholder"),
        )
        if new_profession != profile.get("profession", ""):
            db.update_profile(profession=new_profession)
            st.rerun()

        # Interests
        current_interests = profile.get("interests", [])
        interest_options = [
            ("Cybersecurity", "dash_interest_cybersecurity"),
            ("Technology", "dash_interest_technology"),
            ("AI", "dash_interest_ai"),
            ("Business", "dash_interest_business"),
            ("Science", "dash_interest_science"),
            ("Daily News", "dash_interest_daily_news"),
            ("Finance", "dash_interest_finance"),
            ("Culture", "dash_interest_culture"),
        ]
        interest_labels = [t(key) for _, key in interest_options]
        new_interests = st.multiselect(
            t("dash_interests"),
            interest_labels,
            default=current_interests,
        )
        if set(new_interests) != set(current_interests):
            # Map translated labels back to English values for storage
            label_to_value = dict(zip(interest_labels, [opt[0] for opt in interest_options]))
            english_interests = [label_to_value[label] for label in new_interests]
            db.update_profile(interests=english_interests)
            st.rerun()

    # ── Quick Start ──
    st.markdown("---")
    st.markdown(f"### {t('dash_quick_start')}")
    qcols = st.columns(4)
    pages = [
        (f"📖 {t('nav_vocabulary')}", "pages/vocabulary.py"),
        (f"💬 {t('nav_conversation')}", "pages/conversation.py"),
        (f"📚 {t('nav_reading')}", "pages/reading.py"),
        (f"✍️ {t('nav_sentence')}", "pages/sentence.py"),
    ]
    for col, (label, page) in zip(qcols, pages):
        with col:
            if st.button(label, use_container_width=True):
                st.switch_page(page)

    # ── Weekly Stats ──
    st.markdown("---")
    st.markdown(f"### {t('dash_this_week')}")
    weekly = db.get_weekly_stats()
    if weekly:
        days = {r["date"][-5:]: r["words_learned"] for r in weekly}
        st.bar_chart(days)
    else:
        st.info(t("dash_no_data"))

    # ── Today's Tasks ──
    st.markdown("---")
    st.markdown(f"### {t('dash_recommended')}")
    tasks = [
        ("📖", t("dash_task_vocab"), "vocabulary"),
        ("📚", t("dash_task_read"), "reading"),
        ("💬", t("dash_task_conv"), "conversation"),
        ("✍️", t("dash_task_sentence"), "sentence"),
    ]
    for icon, task, module in tasks:
        c1, c2 = st.columns([5, 1])
        with c1:
            st.checkbox(f"{icon} {task}", key=f"task_{module}")
        with c2:
            if st.button(t("go"), key=f"go_{module}"):
                st.switch_page(f"pages/{module}.py")


if __name__ == "__main__":
    show()
