from enum import Enum
import logging

import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

from src.frontend.utils import InputMode

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(filename)s--l.%(lineno)d: %(message)s",
)
logger = logging.getLogger(__name__)

if "crop" not in st.session_state:
    st.session_state.crop = False
    st.session_state.cropped_image = None

st.sidebar.header("Méthode d'ajout de la photo")
input_mode = st.sidebar.selectbox(
    "Choisis comment tu veux ajouter une photo de ton texte:",
    [InputMode.load.value]
    #[InputMode.take.value, InputMode.load.value]
)

if input_mode == InputMode.take.value:
    picture = st.camera_input("Prends une photo de ton texte")
elif input_mode == InputMode.load.value:
    picture = st.file_uploader("Ajoute une photo de ton texte")

original_picture = st.empty()
cropped_picture = st.empty()

if picture is not None:
    if st.sidebar.button("Crop"):
        st.session_state.crop = True

    if st.session_state.crop:
        cropped_picture.image(st.session_state.cropped_image, caption="Photo de ton texte croquée", use_column_width=True)
    else:
        #original_picture.image(picture, caption="Photo de ton texte originale", use_column_width=True)
        image = Image.open(picture)
        st.session_state.cropped_image = st_cropper(image)

#    # Define cropping parameters
#    st.sidebar.header("Crop Parameters")
#    left = st.sidebar.number_input("Left", value=0, min_value=0)
#    top = st.sidebar.number_input("Top", value=0, min_value=0)
#    right = st.sidebar.number_input("Right", value=0, min_value=0)
#    bottom = st.sidebar.number_input("Bottom", value=0, min_value=0)
#
#    if st.sidebar.button("Crop"):
#        # Open and crop the image using PIL
#        image = Image.open(picture)
#        width, height = image.size
#        logger.debug(f"left={left}, top={top}, right={right}, bottom={bottom}")
#        cropped_image = image.crop((left, top, right, bottom))
#        # Display the cropped image
#        cropped_picture.image(cropped_image, caption="Photo de ton texte croquée", use_column_width=True)
    
if st.sidebar.button("Recommencer"):
    original_picture.empty()
    cropped_picture.empty()
    picture = None
    st.session_state.crop = False
    st.session_state.cropped_image = None