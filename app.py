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

GAMES = {
    "🍔 음식": [
        {
            "question": "평생 하나만 먹는다면?",
            "left": "🍗 치킨",
            "right": "🍕 피자",
        },
        {
            "question": "더 좋아하는 음식은?",
            "left": "🍜 라면",
            "right": "🍝 파스타",
        },
        {
            "question": "간식 하나만 고른다면?",
            "left": "🍫 초콜릿",
            "right": "🍦 아이스크림",
        },
        {
            "question": "아침 식사로 더 좋은 것은?",
            "left": "🥪 샌드위치",
            "right": "🍚 든든한 한식",
        },
        {
            "question": "야식으로 더 끌리는 것은?",
            "left": "🌶️ 매운 떡볶이",
            "right": "🍗 후라이드 치킨",
        },
        {
            "question": "여름에 먹고 싶은 것은?",
            "left": "🍉 수박",
            "right": "🍧 팥빙수",
        },
    ],

    "🏖️ 주말": [
        {
            "question": "주말에 더 하고 싶은 것은?",
            "left": "🏠 집에서 푹 쉬기",
            "right": "🚗 근교로 드라이브",
        },
        {
            "question": "주말 여행을 간다면?",
            "left": "🌊 바다",
            "right": "⛰️ 산",
        },
        {
            "question": "토요일 밤에는?",
            "left": "🎬 영화 보기",
            "right": "🎮 게임하기",
        },
        {
            "question": "친구와 주말에 만나면?",
            "left": "🍻 맛집 투어",
            "right": "☕ 카페 투어",
        },
        {
            "question": "주말 아침에 일어나서?",
            "left": "😴 다시 자기",
            "right": "🏃 운동하기",
        },
    ],

    "✈️ 여행": [
        {
            "question": "지금 바로 떠난다면?",
            "left": "🇯🇵 일본",
            "right": "🇹🇭 태국",
        },
        {
            "question": "휴양 여행을 간다면?",
            "left": "🏝️ 몰디브",
            "right": "🌴 하와이",
        },
        {
            "question": "도시 여행을 간다면?",
            "left": "🇫🇷 파리",
            "right": "🇺🇸 뉴욕",
        },
        {
            "question": "겨울 여행을 간다면?",
            "left": "⛷️ 스위스",
            "right": "❄️ 삿포로",
        },
        {
            "question": "한 달 동안 살아본다면?",
            "left": "🇪🇸 스페인",
            "right": "🇵🇹 포르투갈",
        },
    ],

    "🎬 영화": [
        {
            "question": "더 좋아하는 영화 장르는?",
            "left": "💥 액션",
            "right": "💕 로맨스",
        },
        {
            "question": "영화관에서 본다면?",
            "left": "👻 공포영화",
            "right": "🤣 코미디",
        },
        {
            "question": "주말에 몰아본다면?",
            "left": "🦸 히어로 영화",
            "right": "🕵️ 추리 영화",
        },
        {
            "question": "영화 주인공이 된다면?",
            "left": "🦸 세상을 구하는 영웅",
            "right": "💰 엄청난 부자",
        },
    ],

    "💘 연애": [
        {
            "question": "더 중요한 것은?",
            "left": "💬 대화가 잘 통하는 사람",
            "right": "❤️ 외모가 이상형인 사람",
        },
        {
            "question": "데이트 장소를 고른다면?",
            "left": "🍽️ 분위기 좋은 레스토랑",
            "right": "🎡 놀이공원",
        },
        {
            "question": "연애할 때 더 중요한 것은?",
            "left": "😂 재미",
            "right": "🤝 신뢰",
        },
    ],
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
                #fff4f4 0%,
                #f7f7ff 35%,
                #eef3ff 100%
            );
    }

    /* 상단 여백 */
    .main .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* 제목 */
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #171717;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* 카테고리 */
    .category-title {
        text-align: center;
        font-size: 25px;
        font-weight: 800;
        margin-bottom: 20px;
    }

    /* 질문 */
    .question-box {
        background: rgba(255,255,255,0.8);
        border-radius: 24px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 35px rgba(0,0,0,0.06);
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.8);
    }

    .question-number {
        color: #8b5cf6;
        font-weight: 700;
        font-size: 15px;
        margin-bottom: 10px;
    }

    .question {
        font-size: 30px;
        font-weight: 900;
        color: #222;
    }

    /* 카드 */
    .card {
        border-radius: 28px;
        min-height: 230px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 30px;
        color: white;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        transition: transform 0.2s;
    }

    .card-left {
        background: linear-gradient(
            135deg,
            #ff6b6b,
            #ff416c
        );
    }

    .card-right {
        background: linear-gradient(
            135deg,
            #4facfe,
            #6a5cff
        );
    }

    .card-title {
        font-size: 30px;
        font-weight: 900;
    }

    .card-description {
        font-size: 14px;
        opacity: 0.85;
        margin-top: 8px;
    }

    /* OR */
    .or {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        font-size: 22px;
        font-weight: 900;
        color: #999;
    }

    /* 진행률 */
    .progress-text {
        text-align: center;
        color: #777;
        margin-top: 25px;
    }

    /* 결과 */
    .result-box {
        background: white;
        border-radius: 30px;
        padding: 45px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    }

    .result-title {
        font-size: 38px;
        font-weight: 900;
        margin-bottom: 15px;
    }

    .result-description {
        color: #777;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* 모바일 */
    @media (max-width: 700px) {

        .title {
            font-size: 35px;
        }

        .question {
            font-size: 24px;
        }

        .card {
            min-height: 170px;
        }

        .card-title {
            font-size: 24px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Session State 초기화
# =========================================================

if "category" not in st.session_state:
    st.session_state.category = None

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "started" not in st.session_state:
    st.session_state.started = False

if "finished" not in st.session_state:
    st.session_state.finished = False


# =========================================================
# 게임 시작
# =========================================================

def start_game(category):

    st.session_state.category = category

    # 문제 순서를 랜덤으로 섞기
    questions = GAMES[category].copy()
    random.shuffle(questions)

    st.session_state.questions = questions
    st.session_state.current = 0
    st.session_state.answers = []
    st.session_state.started = True
    st.session_state.finished = False


# =========================================================
# 답변 선택
# =========================================================

def select_answer(answer):

    st.session_state.answers.append(answer)

    st.session_state.current += 1

    if st.session_state.current >= len(
        st.session_state.questions
    ):
        st.session_state.finished = True


# =========================================================
# 게임 초기화
# =========================================================

def reset_game():

    st.session_state.category = None
    st.session_state.questions = []
    st.session_state.current = 0
    st.session_state.answers = []
    st.session_state.started = False
    st.session_state.finished = False


# =========================================================
# 헤더
# =========================================================

st.markdown(
    '<div class="title">⚖️ 밸런스 게임</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '둘 중 하나만 선택할 수 있다면? 당신의 선택은?'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 게임 시작 전
# =========================================================

if not st.session_state.started:

    st.markdown(
        '<div class="category-title">'
        '🎮 게임 카테고리를 선택하세요'
        '</div>',
        unsafe_allow_html=True
    )

    categories = list(GAMES.keys())

    # 3열 카드
    cols = st.columns(3)

    for index, category in enumerate(categories):

        with cols[index % 3]:

            st.markdown(
                f"""
                <div class="question-box">
                    <div style="
                        font-size:45px;
                        margin-bottom:10px;
                    ">
                        {category.split()[0]}
                    </div>

                    <div style="
                        font-size:20px;
                        font-weight:800;
                    ">
                        {" ".join(category.split()[1:])}
                    </div>

                    <div style="
                        color:#999;
                        margin-top:8px;
                    ">
                        {len(GAMES[category])}개의 질문
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"{category} 시작",
                key=f"start_{index}",
                use_container_width=True
            ):
                start_game(category)
                st.rerun()

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#999;
            margin-top:20px;
        ">
        💡 친구와 함께 서로의 선택을 비교해보세요!
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 게임 진행
# =========================================================

elif st.session_state.started and not st.session_state.finished:

    questions = st.session_state.questions
    current = st.session_state.current
    question = questions[current]

    total = len(questions)

    # 카테고리
    st.markdown(
        f"""
        <div class="category-title">
            {st.session_state.category}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 질문
    st.markdown(
        f"""
        <div class="question-box">

            <div class="question-number">
                QUESTION {current + 1} / {total}
            </div>

            <div class="question">
                {question["question"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # 진행률
    st.progress(
        current / total
    )

    # 카드
    left_col, or_col, right_col = st.columns(
        [5, 1, 5]
    )

    with left_col:

        st.markdown(
            f"""
            <div class="card card-left">

                <div class="card-title">
                    {question["left"]}
                </div>

                <div class="card-description">
                    왼쪽을 선택하세요
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "👈 이것을 선택",
            key=f"left_{current}",
            use_container_width=True
        ):
            select_answer(question["left"])
            st.rerun()

    with or_col:

        st.markdown(
            """
            <div class="or">
                VS
            </div>
            """,
            unsafe_allow_html=True
        )

    with right_col:

        st.markdown(
            f"""
            <div class="card card-right">

                <div class="card-title">
                    {question["right"]}
                </div>

                <div class="card-description">
                    오른쪽을 선택하세요
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "이것을 선택 👉",
            key=f"right_{current}",
            use_container_width=True
        ):
            select_answer(question["right"])
            st.rerun()

    st.markdown(
        f"""
        <div class="progress-text">
            현재 {current + 1}번째 질문입니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    if st.button(
        "게임 나가기",
        use_container_width=True
    ):
        reset_game()
        st.rerun()


# =========================================================
# 결과
# =========================================================

elif st.session_state.finished:

    answers = st.session_state.answers

    st.markdown(
        """
        <div class="result-box">

            <div class="result-title">
                🎉 게임 완료!
            </div>

            <div class="result-description">
                당신의 선택을 확인해보세요.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # 선택 결과 표시
    for index, answer in enumerate(answers):

        question = st.session_state.questions[index]

        st.markdown(
            f"""
            <div class="question-box">

                <div style="
                    color:#999;
                    font-size:14px;
                    margin-bottom:8px;
                ">
                    Q{index + 1}. {question["question"]}
                </div>

                <div style="
                    font-size:22px;
                    font-weight:900;
                    color:#6a5cff;
                ">
                    {answer}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("")

    # 다시 하기
    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 다시 하기",
            use_container_width=True
        ):
            start_game(st.session_state.category)
            st.rerun()

    with col2:

        if st.button(
            "🏠 카테고리 선택",
            use_container_width=True
        ):
            reset_game()
            st.rerun()
