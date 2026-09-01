import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="⚖️ 밸런스 게임",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# 게임 데이터
# =========================================================

QUESTIONS = {
    "🍕 음식": [
        {
            "question": "평생 하나만 먹는다면?",
            "left": {
                "title": "🍕 피자",
                "description": "치즈 듬뿍! 토핑 가득한 피자",
                "color": "#FF6B6B",
            },
            "right": {
                "title": "🍗 치킨",
                "description": "바삭바삭한 국민 야식 치킨",
                "color": "#FFA94D",
            },
        },
        {
            "question": "둘 중 하나만 선택한다면?",
            "left": {
                "title": "🍜 라면",
                "description": "매일 밤 먹어도 질리지 않는 라면",
                "color": "#FF8787",
            },
            "right": {
                "title": "🍔 햄버거",
                "description": "두툼한 패티와 풍성한 햄버거",
                "color": "#F08C46",
            },
        },
        {
            "question": "디저트 하나만 고른다면?",
            "left": {
                "title": "🍰 케이크",
                "description": "달콤하고 부드러운 생크림 케이크",
                "color": "#F783AC",
            },
            "right": {
                "title": "🍦 아이스크림",
                "description": "시원하고 달콤한 아이스크림",
                "color": "#74C0FC",
            },
        },
        {
            "question": "아침 메뉴로 하나만 먹는다면?",
            "left": {
                "title": "🥐 빵",
                "description": "따뜻한 빵과 커피 한 잔",
                "color": "#D99A5B",
            },
            "right": {
                "title": "🍚 밥",
                "description": "든든한 한식 아침 식사",
                "color": "#82C91E",
            },
        },
        {
            "question": "야식으로 하나만 선택한다면?",
            "left": {
                "title": "🌶️ 떡볶이",
                "description": "매콤달콤한 국민 야식",
                "color": "#FF6B6B",
            },
            "right": {
                "title": "🍗 치킨",
                "description": "바삭한 치킨과 시원한 콜라",
                "color": "#F59F00",
            },
        },
        {
            "question": "하나만 고른다면?",
            "left": {
                "title": "🍣 초밥",
                "description": "신선한 회와 밥의 완벽한 조합",
                "color": "#20C997",
            },
            "right": {
                "title": "🥩 스테이크",
                "description": "육즙 가득한 두툼한 스테이크",
                "color": "#C92A2A",
            },
        },
        {
            "question": "간식으로 더 좋은 것은?",
            "left": {
                "title": "🍪 과자",
                "description": "바삭바삭한 과자 한 봉지",
                "color": "#FCC419",
            },
            "right": {
                "title": "🍫 초콜릿",
                "description": "달콤한 초콜릿 한 조각",
                "color": "#795548",
            },
        },
    ],

    "🌈 주말": [
        {
            "question": "이번 주말에는?",
            "left": {
                "title": "🏠 집콕",
                "description": "침대에서 영화와 함께 푹 쉬기",
                "color": "#748FFC",
            },
            "right": {
                "title": "🌳 나들이",
                "description": "친구들과 밖으로 나가기",
                "color": "#51CF66",
            },
        },
        {
            "question": "주말에 더 끌리는 것은?",
            "left": {
                "title": "🎮 게임",
                "description": "하루 종일 게임하면서 놀기",
                "color": "#7950F2",
            },
            "right": {
                "title": "🎬 영화",
                "description": "극장에서 최신 영화 보기",
                "color": "#E64980",
            },
        },
        {
            "question": "주말 아침에는?",
            "left": {
                "title": "😴 늦잠",
                "description": "알람 없이 오후까지 자기",
                "color": "#5C7CFA",
            },
            "right": {
                "title": "☀️ 일찍 일어나기",
                "description": "아침부터 알차게 하루 보내기",
                "color": "#FAB005",
            },
        },
        {
            "question": "친구와 주말을 보낸다면?",
            "left": {
                "title": "☕ 카페",
                "description": "조용한 카페에서 수다 떨기",
                "color": "#A67C52",
            },
            "right": {
                "title": "🎳 놀러가기",
                "description": "볼링이나 방탈출 즐기기",
                "color": "#20C997",
            },
        },
        {
            "question": "완벽한 주말은?",
            "left": {
                "title": "📚 혼자",
                "description": "혼자만의 시간을 여유롭게 보내기",
                "color": "#845EF7",
            },
            "right": {
                "title": "👯 친구",
                "description": "친구들과 하루 종일 놀기",
                "color": "#FF922B",
            },
        },
        {
            "question": "주말 저녁에는?",
            "left": {
                "title": "🍺 맛집",
                "description": "맛있는 음식 먹으러 가기",
                "color": "#F08C46",
            },
            "right": {
                "title": "🛋️ 휴식",
                "description": "집에서 편하게 쉬기",
                "color": "#748FFC",
            },
        },
        {
            "question": "주말에 하나만 한다면?",
            "left": {
                "title": "🏋️ 운동",
                "description": "땀 흘리며 운동하기",
                "color": "#40C057",
            },
            "right": {
                "title": "😴 낮잠",
                "description": "부족했던 잠을 실컷 자기",
                "color": "#9775FA",
            },
        },
    ],

    "✈️ 여행": [
        {
            "question": "휴가를 간다면?",
            "left": {
                "title": "🏖️ 바다",
                "description": "푸른 바다에서 여유로운 휴가",
                "color": "#339AF0",
            },
            "right": {
                "title": "🏔️ 산",
                "description": "시원한 공기의 산속 여행",
                "color": "#40C057",
            },
        },
        {
            "question": "해외여행을 간다면?",
            "left": {
                "title": "🇯🇵 일본",
                "description": "맛있는 음식과 온천 여행",
                "color": "#FF8787",
            },
            "right": {
                "title": "🇫🇷 프랑스",
                "description": "파리와 유럽 감성 여행",
                "color": "#748FFC",
            },
        },
        {
            "question": "여행 스타일은?",
            "left": {
                "title": "🗺️ 계획 여행",
                "description": "분 단위로 완벽하게 계획하기",
                "color": "#339AF0",
            },
            "right": {
                "title": "🎒 즉흥 여행",
                "description": "발길 닿는 대로 자유롭게 떠나기",
                "color": "#20C997",
            },
        },
        {
            "question": "숙소를 고른다면?",
            "left": {
                "title": "🏨 호텔",
                "description": "편안하고 깔끔한 호텔",
                "color": "#5C7CFA",
            },
            "right": {
                "title": "🏡 펜션",
                "description": "자연 속 아늑한 숙소",
                "color": "#82C91E",
            },
        },
        {
            "question": "여행에서 더 중요한 것은?",
            "left": {
                "title": "📸 관광",
                "description": "유명한 장소를 최대한 많이 보기",
                "color": "#F06595",
            },
            "right": {
                "title": "😌 휴식",
                "description": "아무것도 안 하고 푹 쉬기",
                "color": "#63E6BE",
            },
        },
        {
            "question": "여행을 누구와 간다면?",
            "left": {
                "title": "👫 친구",
                "description": "친한 친구들과 신나는 여행",
                "color": "#FF922B",
            },
            "right": {
                "title": "❤️ 연인",
                "description": "사랑하는 사람과 로맨틱한 여행",
                "color": "#F06595",
            },
        },
        {
            "question": "여행 중 하나만 한다면?",
            "left": {
                "title": "🍽️ 맛집 투어",
                "description": "현지 맛집을 찾아다니기",
                "color": "#FF6B6B",
            },
            "right": {
                "title": "📷 관광지 투어",
                "description": "유명 관광지를 돌아다니기",
                "color": "#339AF0",
            },
        },
    ],
}


# =========================================================
# 세션 상태
# =========================================================

if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "category" not in st.session_state:
    st.session_state.category = None

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* 전체 페이지 */
    .stApp {
        background:
            radial-gradient(
                circle at 0% 0%,
                rgba(124, 92, 255, 0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 100% 0%,
                rgba(255, 107, 107, 0.10),
                transparent 30%
            ),
            #F8F9FC;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 45px;
        padding-bottom: 70px;
    }

    /* 기본 버튼 */
    .stButton > button {
        width: 100%;
        min-height: 52px;
        border-radius: 15px;
        border: none;
        font-size: 16px;
        font-weight: 800;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* 홈 */
    .main-title {
        text-align: center;
        font-size: 52px;
        font-weight: 900;
        color: #171717;
        margin-bottom: 8px;
        letter-spacing: -2px;
    }

    .main-subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 45px;
    }

    .category-card {
        background: rgba(255,255,255,0.95);
        border-radius: 28px;
        padding: 35px 25px;
        text-align: center;
        border: 1px solid #eeeeee;
        box-shadow: 0 15px 40px rgba(0,0,0,0.07);
        min-height: 230px;
    }

    .category-icon {
        font-size: 58px;
        margin-bottom: 15px;
    }

    .category-title {
        font-size: 25px;
        font-weight: 900;
        color: #222;
        margin-bottom: 10px;
    }

    .category-description {
        color: #888;
        font-size: 14px;
        line-height: 1.6;
    }

    /* 게임 상단 */
    .game-header {
        text-align: center;
        color: #7C3AED;
        font-size: 15px;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .question-title {
        text-align: center;
        font-size: 40px;
        font-weight: 900;
        color: #171717;
        margin-bottom: 35px;
        letter-spacing: -1px;
    }

    .progress-label {
        text-align: center;
        color: #888;
        font-size: 14px;
        margin-top: 8px;
        margin-bottom: 25px;
    }

    /* 게임 카드 */
    .game-card {
        min-height: 350px;
        border-radius: 30px;
        padding: 35px 25px;
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 0 20px 45px rgba(0,0,0,0.14);
    }

    .card-title {
        font-size: 38px;
        font-weight: 900;
        margin-bottom: 15px;
    }

    .card-description {
        font-size: 16px;
        line-height: 1.7;
        opacity: 0.95;
    }

    .vs {
        height: 350px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888;
        font-size: 28px;
        font-weight: 900;
    }

    /* 결과 */
    .result-card {
        background: white;
        border-radius: 30px;
        padding: 45px 30px;
        text-align: center;
        box-shadow: 0 18px 45px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }

    .result-emoji {
        font-size: 70px;
    }

    .result-title {
        font-size: 36px;
        font-weight: 900;
        margin-top: 10px;
        color: #222;
    }

    .result-subtitle {
        color: #888;
        margin-top: 10px;
    }

    .answer-item {
        background: white;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 12px;
        border: 1px solid #eeeeee;
    }

    .answer-number {
        color: #999;
        font-size: 12px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .answer-question {
        color: #333;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .answer-value {
        color: #7C3AED;
        font-size: 19px;
        font-weight: 900;
    }

    /* 모바일 */
    @media (max-width: 768px) {

        .block-container {
            padding-top: 25px;
        }

        .main-title {
            font-size: 38px;
        }

        .question-title {
            font-size: 28px;
        }

        .game-card {
            min-height: 260px;
        }

        .card-title {
            font-size: 30px;
        }

        .vs {
            height: 60px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 함수
# =========================================================

def start_game(category):
    st.session_state.screen = "game"
    st.session_state.category = category
    st.session_state.question_index = 0
    st.session_state.answers = []


def choose_answer(side):
    category = st.session_state.category
    index = st.session_state.question_index

    question = QUESTIONS[category][index]
    selected = question[side]

    st.session_state.answers.append(
        {
            "question": question["question"],
            "answer": selected["title"],
        }
    )

    if index + 1 >= len(QUESTIONS[category]):
        st.session_state.screen = "result"
    else:
        st.session_state.question_index += 1


def go_home():
    st.session_state.screen = "home"
    st.session_state.category = None
    st.session_state.question_index = 0
    st.session_state.answers = []


def restart_game():
    category = st.session_state.category

    st.session_state.screen = "game"
    st.session_state.question_index = 0
    st.session_state.answers = []


# =========================================================
# HOME
# =========================================================

if st.session_state.screen == "home":

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">'
        '둘 중 하나만 선택할 수 있다면? 🤔'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### 🎮 게임 종류를 선택하세요")

    st.write("")

    category_info = [
        (
            "🍕 음식",
            "맛있는 음식 중 하나만 선택한다면?",
            "🍕 🍗 🍔 🍰",
        ),
        (
            "🌈 주말",
            "당신의 완벽한 주말은?",
            "🏠 🎮 🎬 🌳",
        ),
        (
            "✈️ 여행",
            "어디로 떠나고 싶나요?",
            "🏖️ 🏔️ 🇯🇵 🇫🇷",
        ),
    ]

    cols = st.columns(3, gap="large")

    for i, (category, description, icons) in enumerate(category_info):

        with cols[i]:

            st.markdown(
                f"""
                <div class="category-card">

                    <div class="category-icon">
                        {icons}
                    </div>

                    <div class="category-title">
                        {category}
                    </div>

                    <div class="category-description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write("")

            if st.button(
                f"{category} 게임 시작",
                key=f"start_{i}",
                use_container_width=True,
            ):
                start_game(category)
                st.rerun()

    st.write("")
    st.write("")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#999;
            font-size:14px;
        ">
            친구와 함께 하면 더 재미있어요 😎
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# GAME
# =========================================================

elif st.session_state.screen == "game":

    category = st.session_state.category
    index = st.session_state.question_index

    questions = QUESTIONS[category]
    question = questions[index]

    total = len(questions)
    current = index + 1

    # 상단
    top_left, top_right = st.columns([5, 1])

    with top_left:
        st.markdown(
            f"### {category}"
        )

    with top_right:
        if st.button("🏠 나가기"):
            go_home()
            st.rerun()

    # 진행률
    progress = current / total

    st.progress(progress)

    st.markdown(
        f"""
        <div class="progress-label">
            {current} / {total}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 질문
    st.markdown(
        f"""
        <div class="game-header">
            QUESTION {current}
        </div>

        <div class="question-title">
            {question["question"]}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 카드
    left_col, vs_col, right_col = st.columns(
        [5, 1, 5],
        gap="small",
    )

    # 왼쪽
    with left_col:

        left = question["left"]

        st.markdown(
            f"""
            <div class="game-card"
                 style="
                    background:
                    linear-gradient(
                        135deg,
                        rgba(255,255,255,0.12),
                        rgba(0,0,0,0.10)
                    ),
                    {left["color"]};
                 ">

                <div class="card-title">
                    {left["title"]}
                </div>

                <div class="card-description">
                    {left["description"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        if st.button(
            "👈 이것을 선택",
            key=f"left_{category}_{index}",
            use_container_width=True,
        ):
            choose_answer("left")
            st.rerun()

    # VS
    with vs_col:

        st.markdown(
            """
            <div class="vs">
                VS
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 오른쪽
    with right_col:

        right = question["right"]

        st.markdown(
            f"""
            <div class="game-card"
                 style="
                    background:
                    linear-gradient(
                        135deg,
                        rgba(255,255,255,0.12),
                        rgba(0,0,0,0.10)
                    ),
                    {right["color"]};
                 ">

                <div class="card-title">
                    {right["title"]}
                </div>

                <div class="card-description">
                    {right["description"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        if st.button(
            "이것을 선택 👉",
            key=f"right_{category}_{index}",
            use_container_width=True,
        ):
            choose_answer("right")
            st.rerun()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.screen == "result":

    category = st.session_state.category
    answers = st.session_state.answers

    st.markdown(
        """
        <div class="main-title">
            🎉 게임 완료!
        </div>

        <div class="main-subtitle">
            당신의 선택을 확인해보세요.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-emoji">
                🏆
            </div>

            <div class="result-title">
                {category} 밸런스 게임 완료!
            </div>

            <div class="result-subtitle">
                총 {len(answers)}개의 질문에 답했습니다.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📋 나의 선택")

    for i, answer in enumerate(answers):

        st.markdown(
            f"""
            <div class="answer-item">

                <div class="answer-number">
                    QUESTION {i + 1}
                </div>

                <div class="answer-question">
                    {answer["question"]}
                </div>

                <div class="answer-value">
                    👉 {answer["answer"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 다시 하기",
            use_container_width=True,
        ):
            restart_game()
            st.rerun()

    with col2:

        if st.button(
            "🏠 다른 게임 선택",
            use_container_width=True,
        ):
            go_home()
            st.rerun()
