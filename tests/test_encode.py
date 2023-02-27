from __future__ import absolute_import

import pytest

from blurhash import encode


def test_encode_file():
    with open("tests/pic2.png", "rb") as image_file:
        result, width, height = encode(image_file.read(), 4, 3)

    assert width == 314
    assert height == 176
    assert result == "LlMF%n00%#MwS|WCWEM{R*bbWBbH"


def test_encode_black_and_white_picture():
    with open("tests/pic2_bw.png", "rb") as image_file:
        result, _, _ = encode(image_file.read(), 4, 3)

    assert result == "LjIY5?00?bIUofWBWBM{WBofWBj["


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
