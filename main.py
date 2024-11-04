import os
import re
import sys
import shutil
import glob
import cv2

from moviepy.editor import VideoFileClip

def main(): 
    root_directory = ""
    
    # 最下層ディレクトリのリストを取得
    bottom_directories = get_bottom_directories(root_directory)
    for dir in bottom_directories:
        print(dir)

    for dir in bottom_directories:
        # ディレクトリ内の動画ファイルを取得
        video_files = glob.glob(os.path.join(dir, "*.mp4"))
        video_files = glob.glob(os.path.join(dir, "*.MP4"))
        # video_files += glob.glob(os.path.join(dir, "*.avi"))
        video_files += glob.glob(os.path.join(dir, "*.mov"))
        video_files += glob.glob(os.path.join(dir, "*.MOV"))
        video_files += glob.glob(os.path.join(dir, "*.wmv"))
        video_files += glob.glob(os.path.join(dir, "*.flv"))
        video_files += glob.glob(os.path.join(dir, "*.mkv"))
    
        # 動画ファイルがない場合はスキップ
        if not video_files:
            continue

        # 動画ファイルの解像度を取得
        video_resolutions = []
        for video_file in video_files:
            resolution = get_video_resolution(video_file)
            print(video_file, resolution)
            if resolution:
                video_resolutions.append(resolution)
        
        # for resolution in video_resolutions:
        #     print(resolution)


        # # 解像度が一意でない場合はスキップ
        # if len(set(video_resolutions)) != 1:
        #     continue
        
        print()

    
        

# ディレクトリ内の全ての最下層ディレクトリを取得
def get_bottom_directories(root_dir):
    bottom_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # サブディレクトリがない場合は最下層ディレクトリと見なす
        if not dirnames:
            bottom_dirs.append(dirpath)
    return sorted(bottom_dirs)
    
# 動画の解像度を取得
def get_video_resolution(video_path):
    clip = VideoFileClip(video_path)
    width, height = clip.size
    clip.close()
    return width, height

if __name__ == "__main__":
    main()

