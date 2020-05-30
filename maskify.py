from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math
from PIL import Image

# Inspiration and bits of code from
# https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

# Create argparser and read in the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# Initialize dlib's face detector (HOG-based)
# and create facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
assert image is not None, "image must be valid"
image = imutils.resize(image, width=500)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the grayscale image
rects = detector(grayscale, 1)
print("{} faces found in image. Applying masks...".format(len(rects)))

# Load the mask image and retreive its dimensions
mask = Image.open('mask.png')
w, h = mask.size
mask_aspect_ratio = w/h


# Given two facial landmarks, calculate the angle of head tilt.
# p1 and p2 should be outermost points of left and right eyes, respectively
def get_tilt_angle(p1, p2):
	x1, y1 = p1
	x2, y2 = p2

	# Eye-to-eye horizontal distance (should always be positve)
	leg1 = x2-x1
	# Eye-to-eye vertical distance (positive if left eye above right eye)
	leg2 = y2-y1

	angle = math.atan(leg2/leg1)
	return -1*math.degrees(angle)


# Loop over the face detections
# Create and store mask images and coordinates for each face
masks_to_paste = []
mask_coords = []
for (i, rect) in enumerate(rects):
	shape = predictor(grayscale, rect)
	shape = face_utils.shape_to_np(shape)

	# Calculate angle of head tilt using outermost points of eyes
	left_eye_coords = shape[36]
	right_eye_coords = shape[45]
	tilt_angle = get_tilt_angle(left_eye_coords, right_eye_coords)

	# Determine mask dimensions using Euclidean distance facial landmarks
	mask_height = int(math.sqrt((shape[8][1] - shape[28][1])**2 + (shape[8][0] - shape[28][0])**2))
	mask_width = int(math.sqrt((shape[15][0] - shape[1][0])**2 + (shape[15][1] - shape[1][1])**2))
	mask_dims = (mask_width, mask_height)

	# Create mask image to be pasted onto face
	new_mask = mask.copy()
	new_mask = new_mask.resize(mask_dims)

	# Determine coordinates to paste mask
	# Due to rotation, handle left vs. right head tilts differently
	if tilt_angle > 0:
		# Treat upper right corner of pasted image as the pivot
		# and use the right side of the jawline as a reference
		new_mask = new_mask.rotate(tilt_angle, expand=True, center=(0,0))
		mask_x = shape[15][0] - mask_width - int(abs(tilt_angle/90)*mask_width)
		mask_y = shape[15][1]
	else:
		# Treat upper left corner of pasted image as the pivot
		# and use the left side of the jawline as a reference
		new_mask = new_mask.rotate(tilt_angle, expand=True, center=(mask_width,0))
		mask_x = shape[1][0] - int(abs(tilt_angle/90)*mask_width)
		mask_y = shape[1][1]

	# Store mask image and coordinates for this face
	masks_to_paste.append(new_mask)
	mask_coords.append((mask_x, mask_y))


# Access background image for PIL processing 
cv2.imwrite("output_img.png", image)
result = Image.open('output_img.png')
# Paste masks onto each face at the calculated coordinates
for new_mask_img, new_mask_coords in zip(masks_to_paste, mask_coords):
	result.paste(new_mask_img, new_mask_coords, new_mask_img)
# Save the output
result.save('output_img.png', quality=95)

# Display the final photo
result = cv2.imread('output_img.png')
cv2.imshow("Output", result)
cv2.waitKey(0)
