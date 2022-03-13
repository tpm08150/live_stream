import os

# path = "/dev/video0"
rtmp3 = "rtmp://23932540.fme.ustream.tv/ustreamVideo/23932540"
key3 = "8dzGQnwUVCb2fv8fneMqyBPp9PfA3TT9"

#path = "/home/tyler/TestVideo.mp4"
rtmp2 = "rtmp://a.rtmp.youtube.com/live2"
key2 = "99m5-7tuu-qmbr-4c7w-3amp"

path = "/home/tyler/TestVideo.mp4"
key = "FB-144569794714659-0-Abz772aNGLg18V2J"
rtmp = "rtmps://live-api-s.facebook.com:443/rtmp"

stream = f'ffmpeg -re -stream_loop -1 -i {path} -c:v libx264 -preset ultrafast -maxrate 6000k -bufsize 12000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp3}/{key3}'

#stream = f'ffmpeg -f v4l2 -framerate 30 -video_size 1280x720 -i {path} -f alsa -i hw:1 -c:v libx264 -preset ultrafast -maxrate 6000k -bufsize 12000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp}{key}'

os.system(stream)
