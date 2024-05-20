""" NOTES
01. Install python from https://www.python.org/
02. Run this command only once in CMD/Terminal "pip install opencv-python" (https://pypi.org/project/opencv-python/) 
03. Run the script. It will ask you for full video path and second to take screenshot repeatedly.
04. You will find a folder on desktop containing all the screenshots.


double click on video
hold option to find copy pathname
then copy & paste path name in terminal
"""


# Importing all necessary libraries
import cv2
import os
from tqdm import tqdm

# Read the video from specified path
filename = input('--> input file path: ')
vid = cv2.VideoCapture(filename) # e.x. /Users/walkerhutchinson/Desktop/Dragon Ball Z/dbz 1.mp4
# Getting second
sec = int(input('--> input seconds: '))
# Getting fps
fps = vid.get(cv2.CAP_PROP_FPS)
# Skip frames number
skip_frames = sec*fps

# # creating a folder named data
# save_path = f'C:/Users/{os.getlogin()}/Desktop/Images from video'
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

# creating a folder named data
show = "p"
ep = "1"
save_path = f'Desktop/Images from {show}-ep{ep}'
if not os.path.exists(save_path):
    # print("path does not exist")
    os.makedirs(save_path)

# total frame in file
cap = cv2.VideoCapture(filename)
total_frame_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print("total_frame_length: ", total_frame_length)

# frame
current_frame = 2400

# frame to time

past_second = -1
for current_frame in tqdm(range(total_frame_length)):
# while (True):

    # reading from frame
    ret, frame = vid.read()

    # if video is still left continue creating images
    if ret:
        # Skipping by second
        if (current_frame - 1) % skip_frames == 0:

            frame_div_24 = str(current_frame / 24)
            frame_div_24_a = str(frame_div_24).split(".")[0]
            frame_div24a_div60 = int(frame_div_24_a) / 60

            minute = str(frame_div24a_div60).split(".")[0]
            f2460_back = str(frame_div24a_div60).split(".")[1][0:3]

            if len(str(f2460_back)) == len(str(1)):
                f2460_back = int(f2460_back) / 10
            elif len(str(f2460_back)) == len(str(11)):
                f2460_back = int(f2460_back) / 100
            elif len(str(f2460_back)) == len(str(111)):
                f2460_back = int(f2460_back) / 1000
            else:
                print("error")

            second = 60 * float(f2460_back)
            second = str(second).split(".")[0]
            if past_second == second:
                second = second + "b"
            past_second = second

            timestr = "min" + minute + "-" + "sec" + str(second)
            name = f'{save_path}/' + f'{show}-' + f'ep{ep}-' + timestr + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        current_frame += 1
        # os.system('clear') #on Linux System
    else:
        break

# Release all space and windows once done
vid.release()
# cv2.destroyAllWindows()
