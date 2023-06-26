#!/bin/bash

# calculate ndvi from B04 (RED) and B08 (NIR)

calculate_ndvi()
{
# calculate
g.region raster=band_4 -p
i.vi red=band_4 nir=band_8 viname=ndvi output=NDWI --overwrite

echo "---------------- DONE ------------------"
}

calculate_ndvi