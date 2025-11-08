from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def main():
    print(ft_load("animal.jpeg"))

    image = Image.open("animal.jpeg")
    image.show()

    zoomed_image = image.crop((400, 200, 800, 600))
    zoomed_image.save("zoomed_image.jpg")

    grayscale_image = zoomed_image.convert("L")
    grayscale_image.show()
    print(f"New shape after slicing: {ft_load('zoomed_image.jpg').shape}")

    plt.imshow(zoomed_image)
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()

if __name__ == "__main__":
    main()
