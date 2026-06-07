import numpy as np
import matplotlib.pyplot as plt


N = 128                    # Количество отсчётов
n = np.arange(0, N)        # Массив отсчётов
T1 = 4                     # Период ВЧ синусоиды, отсчётов
T2 = 32                    # Период НЧ синусоиды, отсчётов
A1 = 0.5                   # Амплитуда ВЧ синусоиды, В
A2 = 10                    # Амплитуда НЧ синусоиды, В
A0 = 5                     # Амплитуда постоянной составляющей, В


def build_plots(constant_component: bool) -> None:
    y = A1 * np.sin(2 * np.pi * n / T1) + A2 * np.sin(2 * np.pi * n / T2) # Исходный сигнал

    if constant_component:
        y += A0

    S = np.fft.fft(y)      # ДПФ
    A = np.abs(S)          # Амплитудный спектр
    A_norm = A / (N / 2)   # Нормированный амплитудный спектр
    A_norm[0] = A[0] / N
    F = np.angle(S)        # Фазовый спектр
    F_cleaned = np.where(A > 1e-10, F, 0) # Очищенный фазовый спектр

    fig1 = plt.figure(figsize=(9, 3.5))
    plt.stem(n, y, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.title('Исходный сигнал y[n]', fontsize=11, fontweight='bold')
    plt.xlabel('Номер отсчета (n)')
    plt.ylabel('Амплитуда, В')
    plt.grid(True)
    fig1.tight_layout()

    fig2 = plt.figure(figsize=(9, 7))
    ax1 = fig2.add_subplot(2, 1, 1)
    ax1.stem(n, A, linefmt='g-', markerfmt='go', basefmt='r-')
    ax1.set_title('Амплитудный спектр', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Номер спектрального отсчета (k)')
    ax1.set_ylabel('Амплитуда спектра')
    ax1.grid(True)

    ax2 = fig2.add_subplot(2, 1, 2)
    ax2.stem(n, A_norm, linefmt='g-', markerfmt='go', basefmt='r-')
    ax2.set_title('Нормированный амплитудный спектр', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Номер спектрального отсчета (k)')
    ax2.set_ylabel('Амплитуда, В')
    ax2.grid(True)

    fig2.tight_layout()

    fig3 = plt.figure(figsize=(9, 7))
    ax1 = fig3.add_subplot(2, 1, 1)
    ax1.stem(n, F, linefmt='m-', markerfmt='mo', basefmt='r-')
    ax1.set_title('Фазовый спектр', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Номер спектрального отсчета (k)')
    ax1.set_ylabel('Фаза, рад')
    ax1.grid(True)

    ax2 = fig3.add_subplot(2, 1, 2)
    ax2.stem(n, F_cleaned, linefmt='m-', markerfmt='mo', basefmt='r-')
    ax2.set_title('Очищенный фазовый спектр', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Номер спектрального отсчета (k)')
    ax2.set_ylabel('Фаза, рад')
    ax2.grid(True)

    fig3.tight_layout()

if __name__ == '__main__':
    build_plots(constant_component=False)
    plt.show()
    build_plots(constant_component=True)
    plt.show()
