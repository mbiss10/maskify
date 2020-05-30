# Maskify
Uses dlib and OpenCV to detect facial landmarks and then paste images of masks (appropriately scaled and rotated) onto faces in an image. Works best with frontal images. Facial landmarks come from the dlib predictor's 68-point framework that was trained on the iBUG 300-W dataset.  

Inspiration and code snippets from [Adrian Rosebrock's articles](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/) on facial landmarks from [pyimagesearch.com](https://www.pyimagesearch.com/).  

### Example
Input image:  
![photo14](https://user-images.githubusercontent.com/50077908/83337605-ff432b00-a28a-11ea-9441-624c1c9b70fd.jpg)

Output image:  


### Getting Started
Maskify requires the [OpenCV](https://github.com/opencv/opencv) and [dlib](https://github.com/davisking/dlib) libraries. It also uses [imutils](https://github.com/jrosebr1/imutils) for helper functions and Pillow for basic image editing.  
The maskify.py script assumes that dlib’s pre-trained facial landmark detector (shape_predictor_68_face_landmarks.dat) has been downloaded, with that exact name, and is saved to the same directory as the Python script.  

### Usage  
Specify the image path using the --image argument. For example:  
```
python maskify.py --image images/test_photo1.jpg
```
