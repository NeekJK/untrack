__author__ = "Nick Calvin"
__copyright__ = "Copyright 2025, The Untrack Project"
__credits__ = ["Nick Calvin"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Nick Calvin"
__email__ = "nicholasjuan19@yahoo.com"

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logger as ll
import librosa
import numpy as np
import matplotlib
matplotlib.interactive(False)
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import scipy


def audio_load(audio):
    logger.info(f"Loading audio file {audio}")
    y, sr = librosa.load(audio)
    tempo = librosa.beat.tempo(y=y, sr=sr)
    duration = librosa.get_duration(y=y, sr=sr)
    logger.info(f"{audio} loaded! \n BPM: {int(tempo[0])}\n Duration: {int(duration)}s ")
    return y, sr

def audio_sync(audio1, audio2):
    y1, sr1 = audio_load(audio1) # Short clip
    y2, sr2 = audio_load(audio2) # Full audio
    logger.info("Cross-correlating both audios ..")

    # Zero-padding
    y1_padded = np.pad(y1, (0, len(y2) - len(y1)), 'constant') 

    # Correlating
    correlation  = scipy.signal.correlate(y1_padded, y2, mode='full')

    # Lag
    lag = np.argmax(correlation) - (len(y1_padded) - 1) 

    # Time offset
    time_offset = lag / sr1
    
    # Time shifting
    y1_shifted = np.roll(y1, lag)




    # peak_index = np.argmax(corr)
    # peak_lag = lags[peak_index]

    # if peak_lag > 0:
    # # Delay y2 by peak_lag samples
    #     y2_aligned = np.concatenate((np.zeros(peak_lag), y2_norm))[:len(y1_norm)]   
    # else:
    # # Advance y2 by -peak_lag samples
    #     y2_aligned = y2_norm[-peak_lag:]

    plt.figure(figsize=(10, 6))
    plt.plot(y1_shifted, label='y1_shifted')
    plt.plot(y2, label='y2')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Aligned Signals')
    plt.show()
    plt.savefig('my_plot.png')
    # print(corr)


    
if __name__=='__main__':
    logger = ll.get_logger(__name__)
    logger.info(f"Librosa: {librosa.__version__}")
    audio1 = 'examples/audio1.mp3'
    audio2 = 'examples/audio2.mp3'
    
    # audio_load('examples/audio1.mp3')
    audio_sync(audio1, audio2)
    # test()
