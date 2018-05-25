from mutagen.mp3 import MP3
import os
import time

audio = MP3("tmp.mp3")
a = audio.info.length
print (audio.info.length)
os.system('cvlc tmp.mp3')
print (audio.info.length)