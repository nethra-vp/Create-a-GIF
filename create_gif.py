import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png','nyan-cat3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('nyan-cat.gif',images, duration = 500, loop = 0)
# duration = 500: How long each picture should show in the GIF, in milliseconds.
# loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).