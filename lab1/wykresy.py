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
    path = input("Please pass the path to folder with csv files: ")

    file_paths = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            file_paths.append(os.path.join(path, file))

    for path in file_paths:
        data = plot_data(path)
        plt.plot(data['x'], data['y'])
        plt.legend(file_paths)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
