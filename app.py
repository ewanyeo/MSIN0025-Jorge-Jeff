import streamlit as st

# Set page title
st.set_page_config(page_title='Jorge & Jeff', page_icon='Jorge & Jeff-1.jpg')

st.markdown(
    """
    <div style='background-color: #f2f2f2; padding: 30px;'>
        <img src='Jorge & Jeff-1.jpg' style='max-width: 300px;'>
        <h1 style='font-size: 48px; margin-top: 20px;'>Welcome to Jorge & Jeff</h1>
        <p style='font-size: 24px;'>Your one-stop shop for all your fashion needs.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# Add more content below the hero section
st.title('Jorge & Jeff')
st.write('Welcome to Paradise')

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("Ethan likes it")

st.sidebar.title("Menu")

st.image("Jorge & Jeff-1.jpg")
