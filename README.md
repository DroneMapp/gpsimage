# GPSImage Library by Dronemapp

[![CircleCI](https://circleci.com/gh/DroneMapp/gpsimage.svg?style=svg)](https://circleci.com/gh/DroneMapp/gpsimage)

Based on the work of ![Denis Carriere](https://github.com/DenisCarriere/)
on his ![gpsimage](https://github.com/DenisCarriere/gpsimage) library.

Retrieves GPS data from geo-referenced images.


## Install

```bash
$ pip install dronemapp-gpsimage
```

## Python Example

```python
>>> from dronemapp.gpsimage import GPSImageFromFile
>>> img = GPSImageFromFile('your-image.jpg')

# Coordinates Latitude & Longitude in Degrees 
>>> img.y, img.x
45.413140 -75.656703

# Altitude in Feet
>>> img.z
142.04025779

# From 0 to 360 Degrees
>>> img.direction
165.974436341
...
```

## Attributes

### GPS data
- **y** - Latitude (Degrees)
- **x** - Longitude (Degrees)
- **geometry** - GeoJSON Point
- **z** - Elevation Above Mean Sea Level
- **datum** - Coordinate system (Typically WGS84)
- **direction** - Camera orientation (0-360 degrees)
- **has_latlng** - True or False if planar coordinates exists

### Device Specific
- **timestamp** - Calendar dates (YYYY-MM-DD HH:MM:SS)
- **model** - Device model (Galaxy Nexus)
- **manufacturer** - Device manufacturer (Samsung)

### Standard
- **width**
- **height**
- **dimensions**
