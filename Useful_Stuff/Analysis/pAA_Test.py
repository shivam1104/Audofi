#import pyAudioAnalysis
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt

path

from pydub import AudioSegment
sound = AudioSegment.from_mp3("../1.mp3")
sound = sound.set_channels(1)
sound.export("../1.mp3", format="mp3")


[Fs, x] = audioBasicIO.readAudioFile("../1.mp3");
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR'); 
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()