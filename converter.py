import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    while True:
        # Read frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame as image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_count} frames to '{output_folder}'")

# Testing Usage
video_path = "tv static 720hd 60fps.mp4"
output_folder = "frame8"
extract_frames(video_path, output_folder)
