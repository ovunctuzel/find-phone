import os
import argparse
import cv2
from ultralytics import YOLO


class PhoneFinder:
    def __init__(self, model_path='../yolov8n.pt'):
        self.model_path = model_path

    def find_phone(self, image_path):
        model = YOLO(self.model_path)
        image = cv2.imread(image_path)
        boxes = model.predict(image_path, verbose=False)[0].boxes
        # Convert to [xmin, ymin, xmax, ymax, label] format
        boxes = [[*boxes.xyxy.tolist()[i], boxes.cls.tolist()[i]] for i in range(len(boxes))]
        if len(boxes) > 0:
            box = boxes[0]  # We assume there is only a single object in the image
            x, y = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
            norm_x, norm_y = x / image.shape[1], y / image.shape[0]
            return norm_x, norm_y
        return None

    def visualize(self, x, y, image_path):
        image = cv2.imread(image_path)
        image_h, image_w, ch = image.shape
        cv2.drawMarker(image, (int(x * image_w), int(y * image_h)), color=(0, 0, 0), thickness=10)
        cv2.drawMarker(image, (int(x * image_w), int(y * image_h)), color=(0, 255, 0), thickness=2)
        cv2.imshow('', image)
        cv2.waitKey()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Phone Finder")
    parser.add_argument("image_path", type=str, help="Path to the input image, or to a folder containing images")
    parser.add_argument("--visualize", action="store_true", help="Visualize the detected phone")
    args = parser.parse_args()

    images_folder = '../dataset_test/images'
    phone_finder = PhoneFinder('yolov8/yolov8s_phone.pt')

    if os.path.isfile(args.image_path):
        image_paths = [args.image_path]
    else:
        image_paths = [os.path.join(args.image_path, filename) for filename in os.listdir(args.image_path)
                       if os.path.splitext(filename)[-1] in ['.jpeg', '.jpg', '.png']]

    for image_path in image_paths:
        output = phone_finder.find_phone(image_path)
        if output is None:
            print("ERROR: No phone detected in image")
        else:
            x, y = output
            if args.visualize:
                phone_finder.visualize(x, y, image_path)
            print(x, y)
