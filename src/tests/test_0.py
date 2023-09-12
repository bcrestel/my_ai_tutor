import streamlit as st

st.title("Upload and Remove Image")

# Create a placeholder for the uploaded image
uploaded_image = st.empty()

# Upload a new image using Streamlit's file uploader widget
new_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Button to display the uploaded image and remove it
if new_image is not None:
    if st.button("Display Image"):
        uploaded_image.image(new_image, caption="Uploaded Image", use_column_width=True)
    if st.button("Remove Image"):
        uploaded_image.empty()  # Remove the displayed image
