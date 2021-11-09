# -*- coding: utf-8 -*-

from .mallett2019 import (SPECTRAL_SHAPE_sRGB_MALLETT2019,
                          MSDS_BASIS_FUNCTIONS_sRGB_MALLETT2019)
from .otsu2018 import (SPECTRAL_SHAPE_OTSU2018, BASIS_FUNCTIONS_OTSU2018,
                       CLUSTER_MEANS_OTSU2018, SELECTOR_ARRAY_OTSU2018)
from .smits1999 import SDS_SMITS1999

__all__ = [
    'SPECTRAL_SHAPE_sRGB_MALLETT2019',
    'MSDS_BASIS_FUNCTIONS_sRGB_MALLETT2019',
]
__all__ += [
    'SPECTRAL_SHAPE_OTSU2018',
    'BASIS_FUNCTIONS_OTSU2018',
    'CLUSTER_MEANS_OTSU2018',
    'SELECTOR_ARRAY_OTSU2018',
]
__all__ += [
    'SDS_SMITS1999',
]
