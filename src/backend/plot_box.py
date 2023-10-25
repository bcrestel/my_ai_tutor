from PIL import ImageFile, ImageDraw
import pandas as pd


def plot_box(img: ImageFile.ImageFile, df_pytesseract: pd.DataFrame):
    img_box = ImageDraw.Draw(img)
    all_dim = df_pytesseract[["left", "top", "width", "height"]].values
    for dim in all_dim:
        add_rectangle(img_box, *dim)
    img.show()


def add_rectangle(img: ImageDraw.ImageDraw, left, top, width, height, fill=None, outline="red"):
    img.rectangle([(left, top), (width + left, height + top)], fill=fill, outline=outline)