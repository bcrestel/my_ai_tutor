from PIL import ImageFile, ImageDraw
import pandas as pd


def plot_box(img: ImageFile.ImageFile, df_pytesseract: pd.DataFrame, fill=None, outline="red"):
    """Plot boxes as defined by pytesseract on img

    Args:
        img (ImageFile.ImageFile): input image
        df_pytesseract (pd.DataFrame): pandas.DataFrame produced by pytesseract.image_to_data
        fill (_type_, optional): _description_. Defaults to None.
        outline (str, optional): _description_. Defaults to "red".
    """
    img_box = ImageDraw.Draw(img)
    all_dim = df_pytesseract[["left", "top", "width", "height"]].values
    for dim in all_dim:
        add_rectangle(img_box, *dim, fill=fill, outline=outline)
    img.show()


def add_rectangle(img: ImageDraw.ImageDraw, left, top, width, height, fill=None, outline="red"):
    img.rectangle([(left, top), (width + left, height + top)], fill=fill, outline=outline)