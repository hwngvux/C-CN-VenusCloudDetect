import rasterio
from rasterio.enums import Resampling
from osgeo import gdal
import sys
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

tif1 = gdal.Open( "/Users/hungvu/Desktop/Python/Band15_Cloud_4.tif" )
tif2 = gdal.Open("/Users/hungvu/Downloads/VENUS_20190218-033948-000_L2A_VN-HANOI_D_V2-0/VE_VM01_VSC_L2VALD_VN_HANOI_20190218.DBL.DIR/VE_VM01_VSC_PDTANX_L2VALD_VN_HANOI_20190218_CLD.DBL.TIF")

print (tif1.RasterCount)
print (tif1.RasterCount)
type(tif1)
type(tif2)
rasterArray1 = tif1.ReadAsArray()
band1 = tif1.GetRasterBand(1)
data1 = band1.ReadAsArray()
print(data1)

imgplot1 = plt.imshow(data1)
plt.show()

rasterArray2 = tif2.ReadAsArray()
band2 = tif2.GetRasterBand(1)
data2 = band2.ReadAsArray()

print(data2)
imgplot2 = plt.imshow(data2)
plt.show()

cols = tif1.RasterXSize
rows = tif1.RasterYSize

geotransform = tif1.GetGeoTransform()

print(cols,rows,geotransform)


for i in range(rows-1):
    for j in range(cols-1):
        if(data1[i][j] == 1):
            data2[i][j] = 1
            
imgplot2 = plt.imshow(data2)
plt.show()
