import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from the specified path and return it as a NumPy array."""
    try:
        if not path.endswith(('.jpg', '.jpeg')):
            raise ValueError("Unsupported file format.")
        with Image.open(path) as img:
            print(f"The shape of image is: {img.size[1]},{img.size[0]}, \
                  {img.layers}")
            img_array = np.array(img)
            return img_array
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {path} was not found.")
