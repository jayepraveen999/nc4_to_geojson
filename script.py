#!/usr/bin/env python3


import sys
import os
import json
from netCDF4 import Dataset

def convert_nc4_to_geojson(nc4_path, extent=True):
    ds = Dataset(nc4_path)
    lon_lat_list = [(float(lon.data), float(lat.data)) for lon, lat in zip(ds.variables["lon"], ds.variables["lat"])]
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "MultiPoint",
                "coordinates": lon_lat_list
            }
        }
    ]
    if extent:
        features.append({
            "type": "Feature",
            "geometry": json.loads(ds.extent),
        })
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    out_path = nc4_path + ".geojson"
    with open(out_path, "w") as f:
        f.write(json.dumps(geojson))

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <directory or .nc4 file> [extent=True|False]")
        sys.exit(1)
    input_path = sys.argv[1]
    extent = True
    if len(sys.argv) > 2:
        arg = sys.argv[2].lower()
        if arg == "extent=false":
            extent = False
        elif arg == "extent=true":
            extent = True
        else:
            print("Second argument must be extent=True or extent=False")
            sys.exit(1)
    if os.path.isdir(input_path):
        for fname in os.listdir(input_path):
            if fname.endswith(".nc4"):
                nc4_file = os.path.join(input_path, fname)
                print(f"Converting {nc4_file} to geojson...")
                convert_nc4_to_geojson(nc4_file, extent=extent)
    elif input_path.endswith(".nc4") and os.path.isfile(input_path):
        convert_nc4_to_geojson(input_path, extent=extent)
    else:
        print("Input must be a directory or a .nc4 file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
