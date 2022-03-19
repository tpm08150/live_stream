import os

os.system("ffmpeg -re -i /home/tylermorton670/motherTest.mp4 -filter_complex showvolume -f opengl 'audio meter'" )
