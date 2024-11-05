import streamlit as st

# 제목 표시
st.title('Streamlit 버튼 예제')

# 1. 간단한 버튼
st.header('1. 기본 버튼')
if st.button('Click me!'):
    st.write('버튼이 클릭되었습니다!')

# 2. 텍스트 입력
st.header('2. 텍스트 입력')
name = st.text_input('이름을 입력하세요:')
if st.button('인사하기'):
    if name:
        st.write(f'안녕하세요, {name}님!')
    else:
        st.write('이름을 입력해주세요.')

# 3. 숫자 입력
st.header('3. 숫자 입력')
number = st.number_input('숫자를 입력하세요:', value=0)
if st.button('제곱 계산'):
    st.write(f'{number} × {number} = {number ** 2}')

# 4. 체크박스
st.header('4. 체크박스')
if st.checkbox('추가 정보 보기'):
    st.write('여기에 추가 정보가 표시됩니다!')

# 5. 선택박스
st.header('5. 선택박스')
option = st.selectbox(
    '좋아하는 색상을 선택하세요:',
    ['빨강', '파랑', '초록', '노랑']
)
if st.button('색상 확인'):
    st.write(f'당신이 선택한 색상은 {option}입니다.')
