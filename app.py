import streamlit as st
import random

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 게임 데이터
# =========================================================

GAME_DATA = {
    "🍔 음식": [
        {
            "question": "평생 하나만 먹는다면?",
            "left": "🍕 피자",
            "right": "🍗 치킨"
        },
        {
            "question": "더 좋아하는 음식은?",
            "left": "🍜 평생 라면",
            "right": "🍚 평생 김치볶음밥"
        },
        {
            "question": "둘 중 하나만 포기한다면?",
            "left": "☕ 커피",
            "right": "🍺 치맥"
        },
        {
            "question": "디저트 하나만 선택한다면?",
            "left": "🍰 케이크",
            "right": "🍦 아이스크림"
        },
        {
            "question": "평생 하나만 먹어야 한다면?",
            "left": "🍣 초밥",
            "right": "🥩 스테이크"
        },
        {
            "question": "야식으로 더 좋은 것은?",
            "left": "🍕 피자",
            "right": "🌶️ 떡볶이"
        },
    ],

    "🏠 주말": [
        {
            "question": "주말에 더 하고 싶은 것은?",
            "left": "🏠 집에서 푹 쉬기",
            "right": "🚗 어디든 떠나기"
        },
        {
            "question": "완벽한 토요일은?",
            "left": "🎮 하루 종일 게임",
            "right": "🌳 하루 종일 야외활동"
        },
        {
            "question": "주말 아침에 일어났다면?",
            "left": "😴 다시 자기",
            "right": "☀️ 일찍 일어나서 나가기"
        },
        {
            "question": "친구와 주말을 보낸다면?",
            "left": "🍻 맛집 탐방",
            "right": "🎬 영화관 가기"
        },
        {
            "question": "주말 여행을 간다면?",
            "left": "🏖️ 바다",
            "right": "🏔️ 산"
        },
    ],

    "✈️ 여행": [
        {
            "question": "휴가를 간다면?",
            "left": "🇯🇵 일본",
            "right": "🇫🇷 프랑스"
        },
        {
            "question": "여행 스타일은?",
            "left": "🗺️ 계획을 완벽하게 세우기",
            "right": "🎒 아무 계획 없이 떠나기"
        },
        {
            "question": "여행에서 더 중요한 것은?",
            "left": "🍽️ 맛있는 음식",
            "right": "📸 멋진 풍경"
        },
        {
            "question": "휴양 여행이라면?",
            "left": "🏝️ 바다에서 휴식",
            "right": "🏙️ 도시 관광"
        },
        {
            "question": "여행을 간다면 누구와?",
            "left": "👫 친한 친구",
            "right": "❤️ 연인"
        },
        {
            "question": "한 달 여행을 떠난다면?",
            "left": "🇺🇸 미국",
            "right": "🇪🇺 유럽"
        },
    ],

    "🎬 영화·문화": [
        {
            "question": "영화를 본다면?",
            "left": "😂 코미디",
            "right": "😱 공포"
        },
        {
            "question": "영화관에서 하나만 선택한다면?",
            "left": "🍿 팝콘",
            "right": "🥤 콜라"
        },
        {
            "question": "좋아하는 영화 스타일은?",
            "left": "🦸 액션",
            "right": "💖 로맨스"
        },
        {
            "question": "콘서트에 간다면?",
            "left": "🎤 아이돌 콘서트",
            "right": "🎸 밴드 공연"
        },
        {
            "question": "주말 밤에 본다면?",
            "left": "📺 드라마 몰아보기",
            "right": "🎬 영화 정주행"
        },
    ],

    "💭 일상": [
        {
            "question": "둘 중 하나를 선택한다면?",
            "left": "📱 스마트폰 없이 일주일",
            "right": "💻 컴퓨터 없이 일주일"
        },
        {
            "question": "더 싫은 것은?",
            "left": "⏰ 매일 1시간 일찍 출근",
            "right": "🌙 매일 1시간 늦게 퇴근"
        },
        {
            "question": "하루 동안 하나만 한다면?",
            "left": "📚 책 읽기",
            "right": "🎮 게임하기"
        },
        {
            "question": "평생 하나만 선택한다면?",
            "left": "☀️ 여름",
            "right": "❄️ 겨울"
        },
        {
            "question": "하루에 하나만 가능하다면?",
            "left": "🎧 음악 듣기",
            "right": "📺 유튜브 보기"
        },
    ]
}


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
                #eef2ff 0%,
                #f8fafc 40%,
                #ffffff 100%
            );
    }

    /* 상단 여백 */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* 제목 */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        color: #111827;
        margin-bottom: 0.3rem;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* 카테고리 */
    .category-label {
        text-align: center;
        color: #6366f1;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* 질문 */
    .question {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        color: #111827;
        margin: 1rem 0 2rem 0;
    }

    /* 카드 */
    .choice-card {
        min-height: 230px;
        border-radius: 24px;
        padding: 35px 25px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow:
            0 15px 35px rgba(15, 23, 42, 0.08);
        transition: all 0.25s ease;
        border: 1px solid rgba(255,255,255,0.8);
    }

    .choice-card:hover {
        transform: translateY(-5px);
        box-shadow:
            0 20px 45px rgba(15, 23, 42, 0.14);
    }

    .left-card {
        background: linear-gradient(
            135deg,
            #dbeafe,
            #eff6ff
        );
    }

    .right-card {
        background: linear-gradient(
            135deg,
            #fce7f3,
            #fff1f2
        );
    }

    .choice-text {
        font-size: 1.45rem;
        font-weight: 800;
        color: #111827;
    }

    .vs {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        font-weight: 900;
        color: #6366f1;
        height: 100%;
    }

    /* 진행률 */
    .progress-text {
        text-align: center;
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 1rem;
    }

    /* 결과 */
    .result-card {
        background: white;
        border-radius: 25px;
        padding: 35px;
        margin-top: 25px;
        box-shadow:
            0 15px 40px rgba(15, 23, 42, 0.1);
        text-align: center;
    }

    .result-title {
        font-size: 2rem;
        font-weight: 900;
        color: #111827;
    }

    .result-score {
        font-size: 3rem;
        font-weight: 900;
        color: #6366f1;
    }

    /* 버튼 */
    div.stButton > button {
        width: 100%;
        border-radius: 15px;
        min-height: 52px;
        font-weight: 700;
        border: none;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Session State 초기화
# =========================================================

if "category" not in st.session_state:
    st.session_state.category = "🍔 음식"

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "left_score" not in st.session_state:
    st.session_state.left_score = 0

if "right_score" not in st.session_state:
    st.session_state.right_score = 0

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False


# =========================================================
# 함수
# =========================================================

def start_game(category):
    """새 게임 시작"""

    st.session_state.category = category

    questions = GAME_DATA[category].copy()

    random.shuffle(questions)

    st.session_state.questions = questions
    st.session_state.current_question = 0

    st.session_state.left_score = 0
    st.session_state.right_score = 0

    st.session_state.game_started = True
    st.session_state.game_finished = False


def reset_game():
    """게임 초기화"""

    st.session_state.questions = []
    st.session_state.current_question = 0

    st.session_state.left_score = 0
    st.session_state.right_score = 0

    st.session_state.game_started = False
    st.session_state.game_finished = False


def select_answer(side):
    """답변 선택"""

    if side == "left":
        st.session_state.left_score += 1
    else:
        st.session_state.right_score += 1

    st.session_state.current_question += 1

    if (
        st.session_state.current_question
        >= len(st.session_state.questions)
    ):
        st.session_state.game_finished = True


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">⚖️ 밸런스 게임</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '둘 중 하나만 선택해야 한다면? 당신의 선택은?'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 게임 시작 전
# =========================================================

if not st.session_state.game_started:

    st.markdown(
        '<div class="category-label">GAME CATEGORY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">어떤 밸런스 게임을 해볼까요?</div>',
        unsafe_allow_html=True
    )

    categories = list(GAME_DATA.keys())

    cols = st.columns(2)

    for index, category in enumerate(categories):

        with cols[index % 2]:

            question_count = len(GAME_DATA[category])

            if st.button(
                f"{category}\n\n{question_count}개의 질문",
                key=f"category_{index}",
                use_container_width=True
            ):
                start_game(category)
                st.rerun()

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#6b7280;
            padding:20px;
        ">
            💡 카드를 선택하면 게임이 시작됩니다.<br>
            모든 질문에 답하고 나만의 선택 결과를 확인해보세요!
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 게임 진행
# =========================================================

elif (
    st.session_state.game_started
    and not st.session_state.game_finished
):

    questions = st.session_state.questions

    current = st.session_state.current_question

    question = questions[current]

    # 카테고리
    st.markdown(
        f"""
        <div class="category-label">
            {st.session_state.category}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 질문
    st.markdown(
        f"""
        <div class="question">
            {question["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 진행률
    progress = current / len(questions)

    st.progress(progress)

    st.markdown(
        f"""
        <div class="progress-text">
            {current + 1} / {len(questions)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # 카드 영역
    left_col, vs_col, right_col = st.columns(
        [5, 1, 5]
    )

    with left_col:

        st.markdown(
            f"""
            <div class="choice-card left-card">
                <div class="choice-text">
                    {question["left"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "👈 이걸 선택할래!",
            key=f"left_{current}",
            use_container_width=True
        ):
            select_answer("left")
            st.rerun()

    with vs_col:

        st.markdown(
            """
            <div class="vs">
                VS
            </div>
            """,
            unsafe_allow_html=True
        )

    with right_col:

        st.markdown(
            f"""
            <div class="choice-card right-card">
                <div class="choice-text">
                    {question["right"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "이걸 선택할래! 👉",
            key=f"right_{current}",
            use_container_width=True
        ):
            select_answer("right")
            st.rerun()

    st.write("")
    st.write("")

    if st.button(
        "게임 그만하기",
        key="stop_game"
    ):
        reset_game()
        st.rerun()


# =========================================================
# 결과
# =========================================================

elif st.session_state.game_finished:

    left_score = st.session_state.left_score
    right_score = st.session_state.right_score

    total = left_score + right_score

    left_percent = round(
        left_score / total * 100
    )

    right_percent = round(
        right_score / total * 100
    )

    if left_score > right_score:
        result = "👈 당신은 왼쪽 선택을 더 좋아해요!"
    elif right_score > left_score:
        result = "👉 당신은 오른쪽 선택을 더 좋아해요!"
    else:
        result = "⚖️ 당신은 완벽한 밸런스형이에요!"

    st.markdown(
        f"""
        <div class="result-card">

            <div class="category-label">
                {st.session_state.category}
            </div>

            <div class="result-title">
                🎉 게임 완료!
            </div>

            <p style="
                color:#6b7280;
                font-size:1.1rem;
            ">
                총 {total}개의 질문에 답했습니다.
            </p>

            <h2>
                {result}
            </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # 점수 표시

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="choice-card left-card">

                <div class="choice-text">
                    👈 LEFT
                </div>

                <div class="result-score">
                    {left_percent}%
                </div>

                <div>
                    {left_score}표
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="choice-card right-card">

                <div class="choice-text">
                    RIGHT 👉
                </div>

                <div class="result-score">
                    {right_percent}%
                </div>

                <div>
                    {right_score}표
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 같은 카테고리 다시 하기",
            use_container_width=True
        ):
            start_game(st.session_state.category)
            st.rerun()

    with col2:

        if st.button(
            "🏠 다른 게임 선택하기",
            use_container_width=True
        ):
            reset_game()
            st.rerun()
