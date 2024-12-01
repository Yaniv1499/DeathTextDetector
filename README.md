:)
---
# YOU DIED Detector
## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction
Welcome to the YOU DIED Detector, a powerful tool that analyzes video content to detect occurrences of the famous "YOU DIED" message from the Dark Souls universe. This tool uses OCR (Optical Character Recognition) combined with color detection to identify the red-colored "YOU DIED" text in videos and creates a highlights reel.

Do you want to relive the moment you perished over and over? This tool will show you where, when, and how often!

## Prerequisites
Before you begin, make sure your machine meets the following requirements:
- Python 3.7+
- Internet connection to install dependencies
- Videos featuring YOU DIED in red text for the best experience!

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/DeathTextDetector.git
    cd DeathTextDetector
    ```

2. **Create a Virtual Environment**
    This project uses a virtual environment to manage dependencies. To create and activate the environment, run the following:

    On Windows:
    ```bash
    python -m venv DeathTextDetector
    DeathTextDetector\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    python3 -m venv DeathTextDetector
    source DeathTextDetector/bin/activate
    ```

3. **Install Required Libraries**
    Install all necessary libraries using the following:
    ```bash
    pip install -r requirements.txt
    ```
    If the `requirements.txt` is not available, install the libraries manually:
    ```bash
    pip install easyocr opencv-python moviepy gradio
    ```

## How to Run
1. Ensure you have activated the virtual environment.
2. Run the Gradio UI:
    ```bash
    python DeathTextDetector.py
    ```
    This will launch a Gradio interface in your web browser where you can upload videos or provide local file paths.

## Usage
### How to Use the Gradio Interface:
1. **Upload Your Video:**
    Either drag and drop a video file into the "Upload Video" box or provide the path to a video file on your computer.

2. **Select GPU (Optional):**
    If your machine supports GPU acceleration, you can check the Use GPU option for faster processing.

3. **Submit the Video:**
    Hit the Submit button to start the magic. Watch the progress bar update as the tool processes your video!

4. **View the Results:**
    The tool will detect every 'YOU DIED' moment and return the total count in a large, eerie red font to match the dark fantasy theme.

5. **Download Highlights:**
    If 'YOU DIED' moments are found, a link will appear for you to download the highlights reel.


May the flames guide thee...

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
**Author:** Yaniv Cohen  
**Project Link:** [DeathTextDetector](https://github.com/yourusername/DeathTextDetector)

Happy Dying!

---

