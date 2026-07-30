"""
Cyber English AI Tutor - Internationalization (i18n) Module
Supporting Chinese and English. Add translations via the DICT below.
"""

import streamlit as st

# ── Translation Dictionary ──
DICT = {
    # ── Navigation ──
    "nav_home": {"en": "🏠 Home", "zh": "🏠 首页"},
    "nav_dashboard": {"en": "📊 Dashboard", "zh": "📊 学习仪表盘"},
    "nav_vocabulary": {"en": "📖 Vocabulary", "zh": "📖 词汇学习"},
    "nav_conversation": {"en": "💬 Conversation", "zh": "💬 AI 陪练"},
    "nav_reading": {"en": "📚 Reading", "zh": "📚 文章阅读"},
    "nav_sentence": {"en": "✍️ Sentence", "zh": "✍️ 句子分析"},
    "nav_settings": {"en": "Settings", "zh": "设置"},
    "nav_modules": {"en": "Learning Modules", "zh": "学习模块"},
    "nav_ai_provider": {"en": "AI Provider", "zh": "AI 服务商"},
    "nav_language": {"en": "Language", "zh": "语言"},
    "nav_version": {"en": "v1.0.0 | Cyber English AI Tutor", "zh": "v1.0.0 | Cyber English AI Tutor"},

    # ── Home Page ──
    "home_title": {"en": "🌐 Cyber English AI Tutor", "zh": "🌐 Cyber English AI Tutor"},
    "home_welcome": {
        "en": "## 🎯 Welcome to Your AI English Learning Platform\n\n**Cyber English AI Tutor** is an AI-powered platform designed to help you improve your English, with a special focus on cybersecurity and technical vocabulary.",
        "zh": "## 🎯 欢迎使用 AI 英语学习平台\n\n**Cyber English AI Tutor** 是一个由 AI 驱动的英语学习平台，专注于网络安全和技术英语词汇。"
    },
    "home_module_header": {"en": "### Choose a Learning Module:", "zh": "### 选择学习模块："},
    "home_module_desc_vocab": {"en": "Learn words with AI-powered phonetics, examples & memory tips", "zh": "学习单词，包含音标、例句和记忆方法"},
    "home_module_desc_conv": {"en": "Practice speaking with an adaptive AI tutor", "zh": "与自适应 AI 老师练习口语"},
    "home_module_desc_read": {"en": "Read multi-domain articles with smart AI assistance", "zh": "阅读多领域文章，AI 智能辅助"},
    "home_module_desc_sentence": {"en": "Analyze grammar, vocabulary & get improvement suggestions", "zh": "分析语法词汇，获取改进建议"},
    "home_module_desc_dashboard": {"en": "Track your learning progress and daily goals", "zh": "追踪学习进度和每日目标"},
    "home_quick_stats": {"en": "### ⚡ Quick Stats", "zh": "### ⚡ 快速统计"},
    "home_words_learned": {"en": "**Words Learned:** 0", "zh": "**已学单词：** 0"},
    "home_articles_read": {"en": "**Articles Read:** 0", "zh": "**已读文章：** 0"},
    "home_conversations": {"en": "**Conversations:** 0", "zh": "**对话次数：** 0"},
    "home_current_level": {"en": "**Current Level:** Intermediate", "zh": "**当前等级：** 中级"},
    "home_getting_started": {"en": "### 🔧 Getting Started", "zh": "### 🔧 快速开始"},
    "home_gs_step1": {"en": "1. Set your API key in `.env`", "zh": "1. 在 `.env` 中配置 API 密钥"},
    "home_gs_step2": {"en": "2. Start with **Vocabulary** or **Conversation**", "zh": "2. 从**词汇学习**或**AI 陪练**开始"},
    "home_gs_step3": {"en": "3. Check your progress in **Dashboard**", "zh": "3. 在**仪表盘**中查看进度"},
    "home_sidebar_hint": {"en": "👈 Select **Dashboard** from the sidebar to view your learning statistics, or pick a module above to start learning!", "zh": "👈 从侧边栏选择**学习仪表盘**查看学习统计，或选择上方模块开始学习！"},

    # ── Dashboard ──
    "dash_title": {"en": "📊 Learning Dashboard", "zh": "📊 学习仪表盘"},
    "dash_today": {"en": "Today's Learning", "zh": "今日学习"},
    "dash_words": {"en": "Words", "zh": "词汇"},
    "dash_articles": {"en": "Articles", "zh": "文章"},
    "dash_speaking": {"en": "Speaking", "zh": "口语"},
    "dash_sentences": {"en": "Sentences", "zh": "句子"},
    "dash_score": {"en": "Score", "zh": "分数"},
    "dash_daily_goals": {"en": "Daily Goals", "zh": "每日目标"},
    "dash_vocab_goal": {"en": "Vocabulary", "zh": "词汇"},
    "dash_reading_goal": {"en": "Reading", "zh": "阅读"},
    "dash_conv_goal": {"en": "Conversation", "zh": "对话"},
    "dash_english_level": {"en": "🎓 English Level", "zh": "🎓 英语等级"},
    "dash_current_level": {"en": "**Current Level:** {}", "zh": "**当前等级：** {}"},
    "dash_vocab_size": {"en": "**Vocabulary Size:** {} words", "zh": "**词汇量：** {} 个"},
    "dash_update_level": {"en": "Update your level:", "zh": "更新等级："},
    "dash_profile": {"en": "🧑 Profile Settings", "zh": "🧑 个人设置"},
    "dash_profession": {"en": "Profession:", "zh": "职业："},
    "dash_profession_placeholder": {"en": "e.g. Security Engineer", "zh": "例如：信息安全工程师"},
    "dash_interests": {"en": "Interests:", "zh": "兴趣方向："},
    "dash_quick_start": {"en": "🚀 Quick Start", "zh": "🚀 快速开始"},
    "dash_this_week": {"en": "📊 This Week", "zh": "📊 本周统计"},
    "dash_no_data": {"en": "No learning data yet. Start learning to see your progress!", "zh": "暂无学习数据，开始学习吧！"},
    "dash_recommended": {"en": "📋 Recommended Tasks", "zh": "📋 推荐任务"},
    "dash_task_vocab": {"en": "Learn 10 new words", "zh": "学习 10 个新单词"},
    "dash_task_read": {"en": "Read one article", "zh": "阅读一篇文章"},
    "dash_task_conv": {"en": "Practice 15 min conversation", "zh": "练习 15 分钟对话"},
    "dash_task_sentence": {"en": "Analyze 5 sentences", "zh": "分析 5 个句子"},

    # ── Vocabulary ──
    "vocab_title": {"en": "📖 Vocabulary Learning", "zh": "📖 词汇学习"},
    "vocab_tab_lookup": {"en": "🔍 Look Up", "zh": "🔍 查词"},
    "vocab_tab_browse": {"en": "📚 Browse All", "zh": "📚 浏览"},
    "vocab_tab_bookmarks": {"en": "⭐ Bookmarks", "zh": "⭐ 收藏"},
    "vocab_tab_review": {"en": "🔄 Review", "zh": "🔄 复习"},
    "vocab_enter_word": {"en": "Enter an English word:", "zh": "输入英文单词："},
    "vocab_placeholder": {"en": "e.g. vulnerability, firewall, encryption...", "zh": "例如：vulnerability, firewall, encryption..."},
    "vocab_found_local": {"en": "✅ Found in local vocabulary database!", "zh": "✅ 在本地词库中找到！"},
    "vocab_phonetic": {"en": "Phonetic", "zh": "音标"},
    "vocab_pos": {"en": "Part of Speech", "zh": "词性"},
    "vocab_mark_learned": {"en": "✅ Mark as Learned", "zh": "✅ 标记为已学"},
    "vocab_bookmark": {"en": "⭐ Bookmark", "zh": "⭐ 收藏"},
    "vocab_bookmarked": {"en": "⭐ Bookmarked ✓", "zh": "⭐ 已收藏 ✓"},
    "vocab_not_found": {"en": "not found in local database.", "zh": "在本地词库中未找到。"},
    "vocab_ai_hint": {"en": "💡 Try: vulnerability, firewall, encryption, malware, phishing", "zh": "💡 试试：vulnerability, firewall, encryption, malware, phishing"},
    "vocab_details": {"en": "📖 Word Details", "zh": "📖 单词详情"},
    "vocab_meaning": {"en": "Chinese Meaning", "zh": "中文含义"},
    "vocab_level": {"en": "Level", "zh": "等级"},
    "vocab_category": {"en": "Category", "zh": "分类"},
    "vocab_root": {"en": "Word Root", "zh": "词根"},
    "vocab_example": {"en": "Example", "zh": "例句"},
    "vocab_related": {"en": "Related Words", "zh": "相关词汇"},
    "vocab_memory_tip": {"en": "💡 Memory Tip", "zh": "💡 记忆方法"},
    "vocab_browse_title": {"en": "Browse Vocabulary", "zh": "浏览词汇"},
    "vocab_search": {"en": "🔍 Search words:", "zh": "🔍 搜索单词："},
    "vocab_filter_placeholder": {"en": "Filter by keyword...", "zh": "按关键词筛选..."},
    "vocab_all": {"en": "All", "zh": "全部"},
    "vocab_status": {"en": "Status", "zh": "状态"},
    "vocab_learned_status": {"en": "✅ Learned", "zh": "✅ 已学"},
    "vocab_bookmarked_status": {"en": "⭐ Bookmarked", "zh": "⭐ 已收藏"},
    "vocab_no_bookmarks": {"en": "No bookmarked words yet.", "zh": "暂无收藏的单词。"},
    "vocab_review_title": {"en": "🔄 Review Mode", "zh": "🔄 复习模式"},
    "vocab_learned_count": {"en": "You have learned **{}** words.", "zh": "你已经学习了 **{}** 个单词。"},
    "vocab_select_review": {"en": "Select a word to review:", "zh": "选择一个单词复习："},
    "vocab_recall_hint": {"en": "💡 Try to recall the meaning before reading it!", "zh": "💡 先回忆词义再看答案！"},
    "vocab_no_learned": {"en": "No words learned yet.", "zh": "还没有已学单词。"},

    # ── New vocabulary keys ──
    "vocab_learned_label": {"en": "✅ Learned!", "zh": "✅ 已学!"},
    "vocab_memory_tip_ai": {"en": "AI-powered memory tips will appear here once LLM is connected.", "zh": "AI记忆方法将在连接LLM后显示。"},
    "vocab_col_word": {"en": "Word", "zh": "单词"},
    "vocab_col_phonetic": {"en": "Phonetic", "zh": "音标"},
    "vocab_col_meaning": {"en": "Meaning", "zh": "含义"},
    "vocab_col_level": {"en": "Level", "zh": "等级"},
    "vocab_col_category": {"en": "Category", "zh": "分类"},
    "vocab_status_none": {"en": "—", "zh": "—"},
    "vocab_showing_count": {"en": "Showing {} of {} words", "zh": "显示 {} / {} 个单词"},
    "vocab_no_match": {"en": "No words found matching your filters.", "zh": "没有匹配筛选条件的单词。"},
    "vocab_category_filter": {"en": "Category", "zh": "分类"},
    "vocab_level_filter": {"en": "Level", "zh": "等级"},
    "vocab_bookmarked_title": {"en": "Bookmarked Words", "zh": "已收藏的单词"},

    # ── Conversation ──
    "conv_title": {"en": "💬 AI English Conversation", "zh": "💬 AI 英语陪练"},
    "conv_current_level": {"en": "**Current Level:** {}", "zh": "**当前等级：** {}"},
    "conv_adjust_level": {"en": "Adjust your English level:", "zh": "调整英语等级："},
    "conv_session_stats": {"en": "📊 Session Stats", "zh": "📊 会话统计"},
    "conv_messages": {"en": "Messages: **{}**", "zh": "消息数：**{}**"},
    "conv_clear": {"en": "🗑️ Clear History", "zh": "🗑️ 清除历史"},
    "conv_input_placeholder": {"en": "Type your message in English...", "zh": "用英文输入消息..."},
    "conv_topic_suggestions": {"en": "💡 Suggested Topics", "zh": "💡 推荐话题"},
    "conv_topic1": {"en": "Introduce yourself and your job", "zh": "自我介绍和工作"},
    "conv_topic2": {"en": "Describe your last vacation", "zh": "描述上次假期"},
    "conv_topic3": {"en": "Talk about your favorite technology", "zh": "聊聊你最喜欢的技术"},
    "conv_topic4": {"en": "Discuss cybersecurity trends", "zh": "讨论网络安全趋势"},
    "conv_topic5": {"en": "Explain how the internet works", "zh": "解释互联网工作原理"},
    "conv_topic6": {"en": "Describe your daily routine", "zh": "描述你的日常"},
    "conv_topic7": {"en": "Talk about your learning goals", "zh": "聊聊学习目标"},
    "conv_you": {"en": "🧑 You", "zh": "🧑 你"},
    "conv_tutor": {"en": "🤖 Tutor", "zh": "🤖 老师"},

    # ── Reading ──
    "read_title": {"en": "📚 English Reading", "zh": "📚 文章阅读"},
    "read_categories": {"en": "📂 Categories", "zh": "📂 分类"},
    "read_choose_category": {"en": "Choose category:", "zh": "选择分类："},
    "read_refresh": {"en": "🔄 Refresh Articles", "zh": "🔄 刷新文章"},
    "read_no_articles": {"en": "No articles found in '{}'. Check back later!", "zh": "'{}' 分类暂无文章，敬请期待！"},
    "read_tips_title": {"en": "💡 Reading Tips", "zh": "💡 阅读建议"},
    "read_tip1": {"en": "- Start with **Beginner** level articles", "zh": "- 从**初级**文章开始"},
    "read_tip2": {"en": "- Read each article at least twice", "zh": "- 每篇文章至少读两遍"},
    "read_tip3": {"en": "- Note down new vocabulary", "zh": "- 记录生词"},
    "read_tip4": {"en": "- Try to summarize in your own words", "zh": "- 尝试用自己的话总结"},
    "read_select_article": {"en": "Select an article:", "zh": "选择文章："},
    "read_key_vocab": {"en": "🔑 Key Vocabulary", "zh": "🔑 重点词汇"},
    "read_ai_analysis": {"en": "🤖 AI Analysis", "zh": "🤖 AI 分析"},
    "read_mark_read": {"en": "🎯 Mark as Read", "zh": "🎯 标记已读"},
    "read_marked": {"en": "✅ Marked as read! +1 article", "zh": "✅ 已标记！+1 篇文章"},
    "read_progress": {"en": "📊 Reading Progress", "zh": "📊 阅读进度"},
    "read_today_progress": {"en": "Today: {} / 3 articles", "zh": "今日：{} / 3 篇文章"},

    # ── Sentence Analysis ──
    "sent_title": {"en": "✍️ Sentence Analysis", "zh": "✍️ 句子分析"},
    "sent_enter": {"en": "Enter an English sentence to analyze:", "zh": "输入要分析的英文句子："},
    "sent_placeholder": {"en": "e.g. The vulnerability was exploited by attackers.", "zh": "例如：The vulnerability was exploited by attackers."},
    "sent_analyze": {"en": "🔍 Analyze Sentence", "zh": "🔍 分析句子"},
    "sent_try_example": {"en": "🔄 Try Example", "zh": "🔄 试试例句"},
    "sent_ai_analysis": {"en": "🤖 AI Analysis", "zh": "🤖 AI 分析"},
    "sent_hint": {"en": "Enter a sentence above and click **Analyze Sentence** to get started!", "zh": "在上方输入句子后点击**分析句子**开始！"},
    "sent_examples_title": {"en": "💡 Try these example sentences:", "zh": "💡 试试这些例句："},
    "sent_grammar": {"en": "📐 Grammar Analysis", "zh": "📐 语法分析"},
    "sent_difficulty": {"en": "📊 Estimated Difficulty", "zh": "📊 预估难度"},
    "sent_stats": {"en": "📝 Stats", "zh": "📝 统计"},
    "sent_better": {"en": "✨ Better Expression", "zh": "✨ 更优表达"},
    "sent_vocab_in_sentence": {"en": "📖 Vocabulary in This Sentence", "zh": "📖 句中词汇"},
    "sent_no_issues": {"en": "✅ No obvious grammar issues detected!", "zh": "✅ 未检测到明显语法问题！"},
    "sent_ai_offline": {"en": "*Configure API key for AI-powered improvement suggestions.*", "zh": "*配置 API 密钥后可使用 AI 改进建议。*"},

    # ── Misc ──
    "loading": {"en": "Analyzing...", "zh": "分析中..."},
    "go": {"en": "Go", "zh": "前往"},
    "close": {"en": "✕ Close", "zh": "✕ 关闭"},
    "remove": {"en": "✕ Remove", "zh": "✕ 移除"},
    "clear": {"en": "✕ Clear", "zh": "✕ 清除"},
    "see_more": {"en": "See more", "zh": "查看更多"},
    "show_more": {"en": "Show more", "zh": "展开"},
    "show_less": {"en": "Show less", "zh": "收起"},

    # === Auto-added keys ===
    "dash_learner": {"en": "Learner", "zh": "学习者"},
    "dash_min": {"en": "min", "zh": "分钟"},
    "dash_level_beginner": {"en": "Beginner (A1)", "zh": "初级 (A1)"},
    "dash_level_elementary": {"en": "Elementary (A2)", "zh": "基础 (A2)"},
    "dash_level_intermediate": {"en": "Intermediate (B1)", "zh": "中级 (B1)"},
    "dash_level_upper_intermediate": {"en": "Upper Intermediate (B2)", "zh": "中高级 (B2)"},
    "dash_level_advanced": {"en": "Advanced (C1)", "zh": "高级 (C1)"},
    "dash_level_proficient": {"en": "Proficient (C2)", "zh": "精通 (C2)"},
    "dash_interest_cybersecurity": {"en": "Cybersecurity", "zh": "网络安全"},
    "dash_interest_technology": {"en": "Technology", "zh": "科技"},
    "dash_interest_ai": {"en": "AI", "zh": "人工智能"},
    "dash_interest_business": {"en": "Business", "zh": "商业"},
    "dash_interest_science": {"en": "Science", "zh": "科学"},
    "dash_interest_daily_news": {"en": "Daily News", "zh": "每日新闻"},
    "dash_interest_finance": {"en": "Finance", "zh": "金融"},
    "dash_interest_culture": {"en": "Culture", "zh": "文化"},

    # ── Conversation (offline tutor) ──
    "conv_initial_message": {"en": "Hello! I'm your AI English tutor. I'll help you practice English by having conversations. I'll correct your grammar, suggest better expressions, and adapt to your level.\n\n**What would you like to talk about today?**", "zh": "你好！我是你的 AI 英语老师。我会通过对话帮你练习英语，纠正语法错误，建议更好的表达方式，并根据你的水平调整难度。\n\n**今天想聊什么？**"},
    "conv_cleared": {"en": "Conversation cleared! What would you like to talk about?", "zh": "对话已清除！想聊点什么？"},
    "conv_improve_header": {"en": "### ✅ Great effort! Let me help you improve:", "zh": "### ✅ 很不错！我来帮你改进："},
    "conv_corrections_title": {"en": "**Corrections:**", "zh": "**纠错：**"},
    "conv_better_expression": {"en": "**Better expression:**", "zh": "**更优表达：**"},
    "conv_good_job": {"en": "### 👍 Good job! Your sentence looks correct.", "zh": "### 👍 写得好！你的句子看起来正确。"},
    "conv_keep_going": {"en": "**Keep Going!** Here are some ways to expand:", "zh": "**继续加油！** 这里有一些扩展方法："},
    "conv_expand_hint": {"en": "- Try adding more details (when, where, why)", "zh": "- 尝试添加更多细节（时间、地点、原因）"},
    "conv_connector_hint": {"en": "- Use connecting words (however, moreover, therefore)", "zh": "- 使用连接词（however, moreover, therefore）"},
    "conv_vocab_hint": {"en": "- Practice using new vocabulary", "zh": "- 练习使用新词汇"},
    "conv_follow_up": {"en": "**Follow-up Question:** What else would you like to talk about? 😊", "zh": "**追问：** 还想聊点什么？😊"},
    "conv_verb_s_correction": {"en": "Remember: after '{}', the verb usually needs '-s' (e.g., '{}' '{}'s')", "zh": "注意：在 '{}' 之后，动词通常需要加 '-s'（例如：'{}' '{}'s'）"},
    "conv_article_tip": {"en": "Consider adding an article (a/an/the) before singular countable nouns.", "zh": "考虑在单数可数名词前加冠词（a/an/the）。"},
    "conv_punctuation_tip": {"en": "Don't forget to end your sentence with proper punctuation.", "zh": "别忘了用正确的标点符号结束句子。"},
    "conv_vocab_tip": {"en": "**💡 Tip:** Try using more specific vocabulary to express your thoughts clearly.", "zh": "**💡 提示：** 尝试使用更具体的词汇来清晰表达你的想法。"},
    "conv_topic1": {"en": "Introduce yourself and your job", "zh": "自我介绍和工作"},
    "conv_topic2": {"en": "Describe your last vacation", "zh": "描述上次假期"},
    "conv_topic3": {"en": "Talk about your favorite technology", "zh": "聊聊你最喜欢的技术"},
    "conv_topic4": {"en": "Discuss cybersecurity trends", "zh": "讨论网络安全趋势"},
    "conv_topic5": {"en": "Explain how the internet works", "zh": "解释互联网工作原理"},
    "conv_topic6": {"en": "Describe your daily routine", "zh": "描述你的日常"},
    "conv_topic7": {"en": "Talk about your learning goals", "zh": "聊聊学习目标"},

    # ── Reading (offline + meta) ──
    "read_meta_category": {"en": "**📂 {}**", "zh": "**📂 {}**"},
    "read_meta_difficulty": {"en": "**📊 {}**", "zh": "**📊 {}**"},
    "read_meta_date": {"en": "**📅 {}**", "zh": "**📅 {}**"},
    "read_vocab_btn": {"en": "📖 {}", "zh": "📖 {}"},
    "read_word_example": {"en": "Example", "zh": "例句"},
    "read_word_level": {"en": "Level", "zh": "等级"},
    "read_word_category": {"en": "Category", "zh": "分类"},
    "read_vocab_no_api": {"en": "'{}' - AI analysis available after API key configuration.", "zh": "'{}' - 配置 API 密钥后可使用 AI 分析。"},
    "read_analyzing": {"en": "🤖 Analyzing article...", "zh": "🤖 正在分析文章..."},
    "read_ai_analysis_title": {"en": "🤖 AI Article Analysis", "zh": "🤖 AI 文章分析"},
    "read_clear_analysis": {"en": "✕ Clear analysis", "zh": "✕ 清除分析"},
    "read_offline_title": {"en": "### 📋 Article Analysis (Offline Mode)", "zh": "### 📋 文章分析（离线模式）"},
    "read_offline_summary": {"en": "**Summary:**", "zh": "**概要：**"},
    "read_offline_stats": {"en": "This is a {}-word article with {} unique vocabulary words.", "zh": "这是一篇 {} 词的文章，包含 {} 个独特词汇。"},
    "read_offline_vocab": {"en": "**Key Vocabulary:**", "zh": "**核心词汇：**"},
    "read_offline_no_api": {"en": "- (Configure API key for detailed vocabulary analysis)", "zh": "-（配置 API 密钥以获取详细词汇分析）"},
    "read_offline_difficulty": {"en": "**Reading Difficulty:** {}", "zh": "**阅读难度：** {}"},
    "read_offline_sent_count": {"en": "**Sentence Count:** {}", "zh": "**句子数：** {}"},
    "read_offline_avg_len": {"en": "**Average Sentence Length:** {} words", "zh": "**平均句子长度：** {} 词"},
    "read_offline_suggestions": {"en": "**Learning Suggestions:**", "zh": "**学习建议：**"},
    "read_offline_sug1": {"en": "- Read the article aloud to practice pronunciation", "zh": "- 大声朗读文章以练习发音"},
    "read_offline_sug2": {"en": "- Write a short summary in your own words", "zh": "- 用自己的话写一篇简短总结"},
    "read_offline_sug3": {"en": "- Look up unfamiliar words in the Vocabulary module", "zh": "- 在词汇模块中查阅生词"},
    "read_offline_sug4": {"en": "- Try to identify 3 new grammar patterns", "zh": "- 尝试找出 3 个新的语法模式"},
    "read_offline_api_hint": {"en": "*For AI-powered analysis (summary, grammar highlights, discussion questions), configure your API key in .env*", "zh": "*如需 AI 分析（摘要、语法要点、讨论问题），请在 .env 中配置 API 密钥*"},
    "read_level_beginner": {"en": "Beginner", "zh": "初级"},
    "read_level_intermediate": {"en": "Intermediate", "zh": "中级"},
    "read_level_advanced": {"en": "Advanced", "zh": "高级"},

    # ── Sentence (offline analysis) ──
    "sent_grammar_offline": {"en": "### 📐 Grammar Analysis (Offline Mode)", "zh": "### 📐 语法分析（离线模式）"},
    "sent_subject_verb_detail": {"en": "🔸 Subject-verb agreement: After '{}', the verb usually needs '-s' (e.g., '{}' '{}'s')", "zh": "🔸 主谓一致：在 '{}' 之后，动词通常需要加 '-s'（例如：'{}' '{}'s'）"},
    "sent_missing_article": {"en": "🔸 Missing article: Consider adding 'a', 'an', or 'the' before '{}'", "zh": "🔸 缺少冠词：考虑在 '{}' 前加 'a'、'an' 或 'the'"},
    "sent_tense_check": {"en": "🔸 Tense check: If using present perfect, the verb should be in past participle form (e.g., 'have worked')", "zh": "🔸 时态检查：如果使用现在完成时，动词应为过去分词形式"},
    "sent_short_sentence": {"en": "🔸 This sentence is very short. Consider adding more details.", "zh": "🔸 这个句子太短了，考虑添加更多细节。"},
    "sent_passive_voice": {"en": "🔸 **Passive voice** detected. Active voice is usually more direct.", "zh": "🔸 检测到**被动语态**。主动语态通常更直接。"},
    "sent_stats_detail": {"en": "**📝 Stats:** {} words, {} characters, {} punctuation marks", "zh": "**📝 统计：** {} 词，{} 字符，{} 个标点"},
    "sent_active_exploited": {"en": "Active: **Threat actors exploited the vulnerability.**", "zh": "主动语态：**Threat actors exploited the vulnerability.**"},
    "sent_active_implemented": {"en": "Active: **The team implemented the security measures.**", "zh": "主动语态：**The team implemented the security measures.**"},
}


def t(key: str, lang: str = None) -> str:
    """
    Translate a key into the target language.

    Args:
        key: The translation key
        lang: 'en' or 'zh'. If None, reads from st.session_state.language

    Returns:
        Translated string, or key itself if not found
    """
    if lang is None:
        lang = _get_lang()
    
    entry = DICT.get(key)
    if entry is None:
        return key  # key not found, return as-is
    
    return entry.get(lang, entry.get("en", key))


def _get_lang() -> str:
    """Get the current language from session state."""
    if "language" not in st.session_state:
        st.session_state.language = "zh"
    return st.session_state.language


def set_language(lang: str):
    """Set the current language."""
    if lang in ("en", "zh"):
        st.session_state.language = lang


def lang_selector():
    """Render a language selector in the sidebar."""
    current = _get_lang()
    label = "🌐 Language / 语言"
    selected = st.sidebar.selectbox(
        label,
        options=["中文", "English"],
        index=0 if current == "zh" else 1,
        key="_lang_selector",
    )
    new_lang = "zh" if selected == "中文" else "en"
    if new_lang != current:
        set_language(new_lang)
        st.rerun()
