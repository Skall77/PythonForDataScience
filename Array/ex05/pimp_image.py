import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(array) -> np.ndarray:
    """
Inverts the color of the image received.

Param:
array (np.ndarray): Pixel content in RGB format.

Return:
np.ndarray: Pixel content in RGB format.
    """
    image = 255 - array
    Image.fromarray(image).show()
    print(image)
    return image


def ft_red(array) -> np.ndarray:
    """
Converts the image received to red.

Param:
array (np.ndarray): Pixel content in RGB format.

Return:
np.ndarray: Pixel content in RGB format.
    """
    image = array.copy()
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    Image.fromarray(image).show()
    print(image)
    return image


def ft_green(array) -> np.ndarray:
    """
Converts the image received to green.

Param:
array (np.ndarray): Pixel content in RGB format.

Return:
np.ndarray: Pixel content in RGB format.
    """
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    Image.fromarray(image).show()
    print(image)
    return image


def ft_blue(array) -> np.ndarray:
    """
Converts the image received to blue.

Param:
array (np.ndarray): Pixel content in RGB format.

Return:
np.ndarray: Pixel content in RGB format.
    """
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    Image.fromarray(image).show()
    print(image)
    return image


def ft_grey(array) -> np.ndarray:
    """
Converts the image received to grey.

Param:
array (np.ndarray): Pixel content in RGB format.

Return:
np.ndarray: Pixel content in RGB format.
    """
    image = np.dot(array[..., :3], [0.299, 0.587, 0.114])
    image = image.astype(np.uint8)
    image = np.stack((image, image, image), axis=-1)
    print(image)
    Image.fromarray(image).show()
    return image


def main():
    """
The main function of the program.
    """
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)


if __name__ == "__main__":
    main()
