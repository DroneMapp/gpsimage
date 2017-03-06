from dronemapp.gpsimage import GPSImageFromFile


def test_gpsimagefromfile(dji_image_path):
    img = GPSImageFromFile(dji_image_path)
    assert img.x != 0
    assert img.y != 0
    assert img.z != 0
