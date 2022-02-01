import sys
from scipy.io import wavfile


def regognizeGender(data):
    return 'K'


if __name__ == '__main__':
    filename = sys.argv[1]
    try:
        samplerate, data = wavfile.read(filename)
    except WavFileWarning:
        print("SSSSSS")
    result = regognizeGender(data)
    print(result)