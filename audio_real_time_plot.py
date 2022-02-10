import matplotlib.pyplot as plt
import pyaudio
import numpy as np
import wave
# Figure declaration
fig = plt.figure('Sound Amplitude', figsize=(13,7))
ax = fig.add_subplot(1, 1, 1)
# Sound Processes Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
# Audio Opening

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
frames = []
while True:
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)
        signal = b''.join(frames)
        amplitude = np.frombuffer(signal, np.int16)
        # ploting
        ax.plot(amplitude, c='royalblue')
        plt.title("Sound Wave")
        plt.xlabel("Time[s]")
        plt.ylabel("Amplitude")
        plt.pause(0.05)
        # Saving record
        waveFile = wave.open("coursee.wav", 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
plt.close()
# Stoping our recording
stream.stop_stream()
stream.close()
audio.terminate()