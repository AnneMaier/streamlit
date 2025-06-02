import streamlit as st
from PIL import Image

# ----------------- side br -----------------

st.sidebar.title('Sidebar')
st.sidebar.header('텍스트 입력 사용 예')
user_id = st.sidebar.text_input('아이디(ID) 입력', value='root', max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value='1234', type='password')

st.sidebar.header('셀렉트 박스 사용 예')
selectobx_option = ['절규', '월하정인', '진주 귀걸이를 한 소녀', '별이 빛나는 밤']
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectobx_option, index=3)
st.sidebar.write('**당신의 선택** :', your_option)


# ----------------- Main View  0---------------------------------------------------

folder = './data/'

image_files = [
    'https://github.com/AnneMaier/streamlit/blob/main/sidebar/data/2.png?raw=true', 
    'https://github.com/AnneMaier/streamlit/blob/main/sidebar/data/3.png?raw=true',
    'https://github.com/AnneMaier/streamlit/blob/main/sidebar/data/4.png?raw=true',
    'https://github.com/AnneMaier/streamlit/blob/main/sidebar/data/1.png?raw=true']

selectbox_options_index = selectobx_option.index(your_option)
image_file = image_files[selectbox_options_index]

st.image(image_file, width=350, caption=your_option)
