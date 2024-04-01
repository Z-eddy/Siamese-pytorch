import os
import random

import numpy as np

# dataset_path = R"F:\Project\DeepLearning\Siamese\material"
dataset_path = R"F:\Project\DeepLearning\Siamese\testMaterial"
# train_path = os.path.join(dataset_path, 'images_background')
train_path = dataset_path
print(train_path)

types = 0
images = []
labels = []
wordsIdx = {}

for character in os.listdir(train_path):
    # -------------------------------------------------------------#
    #   对每张图片进行遍历
    # -------------------------------------------------------------#
    character_path = os.path.join(train_path, character)
    for image in os.listdir(character_path):
        # 安装规则分离,只要首字
        tempKey = image.split("-")[0]
        # 如果当前字未记录则记录
        if tempKey not in wordsIdx:
            wordsIdx[tempKey] = types
            types += 1
        # 记录当前的文件和类型
        images.append(os.path.join(character_path, image))
        labels.append(wordsIdx[tempKey])

# images.append(os.path.join(character_path, image))
# labels.append(types)
# types += 1

"""
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
# print(train_lines, len(train_labels))

c = random.randint(0,  1)
print(c)
print(train_labels)
idxs = train_labels[:] == c
print(idxs)
selected_path = train_lines[idxs]
print(selected_path)
image_indexes = random.sample(range(0, len(selected_path)), 3)
print(image_indexes)

batch_images_path = []
batch_images_path.append(selected_path[image_indexes[0]])
batch_images_path.append(selected_path[image_indexes[1]])
batch_images_path.append(selected_path[image_indexes[2]])
print(batch_images_path)
"""
