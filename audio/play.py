#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 使用音频库播放录音

import pyaudio
import wave
import sys

# 定义数据流块
CHUNK = 1024


def play_voice():
    # if len(sys.argv) < 2:
    #     print("Plays a wave file.\n\nUsage: %s output.wav" % sys.argv[0])
    #     sys.exit(-1)

    # 只读方式打开wav文件
    wf = wave.open(r'output.wav', 'rb')
    p = pyaudio.PyAudio()
    # 打开数据流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 读取数据
    data = wf.readframes(CHUNK)

    print "开始播放录音..."

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    # 停止数据流
    stream.stop_stream()
    stream.close()

    # 关闭 PyAudio
    p.terminate()


if __name__ == '__main__':
    play_voice()
