import numpy as np
from PIL import Image

from siamese import Siamese

if __name__ == "__main__":
    # 默认的path是model_data/word_compare.pth
    # model = Siamese(model_path="model_data/word_compare.pth")
    model = Siamese(model_path="logs/best_epoch_weights.pth")

    # image_1 = Image.open(R"F:\Project\DeepLearning\Game\material\dataset\temp\12.JPG")
    image_1 = Image.open(R"F:\Project\DeepLearning\Siamese\material\mixImg\本-146-5.png")
    # image_2 = Image.open(R"F:\Project\DeepLearning\Game\material\dataset\temp\10.JPG")
    image_2 = Image.open(R"F:\Project\DeepLearning\Siamese\material\mixImg\本-59-0.png")

    probability = model.detect_image(image_1, image_2)
    print(probability)
