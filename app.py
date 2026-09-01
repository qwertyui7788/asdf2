import streamlit as st
import random

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide"
)

# --------------------------------------------------
# 게임 데이터
# --------------------------------------------------

GAME_DATA = {
    "🍔 음식": [
        ("평생 하나만 먹어야 한다면?", "🍗 치킨", "🍕 피자"),
        ("더 좋아하는 면 요리는?", "🍜 라면", "🍝 파스타"),
        ("디저트 하나만 고른다면?", "🍦 아이스크림", "🍰 케이크"),
        ("야식으로 더 좋은 것은?", "🌶️ 떡볶이", "🍗 치킨"),
        ("아침으로 먹는다면?", "🥪 샌드위치", "🍚 한식"),
        ("여름에 먹고 싶은 것은?", "🍉 수박", "🍧 빙수"),
        ("커피와 함께 먹는다면?", "🥐 크루아상", "🍩 도넛"),
        ("회식 메뉴를 고른다면?", "🥩 소고기", "🐷 삼겹살"),
    ],

    "🏖️ 주말": [
        ("주말에 더 하고 싶은 것은?", "🏠 집에서 쉬기", "🚗 드라이브"),
        ("주말 여행을 간다면?", "🌊 바다", "⛰️ 산"),
        ("토요일 밤에는?", "🎬 영화 보기", "🎮 게임하기"),
        ("친구와 만난다면?", "🍽️ 맛집 가기", "☕ 카페 가기"),
        ("아침에 일어나서?", "😴 다시 자기", "🏃 운동하기"),
        ("주말 하루 종일 한다면?", "📺 넷플릭스", "📚 독서"),
        ("저녁에 한다면?", "🍻 술 한잔", "🍵 카페"),
        ("혼자 보내는 주말이라면?", "🎮 게임", "🎧 음악"),
    ],

    "✈️ 여행": [
        ("지금 바로 떠난다면?", "🇯🇵 일본", "🇹🇭 태국"),
        ("휴양 여행이라면?", "🏝️ 몰디브", "🌴 하와이"),
        ("도시 여행이라면?", "🇫🇷 파리", "🇺🇸 뉴욕"),
        ("겨울 여행이라면?", "⛷️ 스위스", "❄️ 삿포로"),
        ("한 달 살아본다면?", "🇪🇸 스페인", "🇵🇹 포르투갈"),
        ("여름 휴가라면?", "🇬🇷 그리스", "🇮🇹 이탈리아"),
        ("혼자 여행한다면?", "🇯🇵 도쿄", "🇹🇼 타이베이"),
        ("친구와 여행한다면?", "🇻🇳 베트남", "🇹🇭 태국"),
    ],

    "🎬 영화": [
        ("더 좋아하는 영화 장르는?", "💥 액션", "💕 로맨스"),
        ("영화관에서 본다면?", "👻 공포", "🤣 코미디"),
        ("몰아보기 좋은 영화는?", "🦸 히어로", "🕵️ 추리"),
        ("주인공이 된다면?", "🦸 영웅", "💰 부자"),
        ("더 좋아하는 것은?", "🚀 SF", "🐉 판타지"),
        ("영화 볼 때?", "🍿 팝콘", "🍕 피자"),
    ],

    "💘 연애": [
        ("더 중요한 것은?", "💬 대화가 잘 통하는 사람", "❤️ 외모가 이상형인 사람"),
        ("데이트 장소는?", "🍽️ 맛집", "🎡 놀이공원"),
        ("연애에서 중요한 것은?", "😂 재미", "🤝 신뢰"),
        ("연락 스타일은?", "📱 자주 연락", "😌 적당히 연락"),
        ("여행을 간다면?", "🏖️ 휴양지", "🏙️ 도시 여행"),
        ("기념일에는?", "🎁 선물", "🍽️ 특별한 식사"),
    ],

    "💰 돈 & 인생": [
        ("평생 하나만 선택한다면?", "💰 돈 많은 삶", "❤️ 사랑 많은 삶"),
        ("직업을 고른다면?", "🏠 재택근무", "🏢 출근"),
        ("시간과 돈 중 하나를 가진다면?", "⏰ 시간", "💵 돈"),
        ("성공한다면?", "⭐ 유명해지기", "💰 부자 되기"),
        ("하루를 다시 산다면?", "🌅 아침형 인간", "🌙 밤형 인간"),
    ],
}


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #fff5f7 0%,
            #f5f3ff 50%,
            #eef6ff 100%
        );
    }

    .block-container {
        max-width: 1100px;
        padding-top: 35px;
    }

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #171717;
        margin-bottom: 5px;
    }

    .main-subtitle {
        text-align: center;
        font-size: 18px;
        color: #777;
        margin-bottom: 35px;
    }

    .category-card {
        background: white;
        padding: 30px 20px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.07);
        margin-bottom: 12px;
    }

    .category-icon {
        font-size: 50px;
        margin-bottom: 10px;
    }

    .category-name {
        font-size: 22px;
        font-weight: 800;
    }

    .category-count {
        color: #999;
        margin-top: 5px;
    }

    .question-card {
        background: rgba(255,255,255,0.9);
        padding: 35px;
        border-radius: 28px;
        text-align: center;
        box-shadow: 0 12px 35px rgba(0,0,0,0.07);
        margin-bottom: 25px;
    }

    .question-number {
        color: #7357ff;
        font-size: 15px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .question-text {
        font-size: 30px;
        font-weight: 900;
        color: #222;
    }

    .choice-left {
        background: linear-gradient(
            135deg,
            #ff6b6b,
            #ff416c
        );
        color: white;
        min-height: 240px;
        border-radius: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(255,65,108,0.25);
    }

    .choice-right {
        background: linear-gradient(
            135deg,
            #4facfe,
            #6a5cff
        );
        color: white;
        min-height: 240px;
        border-radius: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(80,80,255,0.25);
    }

    .choice-text {
        font-size: 28px;
        font-weight: 900;
    }

    .vs {
        height: 240px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 900;
        color: #999;
    }

    .result-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    }

    .result-title {
        font-size: 40px;
        font-weight: 900;
    }

    .answer-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    }

    @media (max-width: 700px) {

        .main-title {
            font-size: 36px;
        }

        .question-text {
            font-size: 23px;
        }

        .choice-left,
        .choice-right {
            min-height: 170px;
        }

        .choice-text {
            font-size: 22px;
        }

        .vs {
            height: 50px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "category" not in st.session_state:
    st.session_state.category = None

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = []


# --------------------------------------------------
# 게임 시작
# --------------------------------------------------

def start_game(category):

    questions = GAME_DATA[category].copy()

    random.shuffle(questions)

    st.session_state.category = category
    st.session_state.questions = questions
    st.session_state.current = 0
    st.session_state.answers = []
    st.session_state.page = "game"


# --------------------------------------------------
# 답변
# --------------------------------------------------

def answer(choice):

    st.session_state.answers.append(choice)
    st.session_state.current += 1

    if st.session_state.current >= len(
        st.session_state.questions
    ):
        st.session_state.page = "result"


# --------------------------------------------------
# 홈 화면
# --------------------------------------------------

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">⚖️ 밸런스 게임</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        '둘 중 하나만 선택할 수 있다면?'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("🎮 카테고리를 선택하세요")

    categories = list(GAME_DATA.keys())

    for row_start in range(0, len(categories), 3):

        row = categories[row_start:row_start + 3]

        cols = st.columns(3)

        for i, category in enumerate(row):

            with cols[i]:

                icon = category.split()[0]
                name = " ".join(category.split()[1:])

                st.markdown(
                    f"""
                    <div class="category-card">

                        <div class="category-icon">
                            {icon}
                        </div>

                        <div class="category-name">
                            {name}
                        </div>

                        <div class="category-count">
                            {len(GAME_DATA[category])}개의 질문
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"{name} 시작",
                    key=f"category_{category}",
                    use_container_width=True
                ):
                    start_game(category)
                    st.rerun()


# --------------------------------------------------
# 게임 화면
# --------------------------------------------------

elif st.session_state.page == "game":

    category = st.session_state.category
    questions = st.session_state.questions
    current = st.session_state.current

    question, left, right = questions[current]

    total = len(questions)

    st.markdown(
        f"""
        <div class="main-title">
            {category}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(current / total)

    st.markdown(
        f"""
        <div class="question-card">

            <div class="question-number">
                QUESTION {current + 1} / {total}
            </div>

            <div class="question-text">
                {question}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    left_col, middle_col, right_col = st.columns(
        [5, 1, 5]
    )

    with left_col:

        st.markdown(
            f"""
            <div class="choice-left">

                <div class="choice-text">
                    {left}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "👈 왼쪽 선택",
            key=f"left_{current}",
            use_container_width=True
        ):
            answer(left)
            st.rerun()

    with middle_col:

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
            <div class="choice-right">

                <div class="choice-text">
                    {right}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "오른쪽 선택 👉",
            key=f"right_{current}",
            use_container_width=True
        ):
            answer(right)
            st.rerun()

    st.write("")

    if st.button(
        "🏠 게임 종료",
        use_container_width=True
    ):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# 결과 화면
# --------------------------------------------------

elif st.session_state.page == "result":

    st.markdown(
        """
        <div class="result-card">

            <div class="result-title">
                🎉 게임 완료!
            </div>

            <p>
                당신의 선택을 확인해보세요.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    for i, choice in enumerate(
        st.session_state.answers
    ):

        question = st.session_state.questions[i][0]

        st.markdown(
            f"""
            <div class="answer-card">

                <div style="
                    color:#999;
                    font-size:14px;
                ">
                    Q{i + 1}
                </div>

                <div style="
                    font-weight:700;
                    margin:5px 0;
                ">
                    {question}
                </div>

                <div style="
                    color:#6a5cff;
                    font-size:20px;
                    font-weight:900;
                ">
                    👉 {choice}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 다시 하기",
            use_container_width=True
        ):
            start_game(
                st.session_state.category
            )
            st.rerun()

    with col2:

        if st.button(
            "🏠 다른 게임",
            use_container_width=True
        ):
            st.session_state.page = "home"
            st.rerun()
