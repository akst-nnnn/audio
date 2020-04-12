import numpy
import soundfile
from matplotlib import pyplot
from scipy import fftpack

data,rate = soundfile.read("audio3.wav")


n = len(data)
x = numpy.linspace(0, n/rate, n)
y = data
pyplot.xlabel("time(secound)")
pyplot.ylabel("amplitude")
pyplot.plot(x, y)

a = fftpack.fftfreq(n, 1/rate)
b = numpy.abs(fftpack.fft(y))
pyplot.figure("fft")
pyplot.xlabel("frequency(Hz)")
pyplot.ylabel("intensity")
pyplot.plot(a, b)

pyplot.show()