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

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.voicehat
from google.assistant.library.event import EventType
import aiy.audio
import os
import aiy.cloudspeech
import aiy.voicehat
import naver_tts
import bus
import dust
import vlc
from mutagen.mp3 import MP3
import time
from pygame import mixer
from datetime import datetime
import parser

now = datetime.now()
weekday=now.weekday()
ymd=str(now.year)+"."+now.strftime('%m')+"."+str(now.day)
bus = bus.Bus_data()
dust=dust.Dust_data();
tts = naver_tts.NaverTTS()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def process_event(event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        status_ui.status('ready')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            print('당신이 말하길"', text, '"')
            if '노래 틀어 줘' in text:
                audio = MP3('music1.mp3')
                sleep_time = audio.info.length
                os.system('cvlc ' + 'music1.mp3' + ' --play-and-exit')

            elif '안녕' in text:
                tts.play('안녕하세요 저는 스마트 스페이스에서 제작된, 에이아이 스피커, 스스피커라고 합니다')
            elif '할 수 있어' in text and '뭘' in text:
                tts.play('저는 우리 학교의 필요한 정보들을 알려주는 AI 스피커에요. 오늘의 미세먼지 농도 , 급식, 버스등의 우리 학교에 필요한 정보들을 알려 줄 수 있습니다. ')

            elif '삼각지' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03567')
                    play = '삼각지 역 기준으로' + data + '입니다'
                    tts.play(play);
            elif 'KT 용산지점' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03564')
                    play = 'KT용산지점 기준으로' + data + '입니다'
                    tts.play(play);

            elif '시장' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03516')
                    play = '시장 정거장 기준으로' + data + '입니다'
                    tts.play(play);

            elif '디지텍고' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03509')
                    play = '디지텍고앞 정거장 기준으로' + data + '입니다'
                    tts.play(play);

            elif '녹사평' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03738')
                    play = '녹사평 정거장 기준으로' + data + '입니다'
                    tts.play(play);

            elif '신용산역' in text:
                if '알려' in text or '조회' in text:
                    data = bus.bus_play('03561')
                    play = '신용산역 정거장 기준으로' + data + '입니다'
                    tts.play(play);

            elif '미세먼지' in text and '정보' in text and '초미세먼지' not in text:
                data = dust.dust_play('용산구')
                play = '현재 용산구 미세먼지 농도는 ' + data + '마이크로 그램 입니다'
                tts.play(play);

            elif '초미세먼지' in text and '정보' in text:
                data = dust.dust_play2('용산구')
                play = '현재 용산구 초미세먼지 농도는 ' + data + '마이크로 그램 입니다'
                tts.play(play);

            elif '급식' in text and '알려' in text:
                data = parser.get_diet(2, ymd, weekday)
                play = '오늘의 급식은 ' + data + '입니다'
                tts.play(play);
            elif '석식' in text and '알려' in text:
                data = parser.get_diet(3, ymd, weekday)
                play = '오늘의 석식은 ' + data + '입니다'
                tts.play(play);

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    play_check = vlc.MediaPlayer('tmp.mp3')
    tts.en_play("AI Speaker Ready to Listen")
    mixer.init()

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)


if __name__ == '__main__':
    main()
