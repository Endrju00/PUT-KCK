import matplotlib.pyplot as plt


def main():
    plt.figure(figsize=(3, 3))
    plt.plot([100, 200, 300, 400], [0.1, 0.2, 0.8, 0.9])
    # plt.savefig('myplot.pdf')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
