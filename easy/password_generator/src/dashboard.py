import streamlit as st
from src.password_generator import MemorablePasswordGenerator, PinGenerator, RandomPasswordGenerator

st.image("https://www.keepersecurity.com/blog/wp-content/uploads/2022/11/blog-7.jpg")
st.title(":zap: Password Generator")


option  =st.radio("select a password generator",
("Random Password", "Memorable Password", "Pin Code"))

if option == "Pin Code":
    length = st.slider("Select the length of the pin code: ", 4, 32)
    generator = PinGenerator(length)

elif option == "Memorable Password":
    number_of_words = st.slider("Select the number of words: ",3, 10 )
    seperator = '-'
    capitalization = True
    generator = MemorablePasswordGenerator(number_of_words, seperator, capitalization )

elif option == "Random Password":
    length = st.slider("Select the length of the password", 8, 16)
    include_nums = st.checkbox("include numbers")
    include_syms = st.checkbox("include symbols")
    generator = RandomPasswordGenerator(length, include_nums, include_syms)

password = generator.generate()
st.write(f"your password is {password}")