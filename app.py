# _*_ coding:utf-8 _*_
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

# @st.cache_data    
# def load_data(loaddata):
#     a = loaddata
#     df=pd.read_csv('data/a.csv')
#     return df

def main():
    df1=pd.read_csv('data/products(10000).csv')
    df2=pd.read_csv("data/departments.csv")
    st.title("물건의 위치는 밑에 표시됩니다.")
    with st.sidebar :
        st.header('물건의 위치 찾기')
        dpid=st.selectbox("select department_id", df2['department_id'])
        dpname = df2.loc[df2['department_id']==dpid,['department']]
        st.write('선택한 departments :', dpid)
        st.header("찾는 물건의 이름")
        find_product = st.selectbox("찾을 물건의 이름",df1.loc[df1['department_id']==dpid, 'product_name'])
        pdid = df1.loc[df1['product_name']==find_product, 'product_id'] # ==> 33번째 줄이 주석에 설명 되어있음!! 이렇게 판다스로 가공하는 코드는 결국에 쓸모가 없었다. 데이터프레임(series)값이기에 매개변수로 어디든 못들어감!!!
        st.write("선택한 물건의 id는 :", find_product)
        
    with st.sidebar:
        st.header("찾는 물건의 id")
        find_id = st.selectbox("찾을 물건의 id",df1.loc[df1['department_id']==dpid, 'product_id'])
        pdname =  df1.loc[df1['product_id']==find_id, 'product_name'] # ==> 판다스 데이터프레임으로 가져오는 것! 그렇기에 df1['product_name']==pdname에서 pdname이 str, int값이 아닌 데이터프레임(series)값이기에 오류가 떳다.
        st.write("선택한 물건의 이름은 :", pdname)


    st.write('물건 이름에 따른 복도 위치')
    B=df1.loc[(df1['department_id']==dpid)&(df1['product_name']==find_product), :]
    # B=df1.loc[(df1['department_id']==dpid)&(df1['product_name']==pdname), :] ==> 위에 코드랑 다른이유 : pdname이 데이터프레임(series)값이기에 매개변수 자리에는 int, str값이 들어가야한다.   
    st.dataframe(B)
    
    st.write('id에 따른 물건의 복도 위치')
    A=df1.loc[(df1['department_id']==dpid)&(df1['product_id']==find_id) , :]
    st.dataframe(A)
 
    
if __name__ == "__main__":
    main()