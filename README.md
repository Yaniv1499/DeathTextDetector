YOU DIED Detector
YOU DIED

Table of Contents
Introduction
Prerequisites
Installation
How to Run
Usage
Contributing
Introduction
Welcome to the YOU DIED Detector, a powerful tool that analyzes video content to detect occurrences of the famous "YOU DIED" message from the Dark Souls universe. This tool uses OCR (Optical Character Recognition) combined with color detection to identify the red-colored "YOU DIED" text in videos and creates a highlights reel.

Do you want to relive the moment you perished over and over? This tool will show you where, when, and how often!

Prerequisites
Before you begin, make sure your machine meets the following requirements:

Python 3.7+
Internet connection to install dependencies
Videos featuring YOU DIED in red text for the best experience!
Installation
1. Clone the Repository
git clone https://github.com/yourusername/youdied-detector.git
cd youdied-detector
2. Create a Virtual Environment
This project uses a virtual environment to manage dependencies. To create and activate the environment, run the following:

On Windows:
python -m venv youdied-env
youdied-env\Scripts\activate
On macOS/Linux:
python3 -m venv youdied-env
source youdied-env/bin/activate
3. Install Required Libraries
Install all necessary libraries using the following:

pip install -r requirements.txt
If the requirements.txt is not available, install the libraries manually:

pip install easyocr opencv-python moviepy gradio
How to Run
Ensure you have activated the virtual environment.
Run the Gradio UI:
python youdied_detector.py
This will launch a Gradio interface in your web browser where you can upload videos or provide local file paths.

Usage
How to Use the Gradio Interface:
Upload Your Video:

Either drag and drop a video file into the "Upload Video" box or provide the path to a video file on your computer.
File Upload

Select GPU (Optional):

If your machine supports GPU acceleration, you can check the Use GPU option for faster processing.
Submit the Video:

Hit the Submit button to start the magic. Watch the progress bar update as the tool processes your video!
Progress Bar

View the Results:

The tool will detect every 'YOU DIED' moment and return the total count in a large, eerie red font to match the dark fantasy theme.
Result

Download Highlights:

If 'YOU DIED' moments are found, a link will appear for you to download the highlights reel.
Contributing
Contributions are welcome! Whether you're fixing a bug, adding a feature, or enhancing the design, feel free to fork this repository and submit a pull request.

Steps to Contribute:
Fork the project.
Create your feature branch:
git checkout -b feature/amazing-feature
Commit your changes:
git commit -m 'Add some amazing feature'
Push to the branch:
git push origin feature/amazing-feature
Open a pull request.
May the flames guide thee...

Dark Fantasy Theme
Dark Fantasy

This project is inspired by the dark fantasy genre, much like the world of Dark Souls. The interface has been designed with a somber, eerie aesthetic to match the tone of the legendary "YOU DIED" moment.

License
Distributed under the MIT License. See LICENSE for more information.

Contact
Author: Yaniv Cohen
Project Link: https://github.com/yourusername/youdied-detector
Happy Dying!
