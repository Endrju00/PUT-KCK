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
    a = plot_data('data/cel.csv')

    plt.plot(a['x'], a['y'])
    plt.show()


if __name__ == '__main__':
    main()
