import os

# path = "/dev/video0"
# rtmp3 = "rtmp://23932540.fme.ustream.tv/ustreamVideo/23932540"
# key3 = "8dzGQnwUVCb2fv8fneMqyBPp9PfA3TT9"

# path = "/home/tyler/TestVideo.mp4"
stream_name = input("Stream Name(Don't use spaces or special characters): ")
rtmp = input("Stream RTMP(s): ")
key = input("Stream Key: ")


#input("Enter to start Stream, Ctrl-c to Quit")

# path = "/home/hpstream/live_stream/TestVideo.mp4"
path = "DeckLink SDI 4K"
format_code = "Hi59"
# key2 = "7c93612e-5506-41f5-986f-2ae1ecc36292"
# rtmp2 = "rtmps://rtmp-global.cloud.vimeo.com:443/live"

# stream = f'ffmpeg -re -stream_loop -1 -i {path} -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high -preset fast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp3}/{key3}'

stream = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high -preset veryfast -trellis 2 -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp}/{key}'

# stream = f'ffmpeg -y -thread_queue_size 90 -hwaccel cuda -channels 2 -raw_format yuv422p10 -format_code {format_code} -f decklink -i "{path}" -c:a pcm_s16le -c:v libx264 -crf 20.0 -crf_max 25.0 -preset fast -trellis 2 -maxrate 2600k -bufsize 5200k -f flv {rtmp3}{key3}'

# stream = f'ffmpeg -format_code Hi60 -f decklink -i "DeckLink SDI 4K" -c:a copy -c:v copy output.avi'

with open(f'{stream_name}.py', 'w') as f:
    f.write(f"import os\nstream = '{stream}' \ninput('Press enter to start stream, Ctrl-c to quit')\nos.system(stream)")

print(f"\nStream File Created\nType: python3 {stream_name}.py to load stream")

