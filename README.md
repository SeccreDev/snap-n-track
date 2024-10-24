# Snap-n-Track
This project implements a Python-based object detection system using OpenCV's Deep Neural Network (DNN) module.
The system is capable of detecting 20 different object classes in real-time using a pre-trained deep learning model.
It's designed to process video streams or images efficiently and accurately, making it suitable for various computer vision applications.

## Features
- Detects 20 different objects such as people, cars, dogs, and more.
- Real-time performance with optimized object detection algorithms.
- Uses OpenCV DNN to load and run a pre-trained model.
- Can process video streams or static images.
- Easily customizable for adding new models and object classes.

## To be added
GUI

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/SeccreDev/snap-n-track.git](https://github.com/SeccreDev/snap-n-track.git
    
    ```
2. Change to the snap-n-track directory
   ```
   cd snap-n-track
   
   ```
3. Install required dependencies:
    ```
    pip install -r requirements.txt
    
    ```

## How to Run
1. To run :
    ```
    python main.py
    ```
## Additional Information
- After adding the necessary files in the model directory, you can change the pre-trained model and weights in media_detection.py
- You can adjust detection confidence and object classes by modifying the configuration parameters in media_detection.py

## Future Improvements
- Integrate more advanced deep learning models for higher accuracy.
- Optimize for better performance on embedded systems.

## License
[MIT](https://choosealicense.com/licenses/mit/)
