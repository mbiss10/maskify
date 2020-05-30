# Maskify
Uses dlib and OpenCV to detect facial landmarks and then paste images of masks (appropriately scaled and rotated) onto faces in an image. Works best with frontal images. Facial landmarks come from the dlib predictor's 68-point framework that was trained on the iBUG 300-W dataset.  

Inspiration and code snippets from [Adrian Rosebrock's articles](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/) on facial landmarks from [pyimagesearch.com](https://www.pyimagesearch.com/).  

## Example
Input image:  
![test_photo1](https://user-images.githubusercontent.com/50077908/83337979-cd7f9380-a28d-11ea-80fa-0401618e2cb8.jpg)

Output image:  
![output_maskify](https://user-images.githubusercontent.com/50077908/83337623-31ed2380-a28b-11ea-9151-c11c1d82a2b8.png)

Input image:  
![test_photo2](https://user-images.githubusercontent.com/50077908/83337892-27338e00-a28d-11ea-972b-2097634c1d9c.jpg)

Output image:  
![test_output2](https://user-images.githubusercontent.com/50077908/83337952-927d6000-a28d-11ea-8069-5e831e1550ae.png)

Input image:  
![test_photo3](https://user-images.githubusercontent.com/50077908/83337893-27338e00-a28d-11ea-9c6a-ef27e4dbba70.jpg)


Output image:  
![test_output3](https://user-images.githubusercontent.com/50077908/83337951-914c3300-a28d-11ea-8047-24d9ae0e6f93.png)

Input image:  
![test_photo4](https://user-images.githubusercontent.com/50077908/83337894-27338e00-a28d-11ea-943e-b95a455414e2.jpg)

Output image:  
![test_output4](https://user-images.githubusercontent.com/50077908/83337950-90b39c80-a28d-11ea-88a9-4f23bb6e5228.png)

## Getting Started
Maskify requires the [OpenCV](https://github.com/opencv/opencv) and [dlib](https://github.com/davisking/dlib) libraries. It also uses [imutils](https://github.com/jrosebr1/imutils) for helper functions and Pillow for basic image editing.  
The maskify.py script assumes that dlib’s pre-trained facial landmark detector (shape_predictor_68_face_landmarks.dat) has been downloaded, with that exact name, and is saved to the same directory as the Python script.  

## Usage  
Specify the image path using the --image argument. For example:  
```
python maskify.py --image test_images/test_photo1.jpg
```
All photos used in the examples are included in the test_images folder.  

