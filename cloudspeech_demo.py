#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import os
import aiy.cloudspeech
import aiy.voicehat
import naver_tts
import bus
import vlc
from mutagen.mp3 import MP3
import time
from pygame import mixer

bus = bus.Bus_data()
tts = naver_tts.NaverTTS()

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    play_check = vlc.MediaPlayer('tmp.mp3')
    mixer.init()
    while True :
        print('Listening...')
        text = recognizer.recognize()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            print('당신이 말하길"', text, '"')
            if '불 켜' in text:
                 led.set_state(aiy.voicehat.LED.ON)
                 tts.play("불 을  켜드릴꼐요")
            elif 'turn off the light' in text:
                 led.set_state(aiy.voicehat.LED.OFF)
            elif 'blink' in text:
                 led.set_state(aiy.voicehat.LED.BLINK)    
            elif '노래 틀어 줘' in text:
                    audio = MP3('music1.mp3')
                    sleep_time = audio.info.length
                    os.system('cvlc ' + 'music1.mp3' + ' --play-and-exit')
                    
            elif '안녕' in text:
                    tts.play('안녕하세요 저는 스마트 스페이스에서 제작된, 에이아이 스피커, 스스피커라고 합니다')
            elif '삼각지' in text:
                    data = bus.bus_play('03567')
                    play = '삼각지 역 기준으로'+data+'입니다' 
                    tts.play(play);

if __name__ == '__main__':
    main()
