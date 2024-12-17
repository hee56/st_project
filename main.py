import streamlit as st

# MBTI 데이터 정의
mbti_info = {
    "INTJ": {
        "description": "독립적이고 전략적인 성향으로 계획을 세우는 데 탁월합니다.",
        "careers": "전략 컨설턴트, 데이터 분석가, 과학자, 엔지니어",
        "compatibility": "ENTP, ENFP와 잘 어울리며, 창의적인 아이디어를 나눌 수 있는 사람이 적합합니다."
    },
    "ENTP": {
        "description": "창의적이고 논쟁을 즐기는 성향으로 새로운 아이디어를 탐구합니다.",
        "careers": "기업가, 광고 기획자, 제품 디자이너",
        "compatibility": "INFJ, INTJ와 잘 어울리며, 깊은 대화를 나눌 수 있는 사람이 적합합니다."
    },
    "INFJ": {
        "description": "직관적이고 이상주의적인 성향으로 사람들을 돕는 데 열정적입니다.",
        "careers": "상담사, 작가, 심리학자, 사회운동가",
        "compatibility": "ENFP, ENTP와 잘 어울리며, 정서적으로 공감해주는 사람이 적합합니다."
    },
    # 더 많은 MBTI 추가 가능
}

# Streamlit UI
st.title("MBTI 기반 직업 및 이상적인 관계")
st.write("당신의 MBTI를 선택하면, 해당 유형에 적합한 직업과 잘 맞는 사람에 대해 알려드립니다.")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_info.keys()))

# MBTI 정보 표시
if mbti:
    st.subheader(f"당신의 MBTI: {mbti}")
    st.write(f"**특성:** {mbti_info[mbti]['description']}")
    st.write(f"**추천 직업:** {mbti_info[mbti]['careers']}")
    st.write(f"**잘 맞는 사람:** {mbti_info[mbti]['compatibility']}")
