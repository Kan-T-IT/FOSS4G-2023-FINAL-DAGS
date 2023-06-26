#!/bin/bash

# mask raster

calculate_mask()
{
g.region vector=highways_buffer
r.mask vector=highways_buffer
r.out.png input=NDVI output=/grassdb/output/prueb_ndvi -w --overwrite
r.mask -r
echo "---------------- DONE ------------------"
}

calculate_mask