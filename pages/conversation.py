"""
Cyber English AI Tutor - AI Conversation Module
支持与 AI 英语老师进行对话练习，包含纠错、语法解释、难度自适应
"""

import streamlit as st
from core.llm import get_llm_client
from core.i18n import t


def show():
    st.title(t("conv_title"))
    st.markdown("---")

    # Initialize session state for conversation
    if "conversation_messages" not in st.session_state:
        st.session_state.conversation_messages = [
            {"role": "assistant", "content": t("conv_initial_message")}
        ]
    if "conversation_level" not in st.session_state:
        st.session_state.conversation_level = "Intermediate"
    if "conversation_count" not in st.session_state:
        st.session_state.conversation_count = 0

    st.markdown(t("conv_current_level").format(st.session_state.conversation_level))

    # ---- Level selector ----
    col_l1, col_l2, col_l3 = st.columns([2, 2, 2])
    with col_l1:
        new_level = st.selectbox(
            t("conv_adjust_level"),
            options=["Beginner (A1)", "Elementary (A2)", "Intermediate (B1)", 
                     "Upper Intermediate (B2)", "Advanced (C1)", "Proficient (C2)"],
            index=2
        )
        if new_level != st.session_state.conversation_level:
            st.session_state.conversation_level = new_level
            st.rerun()

    with col_l2:
        st.markdown(t("conv_session_stats"))
        st.markdown(t("conv_messages").format(st.session_state.conversation_count))
        
    with col_l3:
        if st.button(t("conv_clear"), use_container_width=True):
            st.session_state.conversation_messages = [
                {"role": "assistant", "content": t("conv_cleared")}
            ]
            st.session_state.conversation_count = 0
            st.rerun()

    # ---- Chat display ----
    chat_container = st.container(border=True, height=450)

    with chat_container:
        for msg in st.session_state.conversation_messages:
            if msg["role"] == "user":
                st.markdown(f"**{t('conv_you')}:** {msg['content']}")
            else:
                st.markdown(f"**{t('conv_tutor')}:** {msg['content']}")
            st.markdown("---")

    # ---- Chat input ----
    user_input = st.chat_input(t("conv_input_placeholder"))

    if user_input:
        # Add user message
        st.session_state.conversation_messages.append({"role": "user", "content": user_input})
        st.session_state.conversation_count += 1

        # Get AI response
        client = get_llm_client()
        if client.is_available:
            # Prepare history for AI
            history = []
            for msg in st.session_state.conversation_messages[-20:-1]:  # Last 20 messages excluding current
                history.append({"role": msg["role"], "content": msg["content"]})
            
            response = client.chat_tutor(
                user_input, 
                history,
                st.session_state.conversation_level
            )
        else:
            # Offline mode: simple keyword-based response
            response = get_offline_tutor_response(user_input)

        st.session_state.conversation_messages.append({"role": "assistant", "content": response})
        st.rerun()

    # ---- Topic suggestions (when conversation is empty) ----
    if st.session_state.conversation_count == 0:
        st.markdown(t("conv_topic_suggestions"))
        topics = [
            t("conv_topic1"),
            t("conv_topic2"),
            t("conv_topic3"),
            t("conv_topic4"),
            t("conv_topic5"),
            t("conv_topic6"),
            t("conv_topic7"),
        ]
        cols = st.columns(3)
        for i, topic in enumerate(topics):
            with cols[i % 3]:
                if st.button(topic, key=f"topic_{i}", use_container_width=True):
                    st.session_state.conversation_messages.append({"role": "user", "content": topic})
                    st.session_state.conversation_count += 1

                    client = get_llm_client()
                    if client.is_available:
                        response = client.chat_tutor(topic, [], st.session_state.conversation_level)
                    else:
                        response = get_offline_tutor_response(topic)
                    
                    st.session_state.conversation_messages.append({"role": "assistant", "content": response})
                    st.rerun()


def get_offline_tutor_response(user_input: str) -> str:
    """
    Offline mode: basic response without AI.
    Provides simple grammar corrections and encouragement.
    """
    import re
    
    # Basic grammar checks
    corrections = []
    
    # Check for missing 3rd person -s
    words = user_input.split()
    for i, w in enumerate(words):
        if w.lower() in ['he', 'she', 'it'] and i + 1 < len(words):
            next_word = words[i + 1]
            if next_word.isalpha() and not next_word.endswith('s') and next_word.lower() not in ['is', 'was', 'has', 'does', 'can', 'will', 'could', 'would', 'should', 'may', 'might', 'must']:
                corrections.append(t("conv_verb_s_correction").format(w=w, nw=next_word))
    
    # Check for missing articles
    if not re.search(r'\b(a|an|the)\b', user_input.lower()):
        corrections.append(t("conv_article_tip"))
    
    # Check for basic sentence structure
    if not user_input.strip().endswith(('.', '!', '?')):
        corrections.append(t("conv_punctuation_tip"))
    
    if corrections:
        response = t("conv_improve_header") + "\n\n"
        response += t("conv_corrections_title") + "\n"
        for c in corrections:
            response += f"- {c}\n"
        
        response += "\n" + t("conv_better_expression") + "\n"
        response += f"- {user_input.strip().capitalize()}"
        if not user_input.strip().endswith(('.', '!', '?')):
            response += "."
        response += "\n\n" + t("conv_vocab_tip") + "\n"
    else:
        response = t("conv_good_job") + "\n\n"
        response += t("conv_keep_going") + "\n"
        response += t("conv_expand_hint") + "\n"
        response += t("conv_connector_hint") + "\n"
        response += t("conv_vocab_hint") + "\n"
    
    response += "\n" + t("conv_follow_up")
    
    return response


if __name__ == "__main__":
    show()
