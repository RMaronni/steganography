from cv2 import *
import os


def jpg_to_png(img_path):

	img = imread(img_path)
	imwrite(os.path.splitext(img_path)[0] + ".png", img)


# img_path = "/Users/renanmaronni/Projects/steganografia-python/woman.jpg"
# img = imread(img_path)

# img_crop = img[211:-250, :]

# imwrite(os.path.splitext(img_path)[0] + "_resized.png", img_crop)

img_path = "/Users/renanmaronni/Projects/steganografia-python/woman.png"
img_path2 = "/Users/renanmaronni/Projects/steganografia-python/woman.png"
img = imread(img_path)
rows, columns, channels = img.shape
rows = rows//4
columns = columns//4
img = resize(img, (rows, columns))
imwrite(img_path2, img)

img_path = "/Users/renanmaronni/Projects/steganografia-python/woman.jpg"

# jpg_to_png(img_path)


