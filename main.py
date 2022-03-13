import os


path = "/Users/tylermorton/Downloads/TestVideo.mp4"
rtmp = "rtmp://a.rtmp.youtube.com/live2/"
key = "99m5-7tuu-qmbr-4c7w-3amp"


stream = f'ffmpeg -re -i {path} -c:v libx264 -f flv {rtmp}{key}'

os.system(stream)
