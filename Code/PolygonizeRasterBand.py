from osgeo import gdal, ogr
import sys

gdal.UseExceptions()

src_ds = gdal.Open( "/Users/hungvu/Desktop/Python/Band5tif" )
if src_ds is None:
    print ('Unable to open %s' % src_filename)
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(1)
except RuntimeError as e:
    print ('Band ( %i ) not found' % band_num)
    print (e)
    sys.exit(1)


dst_layername = "POLYGONIZED_STUFF"
drv = ogr.GetDriverByName("ESRI Shapefile")
dst_ds = drv.CreateDataSource( dst_layername + ".shp" )
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )

gdal.Polygonize( srcband, None, dst_layer, -1, [], callback=None )
