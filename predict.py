import numpy as np
from PIL import Image

from siamese import Siamese

if __name__ == "__main__":
    model = Siamese()

    image_1 = Image.open(R"F:\Project\DeepLearning\Game\material\dataset\temp\10.JPG")
    image_2 = Image.open(R"F:\Project\DeepLearning\Game\material\dataset\temp\12.JPG")

    probability = model.detect_image(image_1, image_2)
    print(probability)
