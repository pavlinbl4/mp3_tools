#  To convert mp4 files to mp3 using Python, you can use the moviepy library.
from moviepy.editor import *


def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    # Load mp4 file
    video = VideoFileClip(mp4_file_path)
    # Extract audio from mp4 file
    audio = video.audio
    # Save audio as mp3 file
    audio.write_audiofile(mp3_file_path, bitrate='96k', nbytes=2)
    # Close video and audio objects
    audio.close()
    video.close()
