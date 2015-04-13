import numpy
from matplotlib import pyplot
from matplotlib import gridspec

def data(num=50):
    x = numpy.linspace(0, 10, num)
    y = numpy.sin(x)
    return x, y

def plot_and_save():
    x, y = data()

    pyplot.figure(figsize=(6,6))
    pyplot.plot(x, y, marker="o")
    # pyplot.show()
    pyplot.savefig("myplot1.pdf")

def plot_many_points():
    x, y = data(100000)

    pyplot.figure(figsize=(6,6))
    pyplot.plot(x, y, marker="o") #, rasterized=True)
    pyplot.savefig("myplot2.pdf", dpi=300)

    pyplot.figure(figsize=(6,6))
    pyplot.plot(x, y, marker="o", rasterized=True)
    pyplot.savefig("myplot2b.pdf", dpi=300)

def simple_subplots():
    x, y = data()
    pyplot.figure(figsize=(6,10))
    pyplot.subplot(211)
    pyplot.plot(x, y)
    pyplot.subplot(212)
    pyplot.plot(y, x)
    pyplot.savefig("myplot3.pdf")

def adjust_subplots():
    x, y = data()
    pyplot.figure(figsize=(6,10))
    pyplot.subplot(211)
    pyplot.plot(x, y)
    pyplot.subplot(212)
    pyplot.plot(y, x)
    pyplot.subplots_adjust(hspace=0)
    pyplot.savefig("myplot4.pdf")

def advanced_subplots():
    x, y = data()

    gs = gridspec.GridSpec(2, 2)
    pyplot.subplot(gs[0,0])
    pyplot.plot(y, x)

    pyplot.subplot(gs[0,1])
    pyplot.plot(-y, x)

    pyplot.subplot(gs[1,:])
    pyplot.plot(x, y)
    pyplot.axis('equal')

    pyplot.savefig("myplot5.pdf")

if __name__ == "__main__":
    plot_and_save()
    plot_many_points()
    simple_subplots()
    adjust_subplots()
    advanced_subplots()
