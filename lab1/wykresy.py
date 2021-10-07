import os
import csv
import matplotlib.pyplot as plt

MARKERS = ['o', 's', '^', 'p', 'P']
COLORS = ['b', 'g', 'r', 'k', 'm']


def plot_data(path):
    '''Takes in path to the csv file, returns the dictionary with x and y axises data.'''

    with open(path) as csv_file:
        data = {
            'x': [],
            'y': []
        }

        reader = csv.reader(csv_file)
        counter = 0
        for row in reader:
            counter += 1

            if counter == 1:
                continue

            data['x'].append(int(row[1])/1000)
            runs = list(map(float, row[2:]))
            data['y'].append(round(sum(runs)/32, 4) * 100)

    return data


def main():
    path = input("Proszę podać ścieżkę do folderu z plikami csv: ")

    filepaths = []
    filenames = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            filepaths.append(os.path.join(path, file))
            filenames.append(file[:-4])

    f, ax = plt.subplots(1)

    i = 0
    for path in filepaths:
        data = plot_data(path)
        ax.plot(data['x'], data['y'],
                f'{COLORS[i]}{MARKERS[i]}', ls='-', ms=6.5, markevery=25)
        ax.legend(filenames)
        i += 1

    ax.set_xlim(xmin=0, xmax=500)
    plt.xlabel("Rozegranych gier (x1000)")
    plt.ylabel("Odsetek wygranych gier [%]")
    plt.savefig('myplot.pdf')
    plt.close()


if __name__ == '__main__':
    main()
