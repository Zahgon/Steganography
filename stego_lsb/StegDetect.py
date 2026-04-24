# -*- coding: utf-8 -*-
"""
    stego_lsb.StegDetect
    ~~~~~~~~~~~~~~~~~~~~

    This module contains functions for detecting images
    which have been modified using the functions from
    the module :mod:`stego_lsb.LSBSteg`.

    :copyright: (c) 2015 by Ryan Gibson, see AUTHORS.md for more details.
    :license: MIT License, see LICENSE.md for more details.
"""
import logging
import os
from time import time
from typing import cast, Tuple, Iterable

from PIL import Image

log = logging.getLogger(__name__)


def show_lsb(image_path: str, n: int) -> None:
    """Shows the n least significant bits of image"""
    pass
