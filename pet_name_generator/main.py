import langchain_helper as lch
import streamlit as st

st.title('Pets name generator')

animal_type = st.sidebar.selectbox("What is your pet?", ("cat", "dog", "bird", "fish"))
if animal_type == 'cat':
    pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)
if animal_type == 'dog':
    pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)
if animal_type == 'bird':
    pet_color = st.sidebar.text_area(label="What color is your bird?", max_chars=15)

if pet_color:
    response = lch.generate_pet_nam(animal_type, pet_color)
    st.text(response['pet_name'])