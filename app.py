import streamlit as st
import random

# ==================================================
# 페이지 설정
# ==================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide"
)


# ==================================================
# 게임 데이터
# ==================================================

GAMES = {
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


# ==================================================
# Session State
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "category" not in st.session_state:
    st.session_state.category = ""

if "questions" not in st.session_state:
    st.session_state.questions = []

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []


# ==================================================
# 함수
# ==================================================

def start_game(category):
    questions = GAMES[category].copy()

    random.shuffle(questions)

    st.session_state.category = category
    st.session_state.questions = questions
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.page = "game"


def select_answer(answer):
    st.session_state.answers.append(answer)

    st.session_state.question_index += 1

    if st.session_state.question_index >= len(
        st.session_state.questions
    ):
        st.session_state.page = "result"


def go_home():
    st.session_state.page = "home"
    st.session_state.category = ""
    st.session_state.questions = []
    st.session_state.question_index = 0
    st.session_state.answers = []


# ==================================================
# 공통 제목
# ==================================================

st.title("⚖️ 밸런스 게임")

st.caption("둘 중 하나만 선택할 수 있다면? 당신의 선택은?")


# ==================================================
# HOME
# ==================================================

if st.session_state.page == "home":

    st.header("🎮 게임을 선택하세요")

    st.write("")

    categories = list(GAMES.keys())

    # 3개씩 배치
    for i in range(0, len(categories), 3):

        cols = st.columns(3)

        for j, category in enumerate(
            categories[i:i + 3]
        ):

            with cols[j]:

                st.subheader(category)

                st.write(
                    f"질문 {len(GAMES[category])}개"
                )

                if st.button(
                    "게임 시작",
                    key=f"start_{category}",
                    use_container_width=True
                ):
                    start_game(category)
                    st.rerun()


# ==================================================
# GAME
# ==================================================

elif st.session_state.page == "game":

    category = st.session_state.category

    questions = st.session_state.questions

    index = st.session_state.question_index

    question, left, right = questions[index]

    total = len(questions)

    # 카테고리
    st.header(category)

    # 진행률
    st.progress(
        index / total
    )

    st.caption(
        f"QUESTION {index + 1} / {total}"
    )

    # 질문
    st.subheader(question)

    st.write("")

    # 선택 카드
    left_col, middle_col, right_col = st.columns(
        [5, 1, 5]
    )

    with left_col:

        st.info(
            f"# {left}"
        )

        if st.button(
            "👈 왼쪽 선택",
            key=f"left_{index}",
            use_container_width=True
        ):
            select_answer(left)
            st.rerun()

    with middle_col:

        st.markdown(
            "<h2 style='text-align:center'>VS</h2>",
            unsafe_allow_html=True
        )

    with right_col:

        st.success(
            f"# {right}"
        )

        if st.button(
            "오른쪽 선택 👉",
            key=f"right_{index}",
            use_container_width=True
        ):
            select_answer(right)
            st.rerun()

    st.write("")

    if st.button(
        "🏠 게임 종료",
        use_container_width=True
    ):
        go_home()
        st.rerun()


# ==================================================
# RESULT
# ==================================================

elif st.session_state.page == "result":

    st.header("🎉 게임 완료!")

    st.write(
        f"당신의 선택 결과입니다."
    )

    st.write("")

    for i, answer in enumerate(
        st.session_state.answers
    ):

        question = st.session_state.questions[i][0]

        st.subheader(
            f"Q{i + 1}. {question}"
        )

        st.success(
            f"👉 {answer}"
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

            go_home()
            st.rerun()
