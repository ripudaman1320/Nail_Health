# import streamlit as st
# import cv2
# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# st.set_page_config(page_title="VIDEO - YOLO Object Detection",
#                    layout='wide',
#                    page_icon='./images/nail.png')

# class VideoTransformer(VideoTransformerBase):
#     def transform(self, frame):
#         img = frame.to_ndarray(format="bgr24")

#         img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

#         return img

# webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

import streamlit as st
import torch
from PIL import Image
import cv2
import numpy as np

from yolov5 import detect

CFG_MODEL_PATH = "models/yolo_nail200.pt"
deviceoption = "CPU"

model = torch.hub.load('ultralytics/yolov5', 'custom', path=CFG_MODEL_PATH, force_reload=True, device=deviceoption)

def run_object_detection(image):
    results = model(image)
    return results

def main():
    st.title("Real-Time Health Nail Object Detection")
    st.write("Detecting diseases in real-time from your webcam!")

    video_capture = cv2.VideoCapture(0)

    # Create placeholder for displaying the processed video
    processed_video_placeholder = st.empty()

    while True:
        _, frame = video_capture.read()

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the RGB frame to PIL Image
        image = Image.fromarray(frame_rgb)

        # Run object detection on the frame
        results = run_object_detection(image)

        # Convert the PIL Image back to RGB array
        frame_processed = np.array(image.convert('RGB'))

        # Draw bounding boxes on the processed frame
        for detection in results.pandas().xyxy[0].iterrows():
            _, data = detection
            x1, y1, x2, y2 = int(data['xmin']), int(data['ymin']), int(data['xmax']), int(data['ymax'])
            label = f"{data['name']} {data['confidence']:.2f}"
            frame_processed = cv2.rectangle(frame_processed, (x1, y1), (x2, y2), (0, 255, 0), 2)
            frame_processed = cv2.putText(frame_processed, label, (x1, y1 - 10),
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the processed video frame
        processed_video_placeholder.image(frame_processed, channels="RGB", use_column_width=True)

    video_capture.release()


if __name__ == '__main__':
    main()