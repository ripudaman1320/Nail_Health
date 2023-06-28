import streamlit as st
import os
import base64


col1, col2, col3 = st.columns(3)
# img_value_size = 200
with col1:
   # col4, col5, col6 = st.columns(3)
   st.title("Ripudaman Singh")
   st.subheader("14333280")
   st.image('./images/team/Ripudaman.jpg')
   # st.image('./images/team/linkedin.png')
   col1.markdown(" ###### LinkedIn : [LinkedIn](https://www.linkedin.com/in/ripudaman-singh-ab8342165/)")
   col1.markdown(" ###### GitHub : [Github](https://github.com/ripudaman1320)")


with col2:
   st.title("Rupali Palikhe")
   st.subheader("13888666")
   st.image('./images/team/Rupali.jpg')
   col2.markdown(" ###### LinkedIn : [LinkedIn](https://www.linkedin.com/in/rupali-palikhe/)")
#    st.image()

with col3:
   st.title("Sarah Agustin")
   st.subheader("13540570")
   st.image('./images/team/Sarah.jpg')
   col3.markdown(" ###### LinkedIn : [LinkedIn](https://www.linkedin.com/in/sarah-mae-agustin-17b837180/)")
#    st.image()