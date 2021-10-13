import os
import csv

import matplotlib.pyplot as plt
import numpy as np

MARKERS = ['o', 's', '^', 'p', 'P']  # Markery dla 5 róznych zestawów danych
COLORS = ['b', 'g', 'r', 'k', 'm']  # Kolory dla 5 róznych zestawów danych
PATH_TO_CSV = "data"  # Ścieżka do folderu z plikami csv
NAMES = {  # Nazwy algorytmów związane z nazwami plików
    'rsel': '1-Evol-RS',
    'cel-rs': '1-Coev-RS',
    '2cel-rs': '2-Coev-RS',
    'cel': '1-Coev',
    '2cel': '2-Coev'
}


def get_data(path):
    '''Takes in path to the csv file, returns the dictionary with x and y axises data.'''

    with open(path) as csv_file:
        data = {
            'x': [],
            'y': [],
            'last': [],
        }

        reader = csv.reader(csv_file)
        counter = 0
        for row in reader:
            counter += 1

            if counter == 1:
                continue

            data['x'].append(int(row[1])/1000)
            runs = list(map(lambda x: float(x) * 100, row[2:]))
            data['y'].append(sum(runs)/32)

            if counter == 201:
                data['last'] = runs

    return data


def pokolenie(x):
    return 0.4 * x


def gry(x):
    return x


def main():
    # Zebranie danych z plików z rozszerzeniem .csv
    filepaths = []
    filenames = []
    for file in os.listdir(PATH_TO_CSV):
        if file.endswith(".csv"):
            filepaths.append(os.path.join(PATH_TO_CSV, file))
            filenames.append(file[:-4])

    # Rysowanie wykresów
    ax1 = plt.subplot(1, 2, 1)
    plt.xlabel("Rozegranych gier (x1000)", fontsize=11)
    plt.ylabel("Odsetek wygranych gier [%]", fontsize=11)

    ax2 = plt.subplot(1, 2, 2)
    ax2_data = {}

    i = 0
    for path in filepaths:
        data = get_data(path)
        ax1.plot(data['x'], data['y'],
                f'{COLORS[i]}{MARKERS[i]}', ls='-', ms=6.5, markevery=25, markeredgecolor='black')
        ax1.legend([NAMES.get(filename, filename) for filename in filenames])
        ax2_data[filenames[i]] = data['last'] 
        i += 1

    
    ax1.set_xlim(xmin=0, xmax=500)
    ax1.grid(color='lightblue', linestyle='dotted')
    secax = ax1.secondary_xaxis('top', functions=(pokolenie, gry))
    secax.set_ticks(np.arange(0, 201, 40))
    secax.set_xlabel('Pokolenie', fontsize=11)

    ax2.boxplot(
            [ax2_data[filename] for filename in filenames],
            labels=[NAMES.get(filename, filename) for filename in filenames],
            notch=True,
            showmeans=True,
            boxprops=dict(color="blue"),
            flierprops = dict(marker='+', markeredgecolor='blue', markersize=6),
            medianprops = dict(color='red'),
            meanprops = dict(marker='o', markeredgecolor='black',
                      markerfacecolor='blue', markersize=4),
            whiskerprops = dict(linestyle='dashed', color='blue')
    )

    ax2.set_ylim(ymin=60, ymax=100)
    ax2.yaxis.tick_right()
    plt.xticks(rotation=25)
    ax2.grid(color='lightblue', linestyle='dotted')

    plt.tight_layout()
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
