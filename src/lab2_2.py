import numpy as np
import matplotlib.pyplot as plt


n = np.arange(0, 8)
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])

S = np.fft.fft(y)
A = np.abs(S)
F = np.angle(S)

fig4 = plt.figure(figsize=(9, 8))
fig4.suptitle('Задание 2: Прямоугольный импульс', fontsize=12, fontweight='bold')
ax1 = fig4.add_subplot(3, 1, 1)
ax2 = fig4.add_subplot(3, 1, 2)
ax3 = fig4.add_subplot(3, 1, 3)

ax1.stem(n, y, linefmt='b-', basefmt='r-')
ax1.set_title('Исходный сигнал', fontweight='bold')
ax1.set_xlabel('Номер отсчета (n)')
ax1.set_ylabel('Амплитуда, В')
ax1.grid(True)

ax2.stem(n, A, linefmt='g-', basefmt='r-')
ax2.set_title('Амплитудный спектр', fontweight='bold')
ax2.set_xlabel('Номер спектрального отсчета (k)')
ax2.set_ylabel('Амплитуда спектра')
ax2.grid(True)

ax3.stem(n, F, linefmt='m-', basefmt='r-')
ax3.set_title('Фазовый спектр', fontweight='bold')
ax3.set_xlabel('Номер спектрального отсчета (k)')
ax3.set_ylabel('Фаза спектра')
ax3.grid(True)

plt.tight_layout()
plt.show()
