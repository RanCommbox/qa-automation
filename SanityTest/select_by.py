from enum import Enum


class SelectBy(Enum):
    ID = 1
    XPATH = 2
    CSS_SELECTOR = 3
    CLASS_NAME = 4
    TAG_NAME = 5
