#!/usr/bin/env python3
from __future__ import print_function

import subprocess
import os
from kivy.app import App
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

stream_name = "streamGUIfile"

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40

        self.startGrid = GridLayout()
        self.startGrid.cols = 2
        self.startGrid.padding = 4
        self.startGrid.spacing = 2
        self.startGrid.size_hint_y = .2
        self.add_widget(self.startGrid)

        self.StartButton = Button(text='Start Stream', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.startGrid.add_widget(self.StartButton)
        self.StartButton.bind(on_press=self.Start)

        self.StopButton = Button(text='Stop Stream', background_color='gray', background_normal= '', size_hint_x=0.1, size_hint_y=0.1)
        self.startGrid.add_widget(self.StopButton)
        self.StopButton.bind(on_press=self.Stop)

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
        global p
        x = 0
        x += 1
        p = subprocess.Popen("exec ", stdout=subprocess.PIPE, shell=True)

        p.kill()
        i = 0
        while os.path.exists(f'/home/tyler/live_stream/{stream_name}{i}.mp4'):
            i += 1
        ap = '"'
        ap2 = "'"
        if self.rtmp1.text != "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
            stream = f'ffmpeg -re -stream_loop -1 -i /home/tyler/TestVideo.mp4 -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]/home/tyler/live_stream/{stream_name}{i}.mp4"'
            print(stream)

        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text == "" and self.rtmp4.text == "":
            stream = f'ffmpeg -re -stream_loop -1 -i /home/tyler/TestVideo.mp4 -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]/home/tyler/live_stream/{stream_name}{i}.mp4"'
            print(stream)

        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text == "":
            stream = f'ffmpeg -re -stream_loop -1 -i /home/tyler/TestVideo.mp4 -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]/home/tyler/live_stream/{stream_name}{i}.mp4"'
            print(stream)

        if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text != "":
            stream = f'ffmpeg -re -stream_loop -1 -i /home/tyler/TestVideo.mp4 -map 0 -flags +global_header -c:v libx264 -crf 20.0 -crf_max 25.0 -profile high444 -preset veryfast -trellis 2 ' \
                     f'-maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                     f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]{self.rtmp4.text}/{self.key4.text}|[f=flv]/home/tyler/live_stream/{stream_name}{i}.mp4"'
            print(stream)
        #os.system(stream)
        p = subprocess.Popen("exec " + stream, stdout=subprocess.PIPE, shell=True)

        # with open(f'{stream_name}.py', 'w') as f:
        #     f.write("import os\nfrom os.path import exists\ni = 0\nwhile os.path.exists(f'"f'/home/tyler/live_stream/{stream_name}'"{i}.mp4'):\n    i += 1\nfilename = f'"f'{stream_name}'"{i}.mp4'\nstream = f'"f'{stream}'"|[f=flv]/home/hpstream/Desktop/StreamArchive/{filename}"f'{ap}'f'{ap2}'"\ninput('Press enter to start stream, Ctrl-c to quit')\nos.system(stream)")

    def Stop(self, instance):
        global p
        p.kill()

class MyApp(App):
    def build(self):
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()
p.kill()