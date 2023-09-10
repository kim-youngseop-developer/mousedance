
from functools import lru_cache

from typing import Optional
from typing import Iterator
from typing import Tuple

from ctypes import windll
user32 = getattr(windll, "user32")

class Point(object):
    x: Optional[int] = None
    y: Optional[int] = None

    def __init__(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        self.x = x
        self.y = y    
    
    def __iter__(self) -> Iterator[int]:
        yield self.x
        yield self.y

class Resolution(object):

    @classmethod
    def get_system_metricts(cls, index: int) -> int:
        """
        the callable refers the function `GetSystemMetrics (winuser.h)`.
        please visit the [document page](https://learn.microsoft.com/ko-kr/windows/win32/api/winuser/nf-winuser-getsystemmetrics)
        if you want to read more information about the function.

        :param index: the system metric or configuration setting to be retrieved.
        this parameter can be one of the following [values](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics#parameters). 
        note that all `SM_CX*` values are widths, and all `SM_CY*` values are heights. 
        also note that all settings designed to return boolean data represent `True` as any nonzero value, 
        and `False` as a zero value.

        :return: if the function succeeds, the return value is the requested system metric or configuration setting.
        if the function fails, the return value is 0. 
        please note that `GetLastError` does not provide extended error information.
        """
        return getattr(user32, "GetSystemMetrics")(index)
    
    @classmethod
    @property
    @lru_cache
    def point_top_left(cls) -> Point:
        return Point(
            x = 0,
            y = 0
        )

    @classmethod
    @property
    @lru_cache
    def point_top_right(cls) -> Point:
        return Point(
            x = cls.get_system_metricts(0),
            y = 0
        )

    @classmethod
    @property
    @lru_cache
    def point_bottom_left(cls) -> Point:
        return Point(
            x = 0,
            y = cls.get_system_metricts(1)
        )

    @classmethod
    @property
    @lru_cache
    def point_bottom_right(cls) -> Point:
        return Point(
            x = cls.get_system_metricts(0),
            y = cls.get_system_metricts(1)
        )
    
    @classmethod
    @property
    @lru_cache
    def point_center(cls) -> Point:
        # set point at the bottom right.
        point_bottom_right = cls.point_bottom_right
        # set point at the top left.
        point_top_left = cls.point_top_left
        return Point(
            x = int((point_bottom_right.x - point_top_left.x) / 2),
            y = int((point_bottom_right.y - point_top_left.y) / 2)
        )
    
    @classmethod
    @property
    @lru_cache
    def points(cls) -> Tuple[Point, Point, Point, Point]:
        return (
            cls.point_top_left,
            cls.point_top_right,
            cls.point_bottom_left,
            cls.point_bottom_right,
        )