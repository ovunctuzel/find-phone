import os
import argparse
import shutil

import torch
from ultralytics import YOLO
from convert_dataset import convert_dataset
from split_dataset import split_dataset


def train_model(model_name='yolov8s_phone.pt', epochs=5):
    torch.backends.cudnn.enabled = False
    model = YOLO('yolov8s.pt')
    model.train(data='yolov8/phone.yaml', epochs=epochs, name=model_name, project='yolov8/runs', save_dir='model')
    shutil.copy(f'yolov8/runs/{model_name}/weights/best.pt', 'yolov8/yolov8s_phone.pt')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Phone Finder")
    parser.add_argument("data_path", type=str, help="Path to the dataset with a set of images and a labels.txt file")
    args = parser.parse_args()

    # Convert dataset to YOLO format
    print("Converting dataset to YOLO format...")
    images_folder = args.data_path
    label_filepath = os.path.join(args.data_path, 'labels.txt')
    convert_dataset(output_folder='./yolov8', images_folder=images_folder, labels_file=label_filepath)

    # Split dataset into train, validation and test sets. Since we have a small dataset, we keep the test set small.
    print("Splitting dataset into train, validation and test sets...")
    split_dataset(dataset_dir='./yolov8', train_ratio=0.85, validation_ratio=0.1, test_ratio=0.05)

    # Train a YOLOv8s model with the provided data
    print("Starting YOLOv8 model training...")
    train_model(epochs=25)

