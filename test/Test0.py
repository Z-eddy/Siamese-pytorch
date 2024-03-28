import os
import random

import numpy as np

dataset_path = R"F:\Project\DeepLearning\Siamese\material"
# train_path = os.path.join(dataset_path, 'images_background')
train_path = dataset_path
print(train_path)

types = 0
images = []
labels = []

for character in os.listdir(train_path):
    # -------------------------------------------------------------#
    #   对每张图片进行遍历
    # -------------------------------------------------------------#
    character_path = os.path.join(train_path, character)
    for image in os.listdir(character_path):
        images.append(os.path.join(character_path, image))
        labels.append(types)
    types += 1

random.seed(1)
shuffle_index = np.arange(len(images), dtype=np.int32)
random.shuffle(shuffle_index)
random.seed(None)
images = np.array(images)
labels = np.array(labels)
images = images[shuffle_index]
labels = labels[shuffle_index]

num_train = int(len(images) * 0.9)
val_lines = images[num_train:]
val_labels = labels[num_train:]
train_lines = images[:num_train]
train_labels = labels[:num_train]

# train_lines, train_labels, val_lines, val_labels
# print(train_lines,len(train_lines))
print(train_labels, len(train_labels))
