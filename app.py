import streamlit as st

st.title("My First Streamlit Project")
st.write("this is the place where you can write anything you want")
#for slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {slider_value}")
# for checkbox
st.write('interactive checkbox')
checkbox_value = st.checkbox("Check me!")
if checkbox_value:
    st.write("Checkbox is checked!")
else:
    st.write("Checkbox is not checked!")
#for text
st.title("Text Input Example")
text_value = st.text_input("Enter some text", "Type here...")
st.write(f"You entered: {text_value}")