from moviepy.editor import  *

video = VideoFileClip("FyyurApp (video-converter.com).mp4")

video.write_gif("my_video.gif")