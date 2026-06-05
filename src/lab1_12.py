import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


T = 100 # Период сигнала, мс
A = 10  # Амплитуда, В
Td_variants = (2, 10, 49) # Периоды дискретизации, мс

def plot_signal(Td: float, ax1: Axes, ax2: Axes) -> None:
    n = np.arange(0, 100, Td)
    y = A * np.sin(2 * np.pi * n / T)

    ax1.plot(n, y, color='blue')
    ax1.set_title(f'Непрерывный сигнал (Td = {Td} мс)')
    ax1.set_xlabel('Время, мс')
    ax1.set_ylabel('Амплитуда, В')
    ax1.set_xlim(0, T)
    ax1.set_ylim(-A - 1, A + 1)
    ax1.grid(True)

    ax2.stem(n, y)
    ax2.set_title(f'Дискретизированный сигнал (Td = {Td} мс)')
    ax2.set_xlabel('Время, мс')
    ax2.set_ylabel('Амплитуда, В')
    ax2.set_xlim(0, T)
    ax2.set_ylim(-A - 1, A + 1)
    ax2.grid(True)

if __name__ == '__main__':
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    for i, Td in enumerate(Td_variants):
            plot_signal(Td, axes[i, 0], axes[i, 1])

    plt.tight_layout()
    plt.show()
