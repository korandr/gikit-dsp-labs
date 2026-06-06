import numpy as np
import matplotlib.pyplot as plt


base_y = [1, 1, 1, 1, 0, 0, 0, 0]

# Кратное число периодов
y_mult = np.tile(base_y, 4) 
n_mult = np.arange(len(y_mult))
S_mult = np.fft.fft(y_mult)
A_mult = np.abs(S_mult)
F_mult = np.angle(S_mult)

# Некратное число периодов
y_non_mult = np.concatenate([np.tile(base_y, 3), [1, 1, 1, 1]])
n_non_mult = np.arange(len(y_non_mult))
S_non_mult = np.fft.fft(y_non_mult)
A_non_mult = np.abs(S_non_mult)
F_non_mult = np.angle(S_non_mult)

fig5 = plt.figure(figsize=(14, 9))
ax1 = fig5.add_subplot(2, 2, 1)
ax2 = fig5.add_subplot(2, 2, 2)
ax3 = fig5.add_subplot(2, 2, 3)
ax4 = fig5.add_subplot(2, 2, 4)

ax1.stem(n_mult, A_mult, linefmt='b-', basefmt='r-')
ax1.set_title('Частотный спектр кратного сигнала (4 периода)', fontweight='bold')
ax1.set_xlabel('Номер спектрального отсчета (k)')
ax1.set_ylabel('Амплитуда спектра')
ax1.grid(True)

ax2.stem(n_non_mult, A_non_mult, linefmt='g-', basefmt='r-')
ax2.set_title('Частотный спектр некратного сигнала (3.5 периода)', fontweight='bold')
ax2.set_xlabel('Номер спектрального отсчета (k)')
ax2.set_ylabel('Амплитуда спектра')
ax2.grid(True)

ax3.stem(n_mult, F_mult, linefmt='m-', basefmt='r-')
ax3.set_title('Фазовый спектр кратного сигнала', fontweight='bold')
ax3.set_xlabel('Номер спектрального отсчета (k)')
ax3.set_ylabel('Фаза спектра')
ax3.grid(True)

ax4.stem(n_non_mult, F_non_mult, linefmt='m-', basefmt='r-')
ax4.set_title('Фазовый спектр некратного сигнала', fontweight='bold')
ax4.set_xlabel('Номер спектрального отсчета (k)')
ax4.set_ylabel('Фаза спектра')
ax4.grid(True)

plt.tight_layout()
plt.show()
