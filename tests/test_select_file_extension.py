import pytest

from converter.filename_or_extension import select_file_extension


def test_select_file_extension_good():
    assert select_file_extension('test_video.mp4') == 'mp4'


def test_select_file_extension_bad():
    with pytest.raises(AttributeError):
        select_file_extension('test_video')
