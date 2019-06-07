from osgeo import gdal
import sys
import numpy as np  
import osgeo.osr as osr

#Get dataset, lat, long into array
array = np.loadtxt(fname = "/Users/hungvu/Desktop/Python/untitled folder/band15_1.txt")
print(array)
lat = np.loadtxt(fname = "/Users/hungvu/Desktop/Python/untitled folder/lat.txt")
print(lat)
lon = np.loadtxt(fname = "/Users/hungvu/Desktop/Python/untitled folder/long.txt")
print(lon)

xmin,ymin,xmax,ymax = [lon.min(),lat.min(),lon.max(),lat.max()]
nrows,ncols = np.shape(array)
xres = (xmax-xmin)/float(ncols)
yres = (ymax-ymin)/float(nrows)
geotransform=(xmin,xres,0,ymax,0, -yres)


output_raster = gdal.GetDriverByName('GTiff').Create('/Users/hungvu/Desktop/Python/Band15_Cloud.tif',ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
output_raster.SetGeoTransform(geotransform)
srs = osr.SpatialReference()                 # Establish its coordinate encoding
srs.ImportFromEPSG(4326)

output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
                                                   # to the file
output_raster.GetRasterBand(1).WriteArray(array)   # Writes my array to the raster

output_raster.FlushCache()
