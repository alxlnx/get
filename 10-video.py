import spidev
import matplotlib.pyplot as plt

spi = spidev.SpiDev()         # Создать объект spi
spi.open(0, 0)                # Открыть нулевое ус-во spi с нулевым chip-select
spi.max_speed_hz = 1_600_000  # Задать частоту тактового сигнала

def getAdc():
  # may be xref2
  adcResponce = spi.xfer2([0, 0])  # Кол-во читаемых байт - длина списка-аргумента
  # Такие странные манипуляции надо производить из-за устройства АЦП. См. документацию.
  # adcResponce[0] - старший байт, маска 0x1F обнуляет три старших бита (0x1F = 0b11111)
  # Сдвиг на 8 даёт 5 старших бит и 8 нулей.
  # Теперь складываем с младшим байтом, из-за сдвига данные байтов не пропадают.
  # Сумму вправо на 1, чтобы выкинуть LSB.
  # Итого, имеем 12-битное число - результат оцифровки.
  return ( (adcResponce[0] & 0x1F) << 8 | adcResponce[1] ) >> 1

try:
  samples = []

  for i in range(20_000):
    samples.append(getAdc())

  plt.plt(samples)
  plt.show()
finally:
  spi.close()
