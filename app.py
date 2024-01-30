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
        st.write('선택한 departments :', dpname)
        st.header("찾는 물건의 이름")
        find_product = st.selectbox("찾을 물건의 이름",df1.loc[df1['department_id']==dpid, 'product_name'])
        pdid = df1.loc[df1['product_name']==find_product, 'product_id']
        st.write("선택한 물건의 id는 :", pdid)
        #st.write(type(find_product))
        #st.write(type(pdid))
        
        
    with st.sidebar:
        st.header("찾는 물건의 id")
        find_id = st.selectbox("찾을 물건의 id",df1.loc[df1['department_id']==dpid, 'product_id'])
        pdname =  df1.loc[df1['product_id']==find_id, 'product_name']
        st.write("선택한 물건의 이름은 :", pdname)
    # filter_pdid=df1.loc[df1['product_id']=='pdid', 'aisle_id']
    # filter_find_product=df1.loc[df1['product_name']=='find_product', 'aisle_id']
    # st.dataframe(filter_pdid)
    # st.dataframe(filter_find_product)
    st.write('물건 이름에 따른 복도 위치')
    B=df1.loc[(df1['department_id']==dpid)&(df1['product_name']==find_product), :]
    # B=df1.loc[(df1['department_id']==dpid)&(df1['product_name']==pdname), :]
    st.dataframe(B)
    
    st.write('id에 따른 물건의 복도 위치')
    A=df1.loc[(df1['department_id']==dpid)&(df1['product_id']==find_id) , :]
    st.dataframe(A)
 
    
if __name__ == "__main__":
    main()