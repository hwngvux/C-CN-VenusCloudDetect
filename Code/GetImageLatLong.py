import rasterio
import numpy as np
from affine import Affine
from pyproj import Proj, transform

def read_latlon(fname):
# Read raster
    with rasterio.open(fname) as r:
        T0 = r.transform  # upper-left pixel corner affine transform
        p1 = Proj(r.crs)
        A = r.read()  # pixel values

# All rows and columns
    cols, rows = np.meshgrid(np.arange(A.shape[2]), np.arange(A.shape[1]))

# Get affine transform for pixel centres
    T1 = T0 * Affine.translation(0.5, 0.5)
# Function to convert pixel row/column index (from 0) to easting/northing at centre
    rc2en = lambda r, c: (c, r) * T1

# All eastings and northings (there is probably a faster way to do this)
    eastings, northings = np.vectorize(rc2en, otypes=[np.float, np.float])(rows, cols)

# Project all longitudes, latitudes
    p2 = Proj(proj='latlong',datum='WGS84')
    longs, lats = transform(p1, p2, eastings, northings)
    np.savetxt("/Users/hungvu/Desktop/Python/untitled folder/long.txt",longs)
    np.savetxt("/Users/hungvu/Desktop/Python/untitled folder/lat.txt",lats)
    
    return 

fname = "/Users/hungvu/Downloads/VENUS_20190218-033948-000_L1C_VN-HANOI_D_V2-0/VE_VM01_VSC_L1VALD_VN_HANOI_20190218.DBL.DIR/VE_VM01_VSC_PDTIMG_L1VALD_VN_HANOI_20190218.DBL.TIF"
read_latlon(fname)
