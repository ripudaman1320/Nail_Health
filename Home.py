import streamlit as st

st.set_page_config(page_title = 'Nail Health', 
                    layout='wide',
                    page_icon='./images/nail.png')
# st.subheader('_Yolo for nail health_')
st.write("# Welcome to Nail Health! 👋")
st.balloons()
# About
st.markdown("""
            ##### This project aims to provide classification results on the different types of nail diseases. Overall, we have compiled a list of 10 nail diseases as per the WHO approved clinical diseases for nails. They are as follows;  
            """)

st.markdown(
    """
    <style>
    .stTabs > div {
        overflow: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
img_value_size = 200
st.subheader("_Nail Diseases_")

with st.container():
    disease1, disease2, disease3, disease4, disease5 = st.tabs(['Acral Lentiginous Melanoma', 'Beaus Line', 'Blue Finger', 'Clubbing', 'Healthy Nail'])

    with disease1:
        st.image('./images/Acral Lentiginous Melanoma.jpg', width=img_value_size)

    with disease2:
        st.image('./images/Beaus Line.jpg', width=img_value_size)

    with disease3:
        st.image('./images/Blue Finger.jpg', width=img_value_size)

    with disease4:
        st.image('./images/Clubbing.jpg', width=img_value_size)

    with disease5:
        st.image('./images/Healthy Nail.jpg', width=img_value_size)

with st.container():
    disease6, disease7, disease8, disease9, disease10, disease11 = st.tabs(['Koilonychia', 'Lindsay-s Nail', 'Muehrckes Lines', 'Onychogryphosis', 'Pitting', 'Terry-s Nail'])

    with disease6:
        st.image('./images/Koilonychia.jpg', width=img_value_size)

    with disease7:
        st.image('./images/Lindsay-s Nail.jpg', width=img_value_size)

    with disease8:
        st.image('./images/Muehrckes Lines.jpg', width=img_value_size)

    with disease9:
        st.image('./images/Onychogryphosis.jpg', width=img_value_size)

    with disease10:
        st.image('./images/pitting.jpg', width=img_value_size)

    with disease11:
        st.image('./images/Terry-s Nail.jpg', width=img_value_size)