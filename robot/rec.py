import wave
from pyaudio import PyAudio, paInt16
import time
import os 
framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/temp/audio.wav'
 
 
def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()
 
 
#录音
def my_record():
    pa = PyAudio()
    #打开一个新的音频stream
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=num_samples)
    my_buf = [] #存放录音数据
 
    t = time.time()
    print('正在录音...')
 
    while time.time() < t + 5:  # 设置录音时间（秒）
        #循环read，每次read 2000frames
        string_audio_data = stream.read(num_samples)
        my_buf.append(string_audio_data)
    print('录音结束.')
    save_wave_file(FILEPATH, my_buf)
    stream.close()
 
