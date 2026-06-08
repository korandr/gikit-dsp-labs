import numpy as np
import matplotlib.pyplot as plt


base_y = [1, 1, 1, 1, 0, 0, 0, 0]

# Кратный сигнал
y_mult = np.tile(base_y, 4) 
N_mult = len(y_mult)
n_mult = np.arange(N_mult)
S_mult = np.fft.fft(y_mult)
A_mult = np.abs(S_mult)
F_mult = np.angle(S_mult)

# Плотная сетка частот для кратной огибающей
k_dense_mult = np.linspace(0, N_mult - 0.01, 1000)
# Аналитическое ДПФ (DTFT) через матричное умножение
S_dense_mult = np.sum(
    [
        y * np.exp(-1j * 2 * np.pi * k_dense_mult * n / N_mult)
        for n, y in enumerate(y_mult)
    ],
    axis = 0,
)
A_envelope_mult = np.abs(S_dense_mult)
F_envelope_mult = np.angle(S_dense_mult)

# Некратный сигнал
y_non_mult = np.concatenate([np.tile(base_y, 3), [1, 1, 1, 1]])
N_non_mult = len(y_non_mult)
n_non_mult = np.arange(N_non_mult)
S_non_mult = np.fft.fft(y_non_mult)
A_non_mult = np.abs(S_non_mult)
F_non_mult = np.angle(S_non_mult)

# Плотная сетка частот для некратной огибающей
k_dense_non_mult = np.linspace(0, N_non_mult - 0.01, 1000)
# Аналитическое ДПФ (DTFT) для некратного сигнала
S_dense_non_mult = np.sum(
    [
        y * np.exp(-1j * 2 * np.pi * k_dense_non_mult * n / N_non_mult)
        for n, y in enumerate(y_non_mult)
    ],
    axis = 0,
)
A_envelope_non_mult = np.abs(S_dense_non_mult)
F_envelope_non_mult = np.angle(S_dense_non_mult)

# Фильтрация фазового шума для дискретных отсчетов
F_mult_cleaned = np.where(A_mult < 1e-10, 0, F_mult)
F_non_mult_cleaned = np.where(A_non_mult < 1e-10, 0, F_non_mult)

# Фильтрация фазового шума для непрерывных огибающих
F_envelope_mult = np.where(A_envelope_mult < 1e-3, 0, F_envelope_mult)
F_envelope_non_mult = np.where(A_envelope_non_mult < 1e-3, 0, F_envelope_non_mult)


fig = plt.figure(figsize=(14, 9))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.stem(n_mult, A_mult, linefmt='b-', markerfmt='bo', basefmt='b-', label='Амплитудный спектр')
ax1.plot(k_dense_mult, A_envelope_mult, 'b--', linewidth=1.5, alpha=0.5, label='Огибающая')
ax1.set_title('Частотный спектр кратного сигнала (4 периода)', fontweight='bold')
ax1.set_xlabel('Номер спектрального отсчета (k)')
ax1.set_ylabel('Амплитуда спектра')
ax1.grid(True)
ax1.legend()

ax2.stem(n_non_mult, A_non_mult, linefmt='g-', markerfmt='go', basefmt='g-', label='Амплитудный спектр')
ax2.plot(k_dense_non_mult, A_envelope_non_mult, 'g--', linewidth=1.5, alpha=0.5, label='Огибающая')
ax2.set_title('Частотный спектр некратного сигнала (3.5 периода)', fontweight='bold')
ax2.set_xlabel('Номер спектрального отсчета (k)')
ax2.set_ylabel('Амплитуда спектра')
ax2.grid(True)
ax2.legend()

ax3.stem(n_mult, F_mult_cleaned, linefmt='b-', markerfmt='bo', basefmt='b-', label='Фазовый спектр')
ax3.plot(k_dense_mult, F_envelope_mult, 'b--', linewidth=1.5, alpha=0.5, label='Огибающая')
ax3.set_title('Фазовый спектр кратного сигнала', fontweight='bold')
ax3.set_xlabel('Номер спектрального отсчета (k)')
ax3.set_ylabel('Фаза спектра')
ax3.grid(True)
ax3.legend()

ax4.stem(n_non_mult, F_non_mult_cleaned, linefmt='g-', markerfmt='go', basefmt='g-', label='Фазовый спектр')
ax4.plot(k_dense_non_mult, F_envelope_non_mult, 'g--', linewidth=1.5, alpha=0.5, label='Огибающая')
ax4.set_title('Фазовый спектр некратного сигнала', fontweight='bold')
ax4.set_xlabel('Номер спектрального отсчета (k)')
ax4.set_ylabel('Фаза спектра')
ax4.grid(True)
ax4.legend()

plt.tight_layout()
plt.show()
