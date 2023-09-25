""" Simple script to check annotations in a yolo-format dataset. Annotations will be visualized in an opencv window. """
import os
import cv2


root_folder = '../dataset'
for image_filename in os.listdir(f'{root_folder}/images'):
    label_filename = f'{os.path.splitext(image_filename)[0]}.txt'
    img = cv2.imread(os.path.join(f'{root_folder}/images', image_filename))
    label, x, y, w, h = open(os.path.join(f'{root_folder}/labels', label_filename), 'r').readline().split(' ')
    x, y, w, h = [float(xx) for xx in [x, y, w, h]]
    image_h, image_w = img.shape[:2]
    xmin, ymin, xmax, ymax = (x - w / 2) * image_w, (y - h / 2) * image_h, (x + w / 2) * image_w, (y + h / 2) * image_h

    cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (100, 255, 0), thickness=5)
    cv2.imshow('', img)
    cv2.waitKey()
