from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

from .exceptions import ExifNotFoundError


def invert_dict(d):
    return {value: key for key, value in d.items()}


class GPSData:
    def __init__(self, gpsinfo):
        self.GPSTAGS = invert_dict(GPSTAGS)
        self.gpsinfo = gpsinfo

    def __getattr__(self, name):
        key = 'GPS' + name
        return self.gpsinfo.get(self.GPSTAGS.get(key))


class ExifData:
    def __init__(self, image):
        self.TAGS = invert_dict(TAGS)
        self.exifdata = self.open_exif(image)

    def __getattr__(self, name):
        return self.exifdata.get(self.TAGS.get(name))

    def open_exif(self, image):
        exif = image._getexif()
        if not exif:
            raise ExifNotFoundError()

        return exif


class GPSImage:
    def __init__(self, image_data):

        self.image = Image.open(image_data, "r")

        self.exif_data = ExifData(self.image)
        self.gps_data = GPSData(self.exif_data.GPSInfo)

    def __repr__(self):
        if self.has_latlng:
            return '<{} [{}, {} ({})]>'.format(self.__class__.__name__, self.y, self.x, self.datum)
        else:
            return '<{}>'.format(self.__class__.__name__)

    def _dms_to_dd(self, dms, ref):
        if len(dms) == 3:
            degrees = (dms[0][0] / dms[0][1])
            minutes = (dms[1][0] / dms[1][1]) / 60
            seconds = (dms[2][0] / dms[2][1]) / 3600
            dd = degrees + minutes + seconds

            # South & West returns Negative values
            if ref in ['S', 'W']:
                dd *= -1
            return dd

    @property
    def dpi(self):
        value = self.image.info.get('dpi')
        if value and any(value):
            return value

    @property
    def has_latlng(self):
        return self.y and self.x

    @property
    def model(self):
        return self.exif_data.Model.split('\x00')[0]

    @property
    def manufacturer(self):
        return self.exif_data.Make.split('\x00')[0]

    @property
    def datum(self):
        return self.gps_data.MapDatum or 'WGS-84'

    @property
    def x(self):
        lng_dms = self.gps_data.Longitude
        lng_ref = self.gps_data.LongitudeRef
        return self._dms_to_dd(lng_dms, lng_ref)

    @property
    def y(self):
        lat_dms = self.gps_data.Latitude
        lat_ref = self.gps_data.LatitudeRef
        return self._dms_to_dd(lat_dms, lat_ref)

    @property
    def z(self):
        altitude = self.gps_data.Altitude
        return altitude[0] / altitude[1]

    @property
    def direction(self):
        return self.gps_data.ImgDirection

    @property
    def timestamp(self):
        return self.exif_data.DateTimeOriginal

    @property
    def width(self):
        return self.image.size[0]

    @property
    def height(self):
        return self.image.size[1]

    @property
    def dimensions(self):
        return (self.width, self.height)

    @property
    def geometry(self):
        if self.has_latlng:
            return {'type': 'POINT', 'coordinates': [self.x, self.y]}

    @property
    def satellites(self):
        if self.gps_data.Satellites:
            return int(self.gps_data.Satellites)

    def as_dict(self):
        container = {
            'x': self.x, 'y': self.y, 'z': self.z,
            'dimensions': self.dimensions,
            'geometry': self.geometry,
            'timestamp': self.timestamp,
            'satellites': self.satellites,
        }
        return container


class GPSImageFromFile(GPSImage):
    def __init__(self, file_path):
        with open(file_path, 'rb') as file_object:
            super().__init__(file_object)
