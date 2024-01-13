from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    The main function of the program.
    Load an image from a file and then
    slice it, grayscale it and display it
    using X and Y axis.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)

        print(img)

        zoomed_image = img[200:600, 400:800]
        zoomed_image = Image.fromarray(zoomed_image).convert("L")
        print(f"New shape after slicing: {zoomed_image.size}")
        print(np.array(zoomed_image))
        plt.imshow(zoomed_image, cmap='gray')
        plt.axis('on')
        plt.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
