import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def num_of_neighbours(row, col, M):
    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life_sum += M[((row + i) % len(M))][((col + j) % len(M[0]))]
    return life_sum


def iterate_numpy(M):
    shape = len(M), len(M[0])
    K = [[0, ] * (shape[1]) for i in range(shape[0])]
    for row in range(shape[0]):
        for col in range(shape[1]):
            neighbors = num_of_neighbours(row, col, M)
            if neighbors < 2 or neighbors > 3:
                K[row][col] = 0
            elif neighbors == 3 and M[row][col] == 0:
                K[row][col] = 1
            else:
                K[row][col] = M[row][col]
    return K


reward = 0

def gen(k):
    global reward
    i = 0
    while reward <= k:
        i += 1
        yield i



def animate(i):
    global reward
    reward =reward + 1
    global M
    Z = M.copy()

    Z = iterate_numpy(M)
    mat.set_data(Z)
    M = Z

    return [mat]




if __name__ == '__main__':
    m, n = 10, 10
    M = np.random.randint(2, size=(m, n))

    print('Введите количество шагов:')
    k = int(input())
    print(M)
    fig, ax = plt.subplots()
    mat = ax.matshow(M)
    ani = animation.FuncAnimation(fig, animate, frames=gen(k), repeat=False)
    plt.show()