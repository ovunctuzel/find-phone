# find_phone
A simple detector to find phones on the floor and report their coordinates in the image frame.


#### Assumptions
Since the dataset does not contain information regarding the size of the phones, they were assumed to occupy about 10% of the image.
Additionally, it was assumed that only a single phone exists in the image. These assumptions were made based on the images provided in the dataset.

#### Improvements / Future Work
If we are interested in detecting phones of various sizes we can do one or more of the following:
- We can use a model that predicts a heatmap, or just x, y coordinates instead of a set of bounding boxes
- Alternatively we could use augmentation techniques like cropping and padding, or pasting the phones onto a variety of backgrounds to add different sized phones to our dataset

If we are interested in detecting multiple phones, we can combine a set of training images into a single image, similar to YOLO's mosaic augmentation. 
That being said, YOLO does some of this under the hood anyway so it might accurately detect multiple phones already. 
