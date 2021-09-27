import cv2
import os

# Check video path and file list
video_path = '../../data/videos'
video_file = os.listdir(video_path)
count = 0

# Capture
for video in video_file:
    cap = cv2.VideoCapture(video_path + '/' + video) # Create video capture object

    if cap.isOpened(): 

        # Check video info
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print('Frame count per second : ', int(fps)) 
        print('Total frame count: ', frame_count)

        # Capture video
        while True:
            ret, frame = cap.read()
            if ret: 
                if count % 15 == 0: # train:1/3, test:1/15
                    cv2.imwrite(f'../../data/video_test/image_{count}.jpg', frame)
            else:
                print('no frame!')
                break
            count += 1
    else:
        print('no camera!')

    cap.release()
    cv2.destroyAllWindows()
