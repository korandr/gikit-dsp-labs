import numpy as np
import matplotlib.pyplot as plt


N = 8 # Количество отсчетов
M = 4 # Количество отсчётов с единичной амплитудой
n = np.arange(0, N)
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])

S = np.fft.fft(y)
A = np.abs(S)
F = np.angle(S)

k_dense = np.linspace(0, N - 0.01, 1000) # Расширенный диапазон k для огибающих

with np.errstate(divide='ignore', invalid='ignore'):
    A_dirichlet = np.where(
        k_dense == 0,
        M,
        np.abs(np.sin(np.pi * M * k_dense / N) / np.sin(np.pi * k_dense / N))
    )
A_sinc = np.abs(M * np.sinc(M * k_dense / N))

F_linear = -np.pi / N * k_dense * (M - 1)
with np.errstate(divide='ignore', invalid='ignore'):
    # Значение частного двух синусов (ф. Дирихле)
    fraction_value = np.where(
        k_dense == 0,
        1,
        np.sin(np.pi * M * k_dense / N) / np.sin(np.pi * k_dense / N)
    )

# Сдвиг на π при отрицательном значении частного
F_envelope = F_linear + np.where(fraction_value < 0, np.pi, 0)
# Удержание фазы в пределих (-π, π]
F_envelope = (F_envelope + np.pi) % (2 * np.pi) - np.pi

fig4 = plt.figure(figsize=(9, 10))
fig4.suptitle('Задание 2: Прямоугольный импульс', fontsize=12, fontweight='bold')
ax1 = fig4.add_subplot(3, 1, 1)
ax2 = fig4.add_subplot(3, 1, 2)
ax3 = fig4.add_subplot(3, 1, 3)

ax1.stem(n, y, linefmt='b-', basefmt='b-')
ax1.set_title('Исходный сигнал', fontweight='bold')
ax1.set_xlabel('Номер отсчета (n)')
ax1.set_ylabel('Амплитуда, В')
ax1.grid(True)

ax2.stem(n, A, linefmt='g-', basefmt='g-', label='Амплитудный спектр')
ax2.plot(k_dense, A_dirichlet, 'b--', linewidth=1.5, alpha=0.5, label='Огибающая')
ax2.plot(k_dense, A_sinc, 'r--', linewidth=1, alpha=0.5, label='Аппроксимация sinc')
ax2.set_title('Амплитудный спектр', fontweight='bold')
ax2.set_xlabel('Номер спектрального отсчета (k)')
ax2.set_ylabel('Амплитуда спектра')
ax2.legend(loc='upper right')
ax2.grid(True)

ax3.stem(n, F, linefmt='m-', basefmt='m-', label='Фазовый спектр')
ax3.plot(k_dense, F_envelope, 'm--', linewidth=1, alpha=0.5, label='Огибающая')
ax3.set_title('Фазовый спектр', fontweight='bold')
ax3.set_xlabel('Номер спектрального отсчета (k)')
ax3.set_ylabel('Фаза спектра')
ax3.legend(loc='upper right')
ax3.grid(True)

plt.tight_layout()
plt.show()
