from converter.filename_or_extension import select_file_name
import pytest


@pytest.mark.parametrize('a, expected_result', [('crocodile.jpeg', 'crocodile'),
                                                ('dd.py', 'dd'),
                                                ('22.mov', '22')])
def test_select_file_name_good(a, expected_result):
    assert select_file_name(a) == expected_result


@pytest.mark.parametrize('expected_exception, filename', [(TypeError, 22),
                                                          (AttributeError, 'ssssss'),
                                                          (AttributeError, 'sdfjfds kdsnfsdk fff')])
def test_file_nane_error(expected_exception, filename):
    with pytest.raises(expected_exception):
        select_file_name(filename)
