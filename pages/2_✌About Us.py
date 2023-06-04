import streamlit as st
import os
import base64

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# @st.cache(allow_output_mutation=True)
# def get_img_with_href(local_img_path, target_url):
#     img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
#     bin_str = get_base64_of_bin_file(local_img_path)
#     html_code = f'''
#         <a href="{target_url}">
#             <img src="data:image/{img_format};base64,{bin_str}" />
#         </a>'''
#     return html_code
# gif_html = get_img_with_href('./images/team/linkedin.png', 'https://docs.streamlit.io')

col1, col2, col3 = st.columns(3)
# img_value_size = 200
with col1:
   st.subheader("Ripudaman Singh - 14333280")
   st.image('./images/team/Ripudaman.jpg')
   col1.markdown("[[LinkedIn]](https://www.linkedin.com/in/ripudaman-singh-ab8342165/)")
   col1.markdown("[[Github]](https://github.com/ripudaman1320)")
#    st.markdown(gif_html, unsafe_allow_html=True)
#    st.markdown('''
#     <a href="https://www.linkedin.com/in/ripudaman-singh-ab8342165/">
#         <img src="./images/team/linkedin.png"/>
#     </a>''',
#     unsafe_allow_html=True
#     )
    


with col2:
   st.subheader("Rupali Palikhe")
#    st.image()

with col3:
   st.subheader("Sarah Agustin")
#    st.image()