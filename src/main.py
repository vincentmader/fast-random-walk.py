#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import random

MPL_THEME = Path("..", "lib", "mpl-styles", "dark.mplstyle")
plt.style.use(MPL_THEME)


if __name__ == "__main__":

    BATCH_SIZE = 100
    positions = [np.array([0, 0]), np.array([0, 1])]

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal", adjustable="box")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    while True:

        positions = [positions[-2], positions[-1]]
        for _ in range(BATCH_SIZE):
            positions.append(positions[-1] + random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]]))

        x = [p[0] for p in positions[-BATCH_SIZE-1:]]
        y = [p[1] for p in positions[-BATCH_SIZE-1:]]

        plt.plot(x, y, "w")

        plt.pause(0.0000001)

plt.show()
