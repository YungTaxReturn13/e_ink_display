import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image
from inky.auto import auto

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

# Save figure
plt.savefig("graph.png")

inky = auto(ask_user=True, verbose=True)
saturation = 0.9

if len(sys.argv) == 1:
    print(
        """
Usage: {file} image-file
""".format(
            file=sys.argv[0]
        )
    )
    sys.exit(1)

image = Image.open("graph.png")
resizedimage = image.resize(inky.resolution)

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

inky.set_image(resizedimage, saturation=saturation)
inky.show()
