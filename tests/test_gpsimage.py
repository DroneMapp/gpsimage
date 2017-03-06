def test_manufacturer(dji_image_object):
    assert dji_image_object.manufacturer == 'DJI'


def test_model(dji_image_object):
    assert dji_image_object.model == 'FC6310'


def test_coordinates(dji_image_object):
    assert dji_image_object.x == -49.3407655
    assert dji_image_object.y == -25.65997133333333


def test_z(dji_image_object):
    assert dji_image_object.z == 1011.688


def test_dimensions(dji_image_object):
    assert dji_image_object.dimensions == (5472, 3648)


def test_datum(dji_image_object):
    assert dji_image_object.datum == 'WGS-84'


def test_geometry(dji_image_object):
    assert 'type' in dji_image_object.geometry
    assert dji_image_object.geometry['type'] == 'POINT'

    assert 'coordinates' in dji_image_object.geometry
    assert dji_image_object.geometry['coordinates'] == [-49.3407655, -25.65997133333333]
