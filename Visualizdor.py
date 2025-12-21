import pydicom
import matplotlib.pyplot as plt

ds = pydicom.dcmread("arquivo.dcm")
plt.imshow(ds.pixel_array, cmap="gray")
plt.show()
