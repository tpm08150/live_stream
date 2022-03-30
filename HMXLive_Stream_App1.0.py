#!/usr/bin/env python3
from __future__ import print_function

import subprocess
from subprocess import run
import os
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock

import time

Window.size = (1280, 500)


video_input1 = ''
video_input2 = ''
video_label1 = ''
video_label2 = ''

#encoder = "-y -format_code Hi59 -f decklink -i 'DeckLink SDI 4K'"
#format_code = "Hi59"
#path = "DeckLink SDI 4K"
stream_name = "Untitled-Stream"
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
#record_path = "/home/hpstream/Desktop/StreamArchive/"
x = 0
p = 0
v = 0
y = 0
a = 0
q = 0
t = 6
pro = 2
pre = 8
stream = '0'
class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        global video_input
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40

        self.startGrid = GridLayout()
        self.startGrid.cols = 5
        self.startGrid.padding = 4
        self.startGrid.spacing = 2
        self.startGrid.size_hint_y = .2
        self.add_widget(self.startGrid)

        self.StartButton = Button(text='Start Stream', background_color='green', size_hint_x=0.33, size_hint_y=0.1)
        self.startGrid.add_widget(self.StartButton)
        self.StartButton.bind(on_press=self.Start)

        self.streamName = TextInput(multiline=False, hint_text="Stream Name", size_hint_x=0.33, font_size=20)
        self.startGrid.add_widget(self.streamName)

        self.recordPath = TextInput(multiline=False, hint_text="Record Path", size_hint_x=0.33, font_size=20)
        self.startGrid.add_widget(self.recordPath)

        self.StopButton = Button(text='Stop Stream', background_color='gray', background_normal= '', size_hint_x=0.33, size_hint_y=0.1)
        self.startGrid.add_widget(self.StopButton)
        self.StopButton.bind(on_press=self.Stop)

        self.recordViewButton = Button(text='View Recording', background_color='gray', background_normal='', size_hint_x=0.33,
                                 size_hint_y=0.1)
        self.startGrid.add_widget(self.recordViewButton)
        self.recordViewButton.bind(on_press=self.recordView)

        self.PrevGrid = GridLayout()
        self.PrevGrid.cols = 4
        self.PrevGrid.padding = 4
        self.PrevGrid.spacing = 2
        self.PrevGrid.size_hint_y = .2
        self.add_widget(self.PrevGrid)

        self.PreviewButton = Button(text='Preview Video', background_color='purple', size_hint_x=0.33, size_hint_y=0.1)
        self.PrevGrid.add_widget(self.PreviewButton)
        self.PreviewButton.bind(on_press=self.Preview)

        self.PreviewAudioButton = Button(text='Audio Meter', background_color='purple', size_hint_x=0.33, size_hint_y=0.1)
        self.PrevGrid.add_widget(self.PreviewAudioButton)
        self.PreviewAudioButton.bind(on_press=self.Preview_audio)

        self.ResGrid = GridLayout()
        self.ResGrid.cols = 5
        self.ResGrid.padding = 4
        self.ResGrid.spacing = 2
        self.ResGrid.size_hint_y = .2
        self.add_widget(self.ResGrid)

        self.inputLabel = Label(text="Decklink Input Resolution", size_hint_x=.25)
        self.ResGrid.add_widget(self.inputLabel)

        self.Hi59Button = Button(text='1080i 59.94', background_color='blue', size_hint_x=0.15, size_hint_y=0.1)
        self.ResGrid.add_widget(self.Hi59Button)
        self.Hi59Button.bind(on_press=self.Hi59)

        self.Hi60Button = Button(text='1080i 60', background_color='gray', size_hint_x=0.15, size_hint_y=0.1)
        self.ResGrid.add_widget(self.Hi60Button)
        self.Hi60Button.bind(on_press=self.Hi60)

        self.Hp59Button = Button(text='1080p 29.97', background_color='gray', size_hint_x=0.15, size_hint_y=0.1)
        self.ResGrid.add_widget(self.Hp59Button)
        self.Hp59Button.bind(on_press=self.Hp59)

        self.Hp60Button = Button(text='1080p 30', background_color='gray', size_hint_x=0.15, size_hint_y=0.1)
        self.ResGrid.add_widget(self.Hp60Button)
        self.Hp60Button.bind(on_press=self.Hp60)

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

        self.tuneGrid = GridLayout()
        self.tuneGrid.cols = 10
        self.tuneGrid.padding = 4
        self.tuneGrid.spacing = 2
        self.tuneGrid.size_hint_y = .15
        self.add_widget(self.tuneGrid)

        self.tune_label = Label(text='Tune', size_hint_x=0.2)
        self.tuneGrid.add_widget(self.tune_label)

        self.tune1Button = Button(text='Film', background_color='yellow', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune1Button)
        self.tune1Button.bind(on_press=self.tune1)

        self.tune2Button = Button(text='Animation', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune2Button)
        self.tune2Button.bind(on_press=self.tune2)

        self.tune3Button = Button(text='Grain', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune3Button)
        self.tune3Button.bind(on_press=self.tune3)

        self.tune4Button = Button(text='StillImage', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune4Button)
        self.tune4Button.bind(on_press=self.tune4)

        self.tune5Button = Button(text='psnr', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune5Button)
        self.tune5Button.bind(on_press=self.tune5)

        self.tune6Button = Button(text='ssim', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune6Button)
        self.tune6Button.bind(on_press=self.tune6)

        self.tune7Button = Button(text='Fastdecode', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune7Button)
        self.tune7Button.bind(on_press=self.tune7)

        self.tune8Button = Button(text='Zerolatency', background_color='gray', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune8Button)
        self.tune8Button.bind(on_press=self.tune8)

        self.tune_label = Label(text='', size_hint_x=0.1)
        self.tuneGrid.add_widget(self.tune_label)

        self.profileGrid = GridLayout()
        self.profileGrid.cols = 10
        self.profileGrid.padding = 4
        self.profileGrid.spacing = 2
        self.profileGrid.size_hint_y = .15
        self.add_widget(self.profileGrid)

        self.profile_label = Label(text='Profile', size_hint_x=0.2)
        self.profileGrid.add_widget(self.profile_label)

        self.profile1Button = Button(text='Baseline', background_color='yellow', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile1Button)
        self.profile1Button.bind(on_press=self.profile1)

        self.profile2Button = Button(text='Main', background_color='gray', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile2Button)
        self.profile2Button.bind(on_press=self.profile2)

        self.profile3Button = Button(text='High', background_color='gray', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile3Button)
        self.profile3Button.bind(on_press=self.profile3)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.profile_label = Label(text='', size_hint_x=0.1)
        self.profileGrid.add_widget(self.profile_label)

        self.presetGrid = GridLayout()
        self.presetGrid.cols = 10
        self.presetGrid.padding = 4
        self.presetGrid.spacing = 2
        self.presetGrid.size_hint_y = .15
        self.add_widget(self.presetGrid)

        self.preset_label = Label(text='CPU Usage Preset', size_hint_x=0.2)
        self.presetGrid.add_widget(self.preset_label)

        self.preset1Button = Button(text='veryslow', background_color='yellow', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset1Button)
        self.preset1Button.bind(on_press=self.preset1)

        self.preset2Button = Button(text='slower', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset2Button)
        self.preset2Button.bind(on_press=self.preset2)

        self.preset3Button = Button(text='slow', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset3Button)
        self.preset3Button.bind(on_press=self.preset3)

        self.preset4Button = Button(text='medium', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset4Button)
        self.preset4Button.bind(on_press=self.preset4)

        self.preset5Button = Button(text='fast', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset5Button)
        self.preset5Button.bind(on_press=self.preset5)

        self.preset6Button = Button(text='faster', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset6Button)
        self.preset6Button.bind(on_press=self.preset6)

        self.preset7Button = Button(text='veryfast', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset7Button)
        self.preset7Button.bind(on_press=self.preset7)

        self.preset8Button = Button(text='superfast', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset8Button)
        self.preset8Button.bind(on_press=self.preset8)

        self.preset9Button = Button(text='ultrafast', background_color='gray', size_hint_x=0.1)
        self.presetGrid.add_widget(self.preset9Button)
        self.preset9Button.bind(on_press=self.preset9)

        self.settingsGrid = GridLayout()
        self.settingsGrid.cols = 8
        self.settingsGrid.padding = 4
        self.settingsGrid.spacing = 2
        self.settingsGrid.size_hint_y = .15
        self.add_widget(self.settingsGrid)

        self.bitrate_label = Label(text='Bitrate', size_hint_x=0.15)
        self.settingsGrid.add_widget(self.bitrate_label)

        self.bitrateSet = TextInput(multiline=False, hint_text="ex. 3000", font_size=20, size_hint_x=.1)
        self.settingsGrid.add_widget(self.bitrateSet)

        self.crf_label = Label(text='CRF', size_hint_x=0.15)
        self.settingsGrid.add_widget(self.crf_label)

        self.crfSet = TextInput(multiline=False, hint_text="ex. 20.0", font_size=20, size_hint_x=.1)
        self.settingsGrid.add_widget(self.crfSet)

        self.keyframe_label = Label(text='Keyframe Interval', size_hint_x=0.15)
        self.settingsGrid.add_widget(self.keyframe_label)

        self.keyframeSet = TextInput(multiline=False, hint_text="ex. 2", font_size=20, size_hint_x=.1)
        self.settingsGrid.add_widget(self.keyframeSet)

        self.threadQ_label = Label(text='Thread Queue Size', size_hint_x=0.15)
        self.settingsGrid.add_widget(self.threadQ_label)

        self.threadQSet = TextInput(multiline=False, hint_text="ex. 512", font_size=20, size_hint_x=.1)
        self.settingsGrid.add_widget(self.threadQSet)

        #self.error_check(self)
        self.button_colors_loop(self)


    def Start(self, instance):
        global stream
        global x
        global p
        global video_input
        global v
        global a
        global thread_queue
        global crf
        global bitrate
        global keyframe
        global stream_name
        global i

        stream_name = self.streamName.text
        record_path = self.recordPath.text

        if len(self.threadQSet.text) > 0:
            thread_queue = self.threadQSet.text
        else:
            thread_queue = '512'
        if len(self.crfSet.text) > 0:
            crf = self.crfSet.text
        else:
            crf = '20.0'
        if len(self.bitrateSet.text) > 0:
            bitrate = self.bitrateSet.text
        else:
            bitrate = '3000'
        if len(self.keyframeSet.text) > 0:
            keyframe = self.keyframeSet.text
        else:
            keyframe = '2'

        if a != 0:
            a.kill()
        if v != 0:
            v.kill()

        self.StartButton.background_color = 'red'
        self.StartButton.text = 'Stream Running'

        if x > 0:
            p.kill()
            #q.kill()

        time.sleep(.1)
        i = 0

        while os.path.exists(f'{record_path}/{stream_name}{i}.mp4'):
            i += 1
        ap = '"'
        ap2 = "'"
        x = 0
        print(i)
        if self.recordPath.text != "":
            if self.rtmp1.text == "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=mpegts]{record_path}/{stream_name}{i}.mp4"'

            if self.rtmp1.text != "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'

                #preview = f'ffplay {record_path}{stream_name}{i}.mp4'

                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=flv]{self.rtmp3.text}/{self.key3.text}|' \
                         f'[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text != "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|' \
                         f'[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]{self.rtmp4.text}/{self.key4.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)

        else:
            if self.rtmp1.text == "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                pass

            if self.rtmp1.text != "" and self.rtmp2.text == "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'

                # preview = f'ffplay {record_path}{stream_name}{i}.mp4'

                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text == "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text == "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|' \
                         f'[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)
                x = 1
            if self.rtmp1.text != "" and self.rtmp2.text != "" and self.rtmp3.text != "" and self.rtmp4.text != "":
                stream = f'ffmpeg -y -thread_queue_size {thread_queue} -format_code {format_code} -f decklink -i "{path}"' \
                         f'-map 0 -flags +global_header -c:v libx264 ' \
                         f'-crf {crf} -crf_max {float(crf) * 1.25} -profile {profile} -tune {tune} -preset {preset} -trellis 2 ' \
                         f'-maxrate {bitrate}k -bufsize {str(int(bitrate) * 2)}k -pix_fmt yuv420p -r {framerate} -g {str(int(keyframe) * int(framerate))} -c:a aac -b:a 160k -ac 2 -ar 44100 ' \
                         f'-f tee "[f=flv]{self.rtmp1.text}/{self.key1.text}|[f=flv]{self.rtmp2.text}/{self.key2.text}|' \
                         f'[f=flv]{self.rtmp3.text}/{self.key3.text}|[f=flv]{self.rtmp4.text}/{self.key4.text}|[f=mpegts]{record_path}/{stream_name}{i}.mp4"'
                print(stream)

        #os.system(stream)
        if x > 0:
            p = subprocess.Popen("exec " + stream, stdout=subprocess.PIPE, shell=True)
            #q = subprocess.Popen("exec " + preview, stdout=subprocess.PIPE, shell=True)



        # with open(f'{stream_name}.py', 'w') as f:
        #     f.write("import os\nfrom os.path import exists\ni = 0\nwhile os.path.exists(f'"f'/home/tyler/live_stream/{stream_name}'"{i}.mp4'):\n    i += 1\nfilename = f'"f'{stream_name}'"{i}.mp4'\nstream = f'"f'{stream}'"|[f=flv]/home/hpstream/Desktop/StreamArchive/{filename}"f'{ap}'f'{ap2}'"\ninput('Press enter to start stream, Ctrl-c to quit')\nos.system(stream)")

    def Stop(self, instance):
        global p
       #global q
        self.StartButton.text="Start Stream"
        self.StartButton.background_color='gray'
        if p != 0:
            p.kill()
        #q.kill()

    def Hi59(self, instance):
        global format_code
        format_code = "Hi59"
        self.Hi59Button.background_color = 'blue'
        self.Hi60Button.background_color = 'gray'
        self.Hp59Button.background_color = 'gray'
        self.Hp60Button.background_color = 'gray'
    def Hi60(self, instance):
        global format_code
        format_code = "Hi60"
        self.Hi59Button.background_color = 'gray'
        self.Hi60Button.background_color = 'blue'
        self.Hp59Button.background_color = 'gray'
        self.Hp60Button.background_color = 'gray'
    def Hp59(self, instance):
        global format_code
        format_code = "Hp29"
        self.Hi59Button.background_color = 'gray'
        self.Hi60Button.background_color = 'gray'
        self.Hp59Button.background_color = 'blue'
        self.Hp60Button.background_color = 'gray'
    def Hp60(self, instance):
        global format_code
        format_code = "Hp30"
        self.Hi59Button.background_color = 'gray'
        self.Hi60Button.background_color = 'gray'
        self.Hp59Button.background_color = 'gray'
        self.Hp60Button.background_color = 'blue'


    def Preview(self, instance):
        global c
        global v
        #video = f'ffmpeg -y -format_code {format_code} -f decklink -i "{path}" -i {video_input} -pix_fmt yuv420p -f opengl "Video Preview"'
        video = f"ffmpeg -y -format_code {format_code} -f decklink -i '{path}' -pix_fmt yuv420p -f opengl 'Video Preview'"
        v = subprocess.Popen("exec " + video, stdout=subprocess.PIPE, shell=True)

    def Preview_audio(self, instance):
        global a
        #audio = f"ffmpeg -f alsa -ac 2 -i hw:1 -filter_complex showvolume -f opengl 'audio meter'"
        audio = f"ffmpeg -y -format_code {format_code} -f decklink -i '{path}' -filter_complex showvolume -f opengl 'audio meter'"
        a = subprocess.Popen("exec " + audio, stdout=subprocess.PIPE, shell=True)

    def recordView(self, instance):
        global stream_name
        global i
        record = f"mpv --start=90% {self.recordPath.text}/{stream_name}{i}.mp4"
        # video = f"ffmpeg -y -format_code {format_code} -f decklink -i '{path}' -pix_fmt yuv420p -f opengl 'Video Preview'"
        r = subprocess.Popen("exec " + record, stdout=subprocess.PIPE, shell=True)

    def tune1(self, instance):
        global tune
        global t
        tune = 'film'
        t = 0

    def tune2(self, instance):
        global tune
        global t
        tune = 'animation'
        t = 1

    def tune3(self, instance):
        global tune
        global t
        tune = 'grain'
        t = 2

    def tune4(self, instance):
        global tune
        global t
        tune = 'stillimage'
        t = 3

    def tune5(self, instance):
        global tune
        global t
        tune = 'psnr'
        t = 4

    def tune6(self, instance):
        global tune
        global t
        tune = 'ssim'
        t = 5

    def tune7(self, instance):
        global tune
        global t
        tune = 'fastdecode'
        t = 6

    def tune8(self, instance):
        global tune
        global t
        tune = 'zerolatency'
        t = 7

    def profile1(self, instance):
        global profile
        global pro
        profile = 'baseline'
        pro = 0

    def profile2(self, instance):
        global profile
        global pro
        profile = 'main'
        pro = 1

    def profile3(self, instance):
        global profile
        global pro
        profile = 'high'
        pro = 2

    def preset1(self, instance):
        global preset
        global pre
        preset = 'veryslow'
        pre = 0

    def preset2(self, instance):
        global preset
        global pre
        preset = 'slower'
        pre = 1

    def preset3(self, instance):
        global preset
        global pre
        preset = 'slow'
        pre = 2

    def preset4(self, instance):
        global preset
        global pre
        preset = 'medium'
        pre = 3

    def preset5(self, instance):
        global preset
        global pre
        preset = 'fast'
        pre = 4

    def preset6(self, instance):
        global preset
        global pre
        preset = 'faster'
        pre = 5

    def preset7(self, instance):
        global preset
        global pre
        preset = 'veryfast'
        pre = 6

    def preset8(self, instance):
        global preset
        global pre
        preset = 'superfast'
        pre = 7

    def preset9(self, instance):
        global preset
        global pre
        preset = 'ultrafast'
        pre = 8

    # def bitrate(self):
    #     global bitrate
    #     bitrate = self.bitrateSet.text
    # def crf(self):
    #     global crf
    #     crf = self.crfSet.text
    # def keyframe(self):
    #     global keyframe
    #     keyframe = self.keyframeSet.text
    # def theadQ(self):
    #     global thread_queue
    #     thread_queue = self.threadQSet.text

    # def error_check(self, instance):
    #     global stream
    #     cmd = [f'ffprobe -v quiet -print_format json -show_streams {stream}']
    #     health = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    #     stream_health = health.communicate()[0]
    #     print(stream_health)
    #     errorClock = Clock.schedule_once(self.error_check, 2)

    def button_colors_loop(self, instance):
        global t
        global pre
        global pro
        tuneList = [self.tune1Button, self.tune2Button, self.tune3Button, self.tune4Button,
                    self.tune5Button, self.tune6Button, self.tune7Button, self.tune8Button,]

        presetList = [self.preset1Button, self.preset2Button, self.preset3Button, self.preset4Button,
                      self.preset5Button, self.preset6Button, self.preset7Button,self.preset8Button, self.preset9Button]

        profileList = [self.profile1Button, self.profile2Button, self.profile3Button]

        x = 0
        for i in tuneList:
            if x == t:
                tuneList[x].background_color = 'yellow'
            else:
                tuneList[x].background_color = 'gray'
            x += 1

        x = 0
        for i in profileList:
            if x == pro:
                profileList[x].background_color = 'yellow'
            else:
                profileList[x].background_color = 'gray'
            x += 1

        x = 0
        for i in presetList:
            if x == pre:
                presetList[x].background_color = 'yellow'
            else:
                presetList[x].background_color = 'gray'
            x += 1

        button_colors = Clock.schedule_once(self.button_colors_loop, 0.1)


class MyApp(App):
    def build(self):
        self.title = 'HMXLive Streaming App'
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()
p.kill()
v.kill()