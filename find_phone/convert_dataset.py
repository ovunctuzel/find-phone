import csv
import os
import shutil


def create_yolo_dataset(labels, images_folder, output_folder):
    """
    Creates a yolo-format dataset from a dictionary representation of bounding boxes
    :param labels: A dictionary where keys are image filenames, and the values are lists in the format:
                   [xmin, ymin, xmax, ymax, label]
    :param images_folder: The folder where the original images are located
    :param output_folder: The output folder for the transformed dataset
    :return: None
    """
    # We hardcode the class index to 0 and the bbox width and height to 0.1 here since we only deal with phones of
    # approximately the same size. The provided dataset only has the center point but yolo requires a bounding box.
    class_idx = 0
    w = 0.1
    h = 0.1

    for filename in labels:
        x, y = labels[filename]
        image_path = os.path.join(images_folder, filename)
        try:
            shutil.copy(image_path, os.path.join(output_folder, 'images', filename))
            with open(os.path.join(output_folder, 'labels', f'{os.path.splitext(filename)[0]}.txt'), 'w') as f:
                f.write(f"{class_idx} {x} {y} {w} {h}")
        except FileNotFoundError:
            print(f"File {filename} not found in {images_folder}.")


def convert_dataset(output_folder='../dataset', images_folder='../dataset', labels_file = '../dataset/labels.txt'):
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels'), exist_ok=True)

    labels = {}
    with open(labels_file, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for image_filename, x, y in reader:
            labels[image_filename] = x, y

    create_yolo_dataset(labels, images_folder, output_folder)


if __name__ == '__main__':
    convert_dataset()

