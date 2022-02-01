import glob
from scipy.io import wavfile
from pylab import *
from scipy import *

human_voice_min_max = [80,255]
male_min_max = [55,160]
female_min_max = [170,275]
HPSLoop = 6

def HPS(rate, data_voice):
    T = 3  # time for HPS method

    if (T > len(data_voice) / rate) : T = len(data_voice) / rate
    data_voice = data_voice[max(0, int(len(data_voice) / 2) - int(T / 2 * rate)) : min(len(data_voice) - 1, int(len(data_voice) / 2) + int(T / 2 * rate))]
    part_len = int(rate)
    parts = [data_voice[i * part_len : (i + 1) * part_len] for i in range(int(T))]
    result_parts = []
    for data in parts:
        if (len(data) == 0): continue
        window = np.hamming(len(data))
        data = data * window
        fftV = abs(fft(data)) / rate
        fftR = copy(fftV)
        for i in range(2, HPSLoop):
            tab = copy(fftV[::i])
            fftR = fftR[:len(tab)]
            fftR *= tab
        result_parts.append(fftR)
    result = [0] * len(result_parts[int(len(result_parts) / 2)])
    for res in result_parts:
        if (len(res)!=len(result)): continue
        result += res

    if (sum(result[male_min_max[0] : male_min_max[1]]) > sum(result[female_min_max[0] : female_min_max[1]])):
      return 1
    return 0

if __name__ == "__main__":
    # male: 1 female: 0
    M = [[0,0],[0,0]]
    files = glob.glob("samples/*.wav")
    for f in files:
        rate, array = wavfile.read(f)
        correct = int(f.replace("/", "_").replace(".", "_").split("_")[2] == "M")
        found = HPS(rate, array)
        M[correct][found] += 1
    print(M)
    correctness = (M[0][0] + M[1][1]) / (sum(M[0]) + sum(M[1]))
    print(correctness)
