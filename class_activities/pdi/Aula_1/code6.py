import matplotlib.pyplot as plt
from pdi_utils import load_lena

# Import the try all function
from skimage.filters  import try_all_threshold

# Import the rgb to gray convertor function
from skimage.___ import ___

lena = load_lena()

# Turn the Lena image to grayscale
grayscale = ___

# Use the try all method on the resulting grayscale image
fig, ax = ___(___, verbose=False)

# Show the resulting plots
plt.show()