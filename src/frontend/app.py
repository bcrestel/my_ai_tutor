from enum import Enum
import logging

import streamlit as st
from PIL import Image

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(filename)s--l.%(lineno)d: %(message)s",
)
logger = logging.getLogger(__name__)

class InputMode(Enum):
    take = "Prendre une photo"
    load = "Verser une photo"

st.sidebar.header("Méthode d'ajout de la photo")
input_mode = st.sidebar.selectbox(
    "Choisis comment tu veux ajouter une photo de ton texte:",
    [InputMode.take.value, InputMode.load.value]
)

if input_mode == InputMode.take.value:
    picture = st.camera_input("Prends une photo de ton texte")
elif input_mode == InputMode.load.value:
    picture = st.file_uploader("Ajoute une photo de ton texte")

original_picture = st.empty()
cropped_picture = st.empty()

if picture is not None:
    original_picture.image(picture, caption="Photo de ton texte originale", use_column_width=True)

    # Define cropping parameters
    st.sidebar.header("Crop Parameters")
    left = st.sidebar.number_input("Left", value=0, min_value=0)
    top = st.sidebar.number_input("Top", value=0, min_value=0)
    right = st.sidebar.number_input("Right", value=0, min_value=0)
    bottom = st.sidebar.number_input("Bottom", value=0, min_value=0)

    if st.sidebar.button("Crop"):
        # Open and crop the image using PIL
        image = Image.open(picture)
        width, height = image.size
        logger.debug(f"left={left}, top={top}, right={right}, bottom={bottom}")
        cropped_image = image.crop((left, top, right, bottom))
        # Display the cropped image
        cropped_picture.image(cropped_image, caption="Photo de ton texte croquée", use_column_width=True)
    
if st.sidebar.button("Recommencer"):
    original_picture.empty()
    cropped_picture.empty()
    picture = None