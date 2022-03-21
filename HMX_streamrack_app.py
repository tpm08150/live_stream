#!/usr/bin/env python3
from __future__ import print_function

import subprocess
import os
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.slider import Slider
import time

Window.size = (1280, 300)

stream_name = "Untitled-Stream"
encoder = "-y -format_code Hi59 -f decklink -i 'DeckLink SDI 4K'"
#encoder = "-f video4linux2 -framerate 30 -video_size hd1080 -i /dev/video0 -f alsa -ac 2 -i hw:1 "
#record_path = "/home/tyler/"
record_path = "/home/hpstream/Desktop/StreamArchive/"
x = 0
p = 0
v = 0
y = 0
class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40

        self.startGrid = GridLayout()
        self.startGrid.cols = 3
        self.startGrid.padding = 4
        self.startGrid.spacing = 2
        self.startGrid.size_hint_y = .2
        self.add_widget(self.startGrid)

        self.StartButton = Button(text='Start Stream', background_color='green', size_hint_x=0.33, size_hint_y=0.1)
        self.startGrid.add_widget(self.StartButton)
        self.StartButton.bind(on_press=self.Start)

        self.streamName = TextInput(multiline=False, hint_text="Stream Name", size_hint_x=0.33, font_size=20)
        self.startGrid.add_widget(self.streamName)

        self.StopButton = Button(text='Stop Stream', background_color='gray', background_normal= '', size_hint_x=0.33, size_hint_y=0.1)
        self.startGrid.add_widget(self.StopButton)
        self.StopButton.bind(on_press=self.Stop)

        self.PrevGrid = GridLayout()
        self.PrevGrid.cols = 2
        self.PrevGrid.padding = 4
        self.PrevGrid.spacing = 2
        self.PrevGrid.size_hint_y = .2
        self.add_widget(self.PrevGrid)

        self.PreviewButton = Button(text='Preview Video', background_color='blue', size_hint_x=0.33, size_hint_y=0.1)
        self.PrevGrid.add_widget(self.PreviewButton)
        self.PreviewButton.bind(on_press=self.Preview)

        self.PreviewAudioButton = Button(text='Audio Meter', background_color='yellow', size_hint_x=0.33, size_hint_y=0.1)
        self.PrevGrid.add_widget(self.PreviewAudioButton)
        self.PreviewAudioButton.bind(on_press=self.Preview_audio)

        self.rtmpGrid = GridLayout()
        self.rtmpGrid.cols = 2
        self.rtmpGrid.padding = 4
        self.rtmpGrid.spacing = 2
        self.rtmpGrid.size_hint_y = .8
        self.add_widget(self.rtmpGrid)

        self.rtmp1 = TextInput(multiline=False, hint_text="RTMP 1", font_size=20)
        self.rtmpGrid.add_widget(self.rtmp1)

        self.key1 = TextInput(multiline=False, hint_text="Stream Key 1", font_size=20)
        self.rtmpGrid.add_widget(self.key1)

        self.rtmp2 = TextInput(multiline=False, hint_text="RTMP 2", font_size=20)
        self.rtmpGrid.add_widget(self.rtmp2)

        self.key2 = TextInput(multiline=False, hint_text="Stream Key 2", font_size=20)
        self.rtmpGrid.add_widget(self.key2)

        self.rtmp3 = TextInput(multiline=False, hint_text="RTMP 3", font_size=20)
        self.rtmpGrid.add_widget(self.rtmp3)

        self.key3 = TextInput(multiline=False, hint_text="Stream Key 3", font_size=20)
        self.rtmpGrid.add_widget(self.key3)

        self.rtmp4 = TextInput(multiline=False, hint_text="RTMP 4", font_size=20)
        self.rtmpGrid.add_widget(self.rtmp4)

        self.key4 = TextInput(multiline=False, hint_text="Stream Key 4", font_size=20)
        self.rtmpGrid.add_widget(self.key4)


    def Start(self, instance):
        global stream
        global x
        global p
        global v
        stream_name = self.streamName.text

        self.StartButton.background_color='red'
        self.StartButton.text = 'Stream Running'

        if x > 0:
            p.kill()
        x += 1
        time.sleep(.1)
        i = 0

        while os.path.exists(f'{record_path}{stream_name}{i}.mp4'):
            i += 1
        ap = '"'
        ap2 = "'"
        x = 0
        if self.rtmp1.text == "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
            pass

        if self.rtmp1.text != "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
            stream = f'ffmpeg {encoder} -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high -preset ultrafast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{record_path}{stream_name}{i}.mp4"'
            print(stream)
            x = 1
        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text == "" and self.rtmp4.text == "":
            stream = f'ffmpeg {encoder} -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset ultrafast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{record_path}{stream_name}{i}.mp4"'
            print(stream)
            x = 1
        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text == "":
            stream = f'ffmpeg {encoder} -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset ultrafast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]{record_path}{stream_name}{i}.mp4"'
            print(stream)
            x = 1
        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text != "":
            stream = f'ffmpeg {encoder} -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset ultrafast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]{self.rtmp4.text}/{self.key4.text}|[f=flv]{record_path}{stream_name}{i}.mp4"'
            print(stream)

        #os.system(stream)
        if x > 0:
            p = subprocess.Popen("exec " + stream, stdout=subprocess.PIPE, shell=True)

        # with open(f'{stream_name}.py', 'w') as f:
        #     f.write("import os\nfrom os.path import exists\ni = 0\nwhile os.path.exists(f'"f'/home/tyler/live_stream/{stream_name}'"{i}.mp4'):\n    i += 1\nfilename = f'"f'{stream_name}'"{i}.mp4'\nstream = f'"f'{stream}'"|[f=flv]/home/hpstream/Desktop/StreamArchive/{filename}"f'{ap}'f'{ap2}'"\ninput('Press enter to start stream, Ctrl-c to quit')\nos.system(stream)")

    def Stop(self, instance):
        self.StartButton.text="Start Stream"
        self.StartButton.background_color='gray'
        p.kill()


    def Preview(self, instance):
        #video = f"ffmpeg -f video4linux2 -framerate 30 -video_size hd1080 -i /dev/video0 -pix_fmt yuv420p -f opengl 'Video in Preview'"
        video = f"ffmpeg -y -format_code {format_code} -f decklink -i '{path}' -pix_fmt yuv420p -f opengl 'Video Preview'"
        v = subprocess.Popen("exec " + video, stdout=subprocess.PIPE, shell=True)

    def Preview_audio(self, instance):
        #audio = f"ffmpeg -f alsa -i hw:1 -filter_complex showvolume -f opengl 'audio meter'"
        audio = f"ffmpeg -y -format_code {format_code} -f decklink -i '{path}' -filter_complex showvolume -f opengl 'audio meter'"
        a = subprocess.Popen("exec " + audio, stdout=subprocess.PIPE, shell=True)


class MyApp(App):
    def build(self):
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()
p.kill()
v.kill()
