import os
import cv2
import argparse

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to images or video or videos in dir")
    parser.add_argument("--output", default="./output", help="output dir")
    return parser

def convert_one_video(input_video,output_path):
    assert os.path.basename(input_video).split(".")[1] in ["mp4","avi"],"input video must is .mp4 or .avi"
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    cap = cv2.VideoCapture(input_video)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    length = len(str(frame_count))
    idx_frame = 0
    while True:
        if idx_frame % 100 == 0:
            print(f"Processing {os.path.basename(input_video)} {idx_frame}/{frame_count}")
        ret, frame = cap.read()
        if not ret:
            break
        output_name = os.path.join(output_path,f"{idx_frame:0{length}}.jpg")
        idx_frame += 1
        cv2.imwrite(output_name,frame)
    print("done")
def convert_videos(input_dir,output_path):
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    videos = os.listdir(input_dir)
    for video in videos:
        video_path = os.path.join(input_dir,video)
        convert_one_video(video_path,os.path.join(output_path,video.split(".")[0]))

if __name__ == "__main__":
    args = make_parser().parse_args()

    if os.path.isfile(args.input):
        convert_one_video(args.input,args.output)
    elif os.path.isdir(args.input):
        convert_videos(args.input,args.output)
    else:
        print("The input path does not exist.")

