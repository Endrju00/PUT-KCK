import os
import csv
import matplotlib.pyplot as plt


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
            
            data['x'].append(int(row[1]))
            runs = list(map(float, row[2:]))
            data['y'].append(round(sum(runs)/32, 4))
    
    return data

def main():
    path = input("Proszę podać ścieżkę do folderu z plikami csv: ")

    file_paths = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            file_paths.append(os.path.join(path, file))

    f, ax = plt.subplots(1)

    for path in file_paths:
        data = plot_data(path)
        ax.plot(data['x'], data['y'])
        ax.legend(file_paths)

    ax.set_xlim(xmin=0, xmax=500000)
    plt.xlabel("Rozegranych gier")
    plt.ylabel("Odsetek wygranych gier")
    plt.show()


if __name__ == '__main__':
    main()
