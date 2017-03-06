import pytest

from dronemapp.gpsimage import GPSImage


@pytest.fixture
def dji_image_path():
    return 'tests/fixtures/images/dji-0001.jpg'


@pytest.fixture
def dji_image(dji_image_path):
    return open(dji_image_path, 'rb')


@pytest.fixture
def dji_image_object(dji_image):
    return GPSImage(dji_image)
