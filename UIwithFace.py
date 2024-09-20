import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import easyocr
import cv2
import numpy as np
import time
import logging
import os
import moviepy.editor as mp
import gradio as gr

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("youdied_log.txt"), logging.StreamHandler()]
)

# Class for detecting 'YOU DIED' in video frames using EasyOCR
class Youdied:
    def __init__(self, video_path, use_gpu):
        self.video_path = video_path
        self.reader = easyocr.Reader(['en'], gpu=use_gpu)


    def process_frame_for_text(self, frame):
        if frame is None:
            return False
        
        # Convert the frame to the HSV color space for easier color detection
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define lower and upper bounds for the red color in HSV space
        lower_red1 = np.array([0, 50, 50])  # Lower bound for the first red hue
        upper_red1 = np.array([10, 255, 255])  # Upper bound for the first red hue
        lower_red2 = np.array([170, 50, 50])  # Lower bound for the second red hue
        upper_red2 = np.array([180, 255, 255])  # Upper bound for the second red hue

        # Create masks to detect red areas in the frame
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        # Combine both masks
        red_mask = cv2.bitwise_or(mask1, mask2)

        # Apply the red mask to the original frame to extract only red regions
        red_regions = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Resize the red regions for OCR to balance speed and accuracy
        scale = 0.7  # Adjust the scaling factor
        resized_red_regions = cv2.resize(red_regions, (0, 0), fx=scale, fy=scale)

        # Use EasyOCR to extract text from the red-marked regions
        result = self.reader.readtext(resized_red_regions)

        # Check if "YOU DIED" is in the detected text
        for (bbox, text, prob) in result:
            if "YOU DIED" in text.upper() or "DEATH" in text.upper():
                logging.info("'YOU DIED' detected in red!")
                return True  # "YOU DIED" found in red
        return False  # "YOU DIED" not found or not in red
            

    def count_you_died(self):
        start_time = time.time()  # Start measuring runtime
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            logging.error("Error: Could not open video.")
            return -1, None

        count = 0
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        sec = 0.8  # Changeable // maybe a condition for assign 
        skip_frames = int(frame_rate * sec)  # Process every X seconds worth of frames
        
        last_you_died = -float('inf')
        same_event_threshold = 3  # Changeable, Number of seconds to consider the same event
        you_died_frames = []  # To store frames where "YOU DIED" is detected
        highlights_clips = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            
            # Process every 'skip_frames' frame
            if current_frame % skip_frames == 0:
                if self.process_frame_for_text(frame):
                    if (current_frame - last_you_died > same_event_threshold * frame_rate):
                        count += 1
                        last_you_died = current_frame
                        logging.info(f"'YOU DIED' detected! Count: {count}")
                        you_died_frames.append(current_frame)
                        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame + skip_frames)

        cap.release()
        end_time = time.time()  # End measuring runtime
        total_time = end_time - start_time
        logging.info(f"Total runtime: {total_time:.2f} seconds")

        # Create highlights clip if there were any detections
        if you_died_frames:
            video = mp.VideoFileClip(self.video_path)
            for frame_num in you_died_frames:
                start_time = frame_num / frame_rate
                clip = video.subclip(max(0, start_time - 10), start_time + 2)  # 1 second before and 2 seconds after "YOU DIED"
                highlights_clips.append(clip)

            if highlights_clips:
                highlights = mp.concatenate_videoclips(highlights_clips)
                highlights_output_path = "highlights_you_died.mp4"
                highlights.write_videofile(highlights_output_path)
                logging.info(f"Highlights saved at {highlights_output_path}")
                return count, highlights_output_path

        return count, None


# Gradio Interface
def process_video(video_file, video_path, use_gpu=True):
    if video_file is not None:
        video_path = video_file.name  # Use the uploaded video file
    elif video_path:  # Use the file path provided if no video is uploaded
        if not os.path.exists(video_path):
            return "Error: The provided video path does not exist.", None

    if video_path:
        # Initialize Youdied class and process video
        youdied = Youdied(video_path, use_gpu)
        count, highlights_path = youdied.count_you_died()

        if highlights_path:
            result_message = f"<h2 style='color:red;'>'YOU DIED' moments detected <span style='font-size: 2em;'>{count}</span> times.</h2>"
            return result_message, highlights_path
        else:
            result_message = f"<h3>No 'YOU DIED' moments detected. Total count: <span style='font-size: 1.5em;'>{count}</span>.</h3>"
            return result_message, None
    else:
        return "Please upload a video file or provide a valid file path.", None


# Gradio UI Setup
with gr.Blocks() as ui:
    with gr.Column():
        gr.Markdown("""
        <h1 style="text-align:center; color:#FF6347;">YOU DIED Detector</h1>
        <p style="text-align:center; font-size:1.2em;">Upload a video or provide a file path to detect Moments of 'YOU DIED',Press Sumbit and wait until You can  download a highlights video.</p>
        """)

    progress_textbox = gr.Markdown("**Progress**: Waiting for video upload or file path input...", elem_id="progress")

    with gr.Row():
        video_input = gr.File(label="Upload Video (Optional)", file_types=["video"])
        video_path_input = gr.Textbox(label="Or Provide Video File Path (BEST AND FAST OPTION!)")
        use_gpu_input = gr.Checkbox(label="Use GPU", value=True)

    submit_button = gr.Button("Submit")

    result = gr.Markdown(label="Result", elem_id="result")
    download_link = gr.File(label="Download Highlights of You Died Moments:")

    def process_video_with_progress(video_file, video_path, use_gpu):
        progress_text = "Processing started..."
        result_message, highlights_path = process_video(video_file, video_path, use_gpu)

        return progress_text, result_message, highlights_path

    # Trigger processing when the Submit button is clicked
    submit_button.click(fn=process_video_with_progress, inputs=[video_input, video_path_input, use_gpu_input], outputs=[progress_textbox, result, download_link])

    ui.launch(share=True)