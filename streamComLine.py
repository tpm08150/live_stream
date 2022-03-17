#!/usr/bin/env python3

import os

# path = "/dev/video0"
# rtmp3 = "rtmp://23932540.fme.ustream.tv/ustreamVideo/23932540"
# key3 = "8dzGQnwUVCb2fv8fneMqyBPp9PfA3TT9"
x = 0
# path = "/home/tyler/TestVideo.mp4"
path = "DeckLink SDI 4K"
format_code = "Hi59"
number_of_streams = input("Number of Stream Destinations (1 to 4): ")
stream_name = input("Stream Name(Don't use spaces or special characters): ")

if number_of_streams == "1":
    rtmp = input("Stream RTMP(s): ")
    key = input("Stream Key: ")
    stream = f'ffmpeg -format_code {format_code} -f decklink -i "{path}" -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f tee "[f=flv]{rtmp}/{key}'

if number_of_streams == "2":
    rtmp = input("Stream RTMP(s): ")
    key = input("Stream Key: ")
    rtmp2 = input("Stream RTMP(s) 2: ")
    key2 = input("Stream Key 2: ")
    stream = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f tee "[f=flv]{rtmp}/{key}|[f=flv]{rtmp2}/{key2}'

if number_of_streams == "3":
    rtmp = input("Stream RTMP(s): ")
    key = input("Stream Key: ")
    rtmp2 = input("Stream RTMP(s) 2: ")
    key2 = input("Stream Key 2: ")
    rtmp3 = input("Stream RTMP(s) 3: ")
    key3 = input("Stream Key 3: ")
    stream = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f tee "[f=flv]{rtmp}/{key}|[f=flv]{rtmp2}/{key2}|[f=flv]{rtmp3}/{key3}'

if number_of_streams == "4":
    rtmp = input("Stream RTMP(s): ")
    key = input("Stream Key: ")
    rtmp2 = input("Stream RTMP(s) 2: ")
    key2 = input("Stream Key 2: ")
    rtmp3 = input("Stream RTMP(s) 3: ")
    key3 = input("Stream Key 3: ")
    rtmp4 = input("Stream RTMP(s) 4: ")
    key4 = input("Stream Key 4: ")
    stream = f'ffmpeg -format_code {format_code} -f decklink -i "{path}" -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f tee "[f=flv]{rtmp}/{key}|[f=flv]{rtmp2}/{key2}|[f=flv]{rtmp3}/{key3}|[f=flv]{rtmp4}/{key4}'


ap = '"'
ap2 = "'"
#input("Enter to start Stream, Ctrl-c to Quit")

# path = "/home/hpstream/live_stream/TestVideo.mp4"

# key2 = "7c93612e-5506-41f5-986f-2ae1ecc36292"
# rtmp2 = "rtmps://rtmp-global.cloud.vimeo.com:443/live"

# stream = f'ffmpeg -re -stream_loop -1 -i {path} -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high -preset fast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp3}/{key3}'

# stream = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high -preset veryfast -trellis 2 -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv {rtmp}/{key}'

# stream = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f tee "[f=flv]{rtmp}/{key}|[f=flv]{rtmp2}/{key2}|[f=flv]{stream_name}.mp4"'
# stream = f'ffmpeg -y -thread_queue_size 90 -hwaccel cuda -channels 2 -raw_format yuv422p10 -format_code {format_code} -f decklink -i "{path}" -c:a pcm_s16le -c:v libx264 -crf 20.0 -crf_max 25.0 -preset fast -trellis 2 -maxrate 2600k -bufsize 5200k -f flv {rtmp3}{key3}'

# stream = f'ffmpeg -format_code Hi60 -f decklink -i "DeckLink SDI 4K" -c:a copy -c:v copy output.avi'
i = 0
with open(f'{stream_name}.py', 'w') as f:
    f.write("import os\nfrom os.path import exists\ni = 0\nwhile os.path.exists(f'"f'/home/hpstream/Desktop/StreamArchive/{stream_name}'"{i}.mp4'):\n    i += 1\nfilename = f'"f'{stream_name}'"{i}.mp4'\nstream = f'"f'{stream}'"|[f=flv]/home/hpstream/Desktop/StreamArchive/{filename}"f'{ap}'f'{ap2}'"\ninput('Press enter to start stream, Ctrl-c to quit')\nos.system(stream)")

print(f"\nStream File Created\nType: python3 {stream_name}.py to load stream")
