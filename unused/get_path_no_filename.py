#  a few ways to get the directory path of a file without the filename in Python:

import os
from pathlib import Path


def der_path(full_path):
    # using os
    dir_path = os.path.dirname(full_path)

    # Using pathlib.Path.parent
    dir_path = Path(full_path).parent

    # Splitting the string on slash and joining back
    dir_path = '/'.join(full_path.split('/')[:-1])
