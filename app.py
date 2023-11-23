import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    st.title("자동차 데이터 분석!")

    st.subheader("차트 보기")
    df = pd.read_csv("./data/fuel_econ.csv")

    if st.checkbox("데이터 프레임 보기") :
        st.data_editor(df)

    st.text("컬럼을 선택하면, 중복제거한 데이터의 개수를 보여줍니다.")
    choice = st.selectbox("컬럼 선택", df.columns) 
    count = df[choice].nunique()
    st.write(f"{choice} 컬럼의 중복제거한 데이터의 개수는 {count}개 입니다.")

    if st.checkbox("자동차 회사별로 몇개의 자동차가 있는지 보기") :
        a = df["make"].value_counts()
        st.dataframe(a)
    
    selected_list = st.multiselect("두개의 컬럼을 선택하세요" , df.columns[8:],max_selections=2 ,placeholder="두개의 컬럼 선택")    

    if len(selected_list) == 2 :
        fig1 = plt.figure()
        plt.scatter(data=df, x=selected_list[0], y=selected_list[1])
        plt.title(f"{selected_list[0]} Vs {selected_list[1]} ")
        plt.xlabel(f"{selected_list[0]}")
        plt.ylabel(f"{selected_list[1]}")
        st.pyplot(fig1)

        st.write("상관계수")
        st.dataframe(df[selected_list].corr())
    elif len(selected_list) == 1 : 
        st.write("두 개의 컬럼을 선택해주세요.")
    else : st.write("")

if __name__ == "__main__" : main()