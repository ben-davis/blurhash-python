from __future__ import absolute_import

import pytest
import pyvips

from blurhash import encode


def test_encode_image():
    image = pyvips.Image.new_from_file("tests/pic2.png")
    result = encode(image, 4, 3)

    assert result == "LjL{rA00%#Mxg2RkWYIoR*X8R*WV"


def test_encode_file():
    with open("tests/pic2.png", "rb") as image_file:
        result = encode(image_file.read(), 4, 3)

    assert result == "LjL{rA00%#Mxg2RkWYIoR*X8R*WV"


def test_encode_black_and_white_picture():
    with open("tests/pic2_bw.png", "rb") as image_file:
        result = encode(image_file.read(), 4, 3)

    assert result == "LhI5Y-00?bIUt7RjayIUWBofWBay"


def test_invalid_image():
    with pytest.raises(IOError):
        with open("README.md", "rb") as image_file:
            encode(image_file.read(), 4, 3)


def test_invalid_x_components():
    with open("tests/pic2.png", "rb") as image_file:
        with pytest.raises(ValueError):
            encode(image_file.read(), 10, 3)

    with open("tests/pic2.png", "rb") as image_file:
        with pytest.raises(ValueError):
            encode(image_file.read(), 0, 3)


def test_invalid_y_components():
    with open("tests/pic2.png", "rb") as image_file:
        with pytest.raises(ValueError):
            encode(image_file.read(), 4, 10)

    with open("tests/pic2.png", "rb") as image_file:
        with pytest.raises(ValueError):
            encode(image_file.read(), 4, 0)
