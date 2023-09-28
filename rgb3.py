import rasterio 
import numpy as np
from rasterio import plot
from rasterio.plot import show
from skimage import exposure

band2=rasterio.open("B02_10m.jp2")
band3=rasterio.open("B03_10m.jp2")
band4=rasterio.open("B04_10m.jp2")

band2_geo=band2.profile
band2_geo.update({"count":3})

with rasterio.open('rgb.tiff','w',**band2_geo) as dest:
    dest.write(band2(1),1)
    dest.write(band3(1),2)
    dest.write(band3(1),3)

img=rasterio.open("rgb.tiff")
image=np.array([img.read(3),img.read(2),img.read(1)]).transpose(1,2,0)
p2,p98=np.percentile(image,(2,98))
image=exposure.rescale.intensity(image,in_range=(p2,p98))/100000

show(image.transpose(2,0,1),transform=img.transform)


