from osgeo import gdal
import sys
import numpy as np

#Open Tif file
gtif = gdal.Open( "/Users/hungvu/Downloads/VENUS_20190218-033948-000_L1C_VN-HANOI_D_V2-0/VE_VM01_VSC_L1VALD_VN_HANOI_20190218.DBL.DIR/VE_VM01_VSC_PDTIMG_L1VALD_VN_HANOI_20190218.DBL.TIF" )

#Get metadata and count image raster(bands)
print (gtif.GetMetadata())
print (gtif.RasterCount)
type(gtif)

#Read raster Dataset into array from Band 15
rasterArray = gtif.ReadAsArray()

band = gtif.GetRasterBand(15)

data = band.ReadAsArray()

print(data)

sh = data.shape
print(sh)

#Save dataset array into txt file
np.savetxt("/Users/hungvu/Desktop/Python/untitled folder/band15.txt",data)
