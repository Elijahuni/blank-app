import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 설정
st.set_page_config(
    page_title="데이터 시각화 데모",
    page_icon="📊",
    layout="wide"
)

# 타이틀과 설명
st.title("📊 데이터 시각화 데모")
st.markdown("다양한 종류의 그래프를 살펴보세요!")

# 사이드바 생성
st.sidebar.header("그래프 설정")
chart_type = st.sidebar.selectbox(
    "그래프 종류 선택",
    ["선 그래프", "막대 그래프", "산점도", "파이 차트", "히트맵"]
)

# 샘플 데이터 생성
@st.cache_data
def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'date': dates,
        'sales': np.random.normal(100, 15, len(dates)),
        'visitors': np.random.normal(500, 50, len(dates)),
        'conversion_rate': np.random.uniform(0.1, 0.3, len(dates))
    }
    return pd.DataFrame(data)

df = generate_data()

# 컬럼 분할
col1, col2 = st.columns([2, 1])

with col1:
    if chart_type == "선 그래프":
        st.subheader("📈 시계열 데이터 트렌드")
        fig = px.line(df, x='date', y=['sales', 'visitors'], 
                     title='일별 판매량과 방문자 수 추이',
                     template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "막대 그래프":
        st.subheader("📊 월별 집계 데이터")
        monthly_data = df.set_index('date').resample('M').mean()
        fig = px.bar(monthly_data, 
                    title='월별 평균 판매량',
                    template='plotly_dark',
                    barmode='group')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "산점도":
        st.subheader("🎯 상관관계 분석")
        fig = px.scatter(df, x='visitors', y='sales', 
                        color='conversion_rate',
                        title='방문자 수와 판매량의 관계',
                        template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "파이 차트":
        st.subheader("🥧 분포 분석")
        quarterly_sales = df.set_index('date').resample('Q')['sales'].sum()
        fig = px.pie(values=quarterly_sales.values, 
                    names=quarterly_sales.index.strftime('%Y-Q%q'),
                    title='분기별 판매량 비중',
                    template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "히트맵":
        st.subheader("🌡️ 히트맵 분석")
        pivot_data = df.pivot_table(
            index=df.date.dt.day_name(),
            columns=df.date.dt.month,
            values='sales',
            aggfunc='mean'
        )
        fig = px.imshow(pivot_data,
                       title='요일/월별 평균 판매량 히트맵',
                       template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📝 데이터 통계")
    st.write("기본 통계량:")
    st.dataframe(df.describe())
    
    # 추가 분석 정보
    st.write("추가 정보:")
    st.metric(
        label="평균 일일 판매량",
        value=f"{df['sales'].mean():.2f}",
        delta=f"{df['sales'].std():.2f} (표준편차)"
    )
    st.metric(
        label="평균 전환율",
        value=f"{df['conversion_rate'].mean():.2%}",
        delta=f"{(df['conversion_rate'].max() - df['conversion_rate'].min()):.2%} (범위)"
    )

# 푸터
st.markdown("---")
st.markdown("### 📌 사용된 라이브러리")
st.markdown("""
- Streamlit
- Plotly Express
- Pandas
- NumPy
""")
