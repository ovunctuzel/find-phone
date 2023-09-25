""" Takes a yolo-format dataset and splits into train/validation/test sets. """

import os
import random
import shutil


def split_dataset(dataset_dir, train_ratio, validation_ratio, test_ratio):
    assert(train_ratio + validation_ratio + test_ratio == 1)
    # Create destination directories
    train_dir = os.path.join("../dataset_train")
    validation_dir = os.path.join("../dataset_validation")
    test_dir = os.path.join("../dataset_test")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Determine the corresponding subdirectory in the destination folders
    train_images = os.path.join(train_dir, 'images')
    train_labels = os.path.join(train_dir, 'labels')
    val_images = os.path.join(validation_dir, 'images')
    val_labels = os.path.join(validation_dir, 'labels')
    test_images = os.path.join(test_dir, 'images')
    test_labels = os.path.join(test_dir, 'labels')

    # Create the subdirectories in the destination folders
    os.makedirs(train_images, exist_ok=True)
    os.makedirs(train_labels, exist_ok=True)
    os.makedirs(val_images, exist_ok=True)
    os.makedirs(val_labels, exist_ok=True)
    os.makedirs(test_images, exist_ok=True)
    os.makedirs(test_labels, exist_ok=True)

    # Split the files in the current directory
    files = os.listdir(os.path.join(dataset_dir, 'images'))
    random.shuffle(files)
    num_files = len(files)
    num_train = int(train_ratio * num_files)
    num_test = int(test_ratio * num_files)
    num_validation = num_files - num_train - num_test

    train_files = files[:num_train]
    test_files = files[num_train:num_train + num_test]
    validation_files = files[num_train + num_test:]

    # Move files to the corresponding destination subdirectories
    for file in train_files:
        shutil.copy2(os.path.join(dataset_dir, 'images', file), os.path.join(train_images, file))
        label_file = f'{os.path.splitext(file)[0]}.txt'
        shutil.copy2(os.path.join(dataset_dir, 'labels', label_file), os.path.join(train_labels, label_file))

    for file in validation_files:
        shutil.copy2(os.path.join(dataset_dir, 'images', file), os.path.join(val_images, file))
        label_file = f'{os.path.splitext(file)[0]}.txt'
        shutil.copy2(os.path.join(dataset_dir, 'labels', label_file), os.path.join(val_labels, label_file))

    for file in test_files:
        shutil.copy2(os.path.join(dataset_dir, 'images', file), os.path.join(test_images, file))
        label_file = f'{os.path.splitext(file)[0]}.txt'
        shutil.copy2(os.path.join(dataset_dir, 'labels', label_file), os.path.join(test_labels, label_file))

    print("Dataset split completed.")


if __name__ == '__main__':
    # Specify the dataset directory and the split ratios
    dataset_directory = "../dataset"
    train_ratio = 0.85
    validation_ratio = 0.1
    test_ratio = 0.05

    # Split the dataset
    split_dataset(dataset_directory, train_ratio, validation_ratio, test_ratio)
