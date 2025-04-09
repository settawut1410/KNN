from sklearn.neighbors import KNeighborsClassifier
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('การจำแนกข้อมูลด้วยเทคนิค ML')
st.image("./img/moew.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("spiderman")
   st.image("./img/s1.jpg")

with col2:
   st.header("spiderman")
   st.image("./img/s2.jpg")

with col3:
   st.header("spiderman")
   st.image("./img/s3.jpg")

html_7 = """
<div style="background-color:#808080;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูล iris หรือข้อมูลดอกไม้สำหรับทำนาย</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")