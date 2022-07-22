import os
import subprocess
import anvil.server

anvil.server.connect("BJ7CUEVYAKN65RRZA565Q2LF-VEPMLXMUVRW2XS3K")

p = ''
@anvil.server.callable
def stream_start(stream_name, stream_rtmp, stream_key):
    global p
    #stream_name = "Untitled-Stream"
    encoder = "-y -format_code Hi59 -f decklink -i 'DeckLink SDI 4K'"
    format_code = "Hi59"
    path = "DeckLink SDI 4K"
    record_path = "/home/hpstream/Desktop/StreamArchive/"

    resolution = 'hd1080'
    thread_queue = '1024'
    bitrate = '3000'
    crf = '20'
    tune = 'zerolatency'
    profile = 'high'
    preset = 'ultrafast'
    framerate = '30'
    keyframe = '2'

    i = 0
    while os.path.exists(f'{record_path}/{stream_name}{i}.mp4'):
        i += 1

    stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
             f'-map 0 -flags +global_header -c:v libx264 ' \
             f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
             f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
             f'-f tee "[f=flv]{stream_rtmp}/{stream_key}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'

    p = subprocess.Popen("exec " + stream, stdout=subprocess.PIPE, shell=True)

@anvil.server.callable
def stream_end(self):
    global p
    if p != '':
        p.kill()
        p = ''
    # q.kill()

anvil.server.wait_forever()
