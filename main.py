import cv2
import argparse
import os

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Perform video extraction to certain image format.")
    parser.add_argument('-i', '--video_path', help="Path of the video", required=True)
    parser.add_argument('-f', '--image_format', help="Path of the video", required=False, default='png')
    parser.add_argument('-v', '--frame_interval', help="Frame interval between saves", required=False, type=int, default=30)
    args = parser.parse_args()
    video_path = args.video_path
    image_format = args.image_format
    fps = args.frame_interval

    # Create new folder
    video_path = os.path.join(os.path.dirname(__file__), video_path)
    folder_path = os.path.splitext(video_path)[0]
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Capturing
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        if count % int(fps) == 0:
            ret, frame = cap.read()
            count_name = "frame%d." % count + str(image_format)
            name = os.path.join(folder_path, count_name)
            cv2.namedWindow("Saving... Press 'q' to exit", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Saving... Press 'q' to exit", 600,600)
            cv2.imshow("Saving... Press 'q' to exit", frame)
            cv2.imwrite(name, frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

if __name__ == "__main__":
    main()

    