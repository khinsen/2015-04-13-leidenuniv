import numpy
from matplotlib import pyplot, animation
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
    y += numpy.random.normal(size=y.size)

    pyplot.figure(figsize=(6,6))
    pyplot.plot(x, y, marker="o")
    pyplot.savefig("myplot2.pdf")

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

def movie():
    x, y = data(200)

    fig = pyplot.figure(figsize=(6,6))
    pyplot.plot(x, y)
    artists = []
    for xi, yi in zip(x, y):
        points = pyplot.scatter(xi, yi, marker='o')
        artists.append([points])
    movie = animation.ArtistAnimation(fig, artists, interval=50,
                                      repeat_delay=3000, blit=True)
    writer = animation.writers['ffmpeg'](fps=15, metadata=dict(artist='Me'), bitrate=1800)
    movie.save("mymovie.avi", writer=writer, dpi=300)

if __name__ == "__main__":
    # plot_and_save()
    # plot_many_points()
    # simple_subplots()
    # adjust_subplots()
    # advanced_subplots()
    # movie()
