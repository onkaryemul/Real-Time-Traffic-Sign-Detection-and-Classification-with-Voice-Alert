
Real-Time Detection and Classification of Traffic Signs using YOLOv5s object detection algorithm. This project incorporates multilingual voice alerts and a user-friendly Tkinter-based GUI with various camera options for enhanced road safety.


# Real-Time Traffic Sign Detection and Classification with Voice Alert

An advanced real-time traffic sign detection and classification system with voice alert capabilities. The project employs YOLOv5 for accurate and swift detection, providing multilingual voice alerts through a user-friendly Tkinter GUI. Enhance road safety and driving experience with this comprehensive solution.


## Table of Contents

- [Features](#features)
- [Multilingual Alerts and Tkinter GUI](#multilingual-alerts-and-tkinter-gui)
- [Technologies Used](#technologies-used)
- [System Requirement](#system-requirement)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Features

1. **Real-Time Detection:** Achieve up to 45 fps for swift and accurate traffic sign detection.
2. **Multilingual Voice Alerts:** Receive alerts in English, Hindi, and Marathi for diverse user communication.
3. **Tkinter GUI:** Intuitive graphical interface providing clear visual and audio feedback.
4. **Multiple Camera Options:** Support for default laptop camera, USB camera, and wireless or IP camera.


## Multilingual Alerts and Tkinter GUI

The project provides voice alerts in English, Hindi, and Marathi using the gtts library. The Tkinter-based GUI ensures a user-friendly interface, offering visual and audio notifications for identified traffic signs.


## Technologies Used

- YOLOv5
- OpenCV
- gtts (Google Text-to-Speech)
- Tkinter


## System Requirement

1. **Operating System:** Windows 10/11
2. **Python Version:** 3.8 to 3.11.5 (preferably 3.11.5)
3. **Internet Connectivity:** Required for voice alerts using gtts library
4. **Camera:** Default camera of laptop/USB camera/wireless or IP camera


## Installation

1. **Clone the repository:**

    ```bash
      git clone https://github.com/onkaryemul/Real-Time-Traffic-Sign-Detection-and-Classification-with-Voice-Alert.git
    ```

2. **Navigate to the project directory:**

   ```bash
     cd Real-Time-Traffic-Sign-Detection-and-Classification-with-Voice-Alert
   ```

3. **Install dependencies:**

    ```bash
      pip install -r requirements.txt
    ```

### Installation instructions for `playsound` library:

If you encounter issues with automatic installation, you can install playsound manually by following these steps:

1. Download the source code from the playsound GitHub repository: [playsound on GitHub](https://github.com/TaylorSMarks/playsound).
2. Extract the downloaded archive.
3. Open a command prompt or terminal in the extracted directory.
4. Run the following command to install playsound:

   ```bash
     python setup.py install
   ```


## Usage

1. **Navigate to the Codes directory** inside main project Real-Time-Traffic-Sign-Detection-and-Classification-with-Voice-Alert :

    ```bash
      cd Codes
    ```

2. **Run the detection script** with the desired parameters
   For running on the Default Webcam of the laptop, run:

    ```bash
      python detect.py --source 0
    ```

    **OR**

   **Run the Python TKinter GUI Application script** by executing following command:

   ```bash
      python gui.py
   ```

### Instructions for providing Wireless or IP Camera Streaming URL:

In the streaming URL entry, you can use the following format for an IP camera:

   ```plaintext
     **For general format:** http://username:password@IP:PORT/video
     **Example:** http://admin:your_password@192.168.1.100:8080/video
   ```

Make sure to replace 'username', 'password', 'IP', 'PORT', and 'your_password' with the actual credentials and details of your IP camera.

For more details on accessing IP cameras in Python using OpenCV, refer to the following Stack Overflow post: 
[Access IP Camera in Python OpenCV](https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv)


### Testing:

1. **Navigate to the Codes directory**:
   
   ```bash
     cd Codes
   ```
   
2. **For testing:**
   Before running the next command, put your test file in the directory named `Test`.

   ```bash 
     python detect.py --source ../Test/(name of your file)
   ```

   For example, if your image name is test.jpg, then put your image in the directory named `Test` and run:

   ```bash 
     python detect.py --source ../Test/test1.jpeg
   ```
   
   Above, the same step can also be used to test the model on video files.


## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Please follow best practices and maintain code clarity.

If you would like to contribute to the project, follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```bash
     git checkout -b feature/your-feature-name
   ```
   
3. Make your changes and commit:

   ```bash
     git commit -m "Add your feature"
   ```

4. Push to your branch:

   ```bash
     git push origin feature/your-feature-name
   ```
   
5. Create a pull request on GitHub.

