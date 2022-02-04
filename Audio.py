import pyaudio # Soundcard audio I/O access library
import wave, sys # Python 3 module for reading / writing simple .wav files
import matplotlib.pyplot as plt
import numpy as np
# Processing Parameters
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 10 # Record time
CHANNELS = 2
CHUNK = 1024
RATE = 44100
# Startup pyaudio instance
audio = pyaudio.PyAudio()
# start Recording
stream = audio.open(format= FORMAT, channels= CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer= CHUNK)
print("recording...")
frames = []
# Recording Loop
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")
# Saving Data with Wave tool
waveFile = wave.open("file.wav", 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
# Stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
#Ploting
wave = wave.open('file.wav')
signal = wave.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")
# Ploting
fig = plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
time = np.linspace(0, RECORD_SECONDS, num = len(signal))
plt.plot(time, signal)
plt.show()