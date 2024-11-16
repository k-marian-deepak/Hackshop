import streamlit as st
from PIL import Image

# Sidebar section for basic navigation
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Projects", "Contact"])

# Main Portfolio Content
st.title("My Portfolio")

# About Me Section
if page == "About Me":
    st.header("👋 About Me")
    st.write("""
    Hello! I'm K M Deepak, a passionate developer with a focus on Python, data science, and creating interactive applications.
    I love tackling challenging problems and bringing creative solutions to life!
    """)
    st.write("""
    - 📚 Currently studying B.E. CSE
    - 🧑‍💻 Experienced in: Python, Data Analysis, Machine Learning
    - 🌱 Learning: Streamlit, Web Development
    """)
    
    # Display a profile image
    #profile_img = Image.open("your_profile_picture.jpg")  # Add your own image here
    #st.image(profile_img, width=200)

# Projects Section
elif page == "Projects":
    st.header("🛠 Projects")
    st.write("Here are some of my projects:")

    # Sample Project 1
    st.subheader("1. Guessing Game")
    st.write("""
    - A fun interactive game where the computer or user guesses a number.
    - Implements binary search for optimal guesses.
    - Built with Python and Streamlit.
    """)

    # Sample Project 2
    st.subheader("2. Data Analysis Project")
    st.write("""
    - Conducted an in-depth analysis on Automation.
    - Used Python libraries like Pandas and Matplotlib for data cleaning and visualization.
    - Gained valuable insights into Building own projects through inovation.
    """)

# Contact Section
elif page == "Contact":
    st.header("📬 Contact Me")
    st.write("Feel free to reach out to me through any of the following channels:")

    # Display contact information
    st.write("- Email: kmadeepakdeepak299@gmail.com")
    st.write("- LinkedIn: https://www.linkedin.com/in/k-m-deepak-72193a314")
    st.write("- GitHub: https://github.com/k-marian-deepak")

    # Contact form (optional)
    st.write("Or leave me a message here:")
    user_message = st.text_area("Message", placeholder="Type your message here...")
    if st.button("Send"):
        if user_message:
            st.success("Thank you! Your message has been sent.")
        else:
            st.warning("Please write a message before sending.")
