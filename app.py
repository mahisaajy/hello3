import streamlit as st
import time




st.write("Hello World")
st.write("BMKG 123")
# st.snow()

st.title("Judul ABC")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.header('This is a header with a divider', divider='rainbow')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.divider()  # 👈 Draws a horizontal rule

################

st.image('bmkg.png', caption='Clear Clean and Qualified')

st.audio("cat-purr.mp3", format="audio/mpeg")

video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


##################



# Spinner
# with st.spinner('Wait for it...'):
#     time.sleep(5)
st.success('Done!')
# Toast
st.toast('Your edited image was saved!', icon='😍')
# Balloons
# st.balloons()
# Snow
# st.snow()

###################

#Button
st.button("Reset", type="primary")
if st.button('Say hello'):
   st.write('Why hello there')
else:
   st.write('Goodbye')
#Link Button
st.link_button("Go to gallery", "https://streamlit.io/gallery")


####################

col1, col2, col3 = st.columns(3)

with col1:
  st.header("A cat")
  st.image("https://cdn.bmkg.go.id/Web/WhatsApp-Image-2024-04-30-at-09.40.16.jpeg")
  # Using object notation
  add_selectbox1 = st.selectbox(
        "How would you like to be contacted ?",
        ("Email", "Home phone", "Mobile phone")
  )

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")


############

st.sidebar.title('Judul')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

###############

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


st.set_page_config(
    page_title="Home",
    page_icon="🧊",
    # layout="wide",
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)