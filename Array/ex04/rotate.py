from PIL import Image
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
The main function of the program.
Load an image, zoom on it, grey it and transposes it.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise FileNotFoundError("File not found.")
        print(img)
        zoomed_image = img[200:600, 400:800]
        zoomed_image = np.array(list(zip(*zoomed_image)))
        zoomed_image = Image.fromarray(zoomed_image).convert("L")
        print("New shape after slicing:", zoomed_image.size)
        print(np.array(zoomed_image))
        plt.imshow(zoomed_image, cmap='gray')
        plt.axis('on')
        plt.show()
    except FileNotFoundError as e:
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    main()
