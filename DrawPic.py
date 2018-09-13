# define the size of x is 1*2
import numpy as np
import matplotlib.pyplot as plt

# dataset
x1 = np.array([3, 6, 1])
x2 = np.array([1, 5, -1])
x3 = np.array([3, 5, 1])
x4 = np.array([6, 5, 1])
x5 = np.array([2, 4, -1])
x6 = np.array([4, 4, 1])
x7 = np.array([6, 3, 1])
x8 = np.array([1, 2, -1])
x9 = np.array([2.6, 1.6, -1])
x10 = np.array([4, 2, 1])
x11 = np.array([2, 1, -1])
x12 = np.array([7, 1, 1])
Data = np.array(
    [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12])


if __name__ == '__main__':

    arr_forImg_x_R = []
    arr_forImg_y_R = []
    arr_forImg_x_B = []
    arr_forImg_y_B = []
    # Red
    for i in range(len(Data)):
        if Data[i][2] == -1:
            arr_forImg_x_R.append(Data[i][0])
    for i in range(len(Data)):
        if Data[i][2] == -1:
            arr_forImg_y_R.append(Data[i][1])

    x_R = np.array(arr_forImg_x_R)
    y_R = np.array(arr_forImg_y_R)
    # Blue
    for i in range(len(Data)):
        if Data[i][2] == 1:
            arr_forImg_x_B.append(Data[i][0])
    for i in range(len(Data)):
        if Data[i][2] == 1:
            arr_forImg_y_B.append(Data[i][1])

    x_B = np.array(arr_forImg_x_B)
    y_B = np.array(arr_forImg_y_B)

    x = np.arange(2.65, 2.9, 0.1)
    y = 64 * x - 170

    plt.figure('Divide')
    ax = plt.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # s "the size of point"
    # alpha "transparency"
    ax.scatter(arr_forImg_x_R, arr_forImg_y_R, c='r', s=20, alpha=1)
    ax.scatter(arr_forImg_x_B, arr_forImg_y_B, c='b', s=20, alpha=1)
    ax.plot(x, y)
    # plt.grid(True, linestyle="-.", color="r", linewidth="3")
    plt.show()
