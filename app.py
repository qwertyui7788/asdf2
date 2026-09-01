import streamlit as st
from questions import QUESTIONS


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* 전체 배경 */
    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(255, 107, 107, 0.12),
                transparent 35%
            ),
            radial-gradient(
                circle at top right,
                rgba(78, 205, 196, 0.12),
                transparent 35%
            ),
            #f8f9fc;
    }

    /* 기본 컨테이너 */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* 제목 */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        color: #202124;
        margin-bottom: 0.3rem;
        letter-spacing: -2px;
    }

    .sub-title {
        text-align: center;
        color: #777;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* 카테고리 버튼 */
    .category-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #333;
        margin-bottom: 1rem;
    }

    /* 질문 */
    .question-number {
        text-align: center;
        color: #888;
        font-size: 0.95rem;
        font-weight: 700;
        margin-top: 1rem;
    }

    .question {
        text-align: center;
        font-size: 2rem;
        font-weight: 900;
        color: #222;
        margin: 1rem 0 2rem 0;
        line-height: 1.35;
        letter-spacing: -1px;
    }

    /* 진행률 */
    .progress-wrapper {
        width: 100%;
        height: 10px;
        background: #e8e8ee;
        border-radius: 20px;
        overflow: hidden;
        margin: 1rem 0 2rem 0;
    }

    .progress-bar {
        height: 100%;
        background: linear-gradient(
            90deg,
            #ff6b6b,
            #ff8e53
        );
        border-radius: 20px;
        transition: width 0.3s ease;
    }

    /* 선택 카드 */
    .choice-card {
        min-height: 250px;
        padding: 30px 20px;
        border-radius: 28px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
    }

    .choice-a {
        background: linear-gradient(
            145deg,
            #ff6b6b,
            #ff8e8e
        );
        color: white;
    }

    .choice-b {
        background: linear-gradient(
            145deg,
            #4ecdc4,
            #73d9d2
        );
        color: white;
    }

    .choice-emoji {
        font-size: 4rem;
        margin-bottom: 1rem;
    }

    .choice-title {
        font-size: 1.6rem;
        font-weight: 900;
        line-height: 1.3;
    }

    .choice-description {
        margin-top: 0.8rem;
        font-size: 0.95rem;
        opacity: 0.9;
    }

    /* 결과 */
    .result-box {
        background: white;
        padding: 35px 25px;
        border-radius: 28px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    }

    .result-emoji {
        font-size: 5rem;
    }

    .result-title {
        font-size: 2.2rem;
        font-weight: 900;
        color: #222;
        margin: 1rem 0;
    }

    .result-text {
        color: #777;
        font-size: 1rem;
        line-height: 1.7;
    }

    /* Streamlit 버튼 */
    div.stButton > button {
        width: 100%;
        border-radius: 18px;
        border: none;
        padding: 0.8rem 1rem;
        font-weight: 800;
        font-size: 1rem;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
    }

    /* 모바일 */
    @media (max-width: 768px) {

        .main-title {
            font-size: 2.3rem;
        }

        .question {
            font-size: 1.5rem;
        }

        .choice-card {
            min-height: 200px;
        }

        .choice-emoji {
            font-size: 3rem;
        }

        .choice-title {
            font-size: 1.3rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 세션 초기화
# =========================================================

if "category" not in st.session_state:
    st.session_state.category = None

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False


# =========================================================
# 함수
# =========================================================

def start_game(category):
    """게임 시작"""

    st.session_state.category = category
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.game_finished = False


def select_answer(answer):
    """답변 선택"""

    st.session_state.answers.append(answer)

    current = st.session_state.current_question
    questions = QUESTIONS[st.session_state.category]

    if current + 1 >= len(questions):
        st.session_state.game_finished = True
    else:
        st.session_state.current_question += 1


def restart_game():
    """게임 초기화"""

    st.session_state.category = None
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.game_finished = False


# =========================================================
# 홈 화면
# =========================================================

if st.session_state.category is None:

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        '둘 중 하나만 선택한다면? 🤔'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="category-title">🎮 게임을 선택하세요</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="choice-card choice-a">
                <div class="choice-emoji">🍔</div>
                <div class="choice-title">음식</div>
                <div class="choice-description">
                    평생 하나만 먹는다면?
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🍔 음식 게임 시작", key="food"):
            start_game("음식")
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="choice-card choice-b">
                <div class="choice-emoji">🏕️</div>
                <div class="choice-title">주말</div>
                <div class="choice-description">
                    주말에 뭐 할까?
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🏕️ 주말 게임 시작", key="weekend"):
            start_game("주말")
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="choice-card choice-a">
                <div class="choice-emoji">✈️</div>
                <div class="choice-title">여행</div>
                <div class="choice-description">
                    어디로 떠날까?
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("✈️ 여행 게임 시작", key="travel"):
            start_game("여행")
            st.rerun()

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#999;
            font-size:0.9rem;
            margin-top:2rem;
        ">
        친구들과 누가 더 취향이 비슷한지 비교해보세요! 👥
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 게임 화면
# =========================================================

elif not st.session_state.game_finished:

    category = st.session_state.category
    questions = QUESTIONS[category]

    current = st.session_state.current_question
    question = questions[current]

    total = len(questions)

    progress = ((current) / total) * 100

    # 상단
    st.markdown(
        f'<div class="main-title">⚖️ {category} 밸런스</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="question-number">
            QUESTION {current + 1} / {total}
        </div>

        <div class="progress-wrapper">
            <div
                class="progress-bar"
                style="width:{progress}%"
            ></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 질문
    st.markdown(
        f'<div class="question">{question["question"]}</div>',
        unsafe_allow_html=True
    )

    # 선택지
    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown(
            f"""
            <div class="choice-card choice-a">
                <div class="choice-emoji">
                    {question["a"]["emoji"]}
                </div>

                <div class="choice-title">
                    {question["a"]["title"]}
                </div>

                <div class="choice-description">
                    {question["a"]["description"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f'❤️ {question["a"]["title"]}',
            key=f"a_{current}"
        ):
            select_answer("A")
            st.rerun()

    with col2:

        st.markdown(
            f"""
            <div class="choice-card choice-b">
                <div class="choice-emoji">
                    {question["b"]["emoji"]}
                </div>

                <div class="choice-title">
                    {question["b"]["title"]}
                </div>

                <div class="choice-description">
                    {question["b"]["description"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f'💚 {question["b"]["title"]}',
            key=f"b_{current}"
        ):
            select_answer("B")
            st.rerun()

    # 홈으로
    st.markdown("")

    if st.button("🏠 게임 선택으로 돌아가기"):
        restart_game()
        st.rerun()


# =========================================================
# 결과 화면
# =========================================================

else:

    category = st.session_state.category
    answers = st.session_state.answers

    a_count = answers.count("A")
    b_count = answers.count("B")

    total = len(answers)

    if a_count > b_count:
        winner = "A"
        result_emoji = "❤️"
        result_title = "A 선택이 더 많아요!"
    elif b_count > a_count:
        winner = "B"
        result_emoji = "💚"
        result_title = "B 선택이 더 많아요!"
    else:
        winner = "DRAW"
        result_emoji = "⚖️"
        result_title = "완벽한 반반 취향!"
        
    st.markdown(
        '<div class="main-title">🎉 게임 종료!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-emoji">
                {result_emoji}
            </div>

            <div class="result-title">
                {result_title}
            </div>

            <div class="result-text">
                총 {total}개의 질문에 답했습니다.<br><br>

                ❤️ A 선택: <strong>{a_count}</strong>개<br>
                💚 B 선택: <strong>{b_count}</strong>개
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # 결과 메시지
    if winner == "A":

        st.success(
            "당신은 A 선택지를 선호하는 편이에요! ❤️"
        )

    elif winner == "B":

        st.success(
            "당신은 B 선택지를 선호하는 편이에요! 💚"
        )

    else:

        st.info(
            "어느 한쪽도 포기할 수 없는 균형 잡힌 취향이네요! ⚖️"
        )

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔄 다시 하기"):
            start_game(category)
            st.rerun()

    with col2:

        if st.button("🏠 다른 게임"):
            restart_game()
            st.rerun()
