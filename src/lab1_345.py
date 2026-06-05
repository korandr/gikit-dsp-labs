import numpy as np
import matplotlib.pyplot as plt


T = 127 # Период сигнала, отсчётов
A = 10  # Амплитуда, В
n = np.arange(0, 127)
y = A * np.sin(2 * np.pi * n / T)

N = 8 # Количество уровней квантования
d = A / (N - 1) # Шаг квантования
yd = y / d # Значение сигнала, делённое на шаг квантования

Yrd = np.round(yd)
Ycl = np.ceil(yd)
Yfx = np.trunc(yd)
Yfr = np.floor(yd)

ERRrd = yd - Yrd
ERRcl = yd - Ycl
ERRfx = yd - Yfx
ERRfr = yd - Yfr

methods = [
    ('round', Yrd, ERRrd, 'red'),
    ('ceil', Ycl, ERRcl, 'blue'), 
    ('trunc', Yfx, ERRfx, 'green'),
    ('floor', Yfr, ERRfr, 'cyan'),
]

def plot_quantized_signals() -> None:
    fig = plt.figure(figsize=(10, 4.5))
    ax = fig.add_subplot(1, 1, 1)

    for name, Y, _, color in methods:
        ax.step(n, Y, color=color, label=name, where='mid', alpha=0.8)

    ax.set_title('Сигналы, квантованные разными методами', fontsize=11, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True)
    fig.tight_layout()


def plot_quantization_error_histograms() -> None:
    fig, axs = plt.subplots(2, 2, figsize=(10, 7))
    axs_flat = axs.ravel()
    bins = np.arange(-1, 1.05, 0.05)

    for i, (name, _, err, color) in enumerate(methods):
        axs_flat[i].hist(err, bins=bins, color=color, edgecolor='black', alpha=0.7)
        axs_flat[i].set_title(f'Гистограмма ошибки ({name})', fontsize=10)
        axs_flat[i].grid(True)

    fig.tight_layout()


def plot_quantization_error_table() -> None:
    fig = plt.figure(figsize=(8, 2.5))
    ax_table = fig.add_subplot(1, 1, 1)
    ax_table.axis('off')

    columns = ['Метод', 'Среднее', 'Станд. откл.', 'Мин', 'Макс']
    table_data = []
    for name, _, err, _ in methods:
        table_data.append([
            name,
            f'{np.mean(err):.4f}',
            f'{np.std(err, ddof=1):.4f}',
            f'{np.min(err):.4f}',
            f'{np.max(err):.4f}'
        ])

    report_table = ax_table.table(
        cellText = table_data, 
        colLabels = columns, 
        loc = 'center', 
        cellLoc = 'center',
    )

    report_table.auto_set_font_size(False)
    report_table.set_fontsize(11)
    report_table.scale(1, 1.8)

    fig.tight_layout()

def print_binary_codes_table() -> None:
    print('\n' + '='*65)
    print('ЗАДАНИЕ 5: ТАБЛИЦА ДВОИЧНОГО КОДИРОВАНИЯ СИГНАЛА (метод round)')
    print('='*65)
    print(f'{'№ отсчета':<10} | {'Квант. значение':<16} | {'Прямой код':<12} | {'Доп. код':<12}')
    print('-'*65)

    for i in range(50):
        q_val = int(Yrd[i])
        direct, twos = _to_binary_codes(q_val, bits=4)
        print(f'{i:<10} | {q_val:<16} | {direct:<12} | {twos:<12}')

    print('='*65)

def _to_binary_codes(value: int, bits: int = 4) -> tuple[str, str]:
    """Преобразовать целое число в прямой и дополнительный двоичные коды."""

    # Прямой код (Sign-Magnitude)
    if value >= 0:
        direct_code = f'0{bin(value)[2:].zfill(bits-1)}'
    else:
        direct_code = f'1{bin(abs(value))[2:].zfill(bits-1)}'
        
    # Дополнительный код (Two's Complement)
    if value >= 0:
        twos_code = direct_code
    else:
        twos_code = bin((1 << bits) + value)[2:]
        
    return direct_code, twos_code


if __name__ == '__main__':
    plot_quantized_signals()
    plot_quantization_error_histograms()
    plot_quantization_error_table()
    print_binary_codes_table()
    plt.show()
