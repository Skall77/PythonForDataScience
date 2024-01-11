from PIL import Image
import numpy as np


def ft_load(path: str):
    """
Load an image from a file.
Print its format and return
its pixel content in RGB format.

Param:
    path (str): Path to the file.

Return:
    array: Pixel content in RGB format.
    """
    try:
        image = Image.open(path)
        print(f"Image format: {image.format}")
        img = np.array(image)
        print(f"The shape of image is: {img.shape}")
        return img
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
The main function of the program.
Test ft_load function.
    """
    print(ft_load("landscape.jpg"))
    print(ft_load("crab.png"))
    print(ft_load("notAnImage.txt"))
    print(ft_load("doesNotExist.jpg"))
