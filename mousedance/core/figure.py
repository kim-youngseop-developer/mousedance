
from math import cos
from math import sin
from math import radians
from enum import StrEnum
from random import randint

from core.utilities import Cache
from core.utilities import Factory
from core.mouse import MouseGlobal
from core.resolution import Point
from core.resolution import Resolution

from typing import Iterator
from typing import Optional

class Position(StrEnum):
    """
    the string enum class `Position` provides 
    a certain point to place the mouse 
    when a `Figure` instance calls `simulate_start_point`.

    - the value `POINT_CENTER` represents 
    a center point which of the screen resolution.
    
    - the value `POINT_CURRENT` represents 
    a current point of the mouse which is captured by the class `MouseGlobal`.

    - the value `POINT_CONSTRUCTED` represents 
    a point which is provided when constructing a `Figure` instance.
    """

    POINT_CENTER: str = "POINT_CENTER"
    POINT_CURRENT: str = "POINT_CURRENT"
    POINT_CONSTRUCTED: str = "POINT_CONSTRUCTED"

class Figure(object):
    """
    the class simulates points with calling the callables.
    but as the callable `simulate_points` is not implemented on this class,
    you should implement on a inherited class.
    
    1. `simulate`
    2. `simulate_start_point`
    3. `simulate_points`

    please remember that 
    the class does not draw a figure by itself, only simulating the points.
    and the simulation is started by being called the callable `simulate` by another instance.
    
    ```python
    class Rectangle(Figure):

        def simulate_points(self) -> Iterator[Point]:
            # yield points to draw a rectangle.
            yield ...
    ```
    """

    # cached point when after calling `simulate_start_point`.
    __cached: Cache[Point] = Cache(instance = None)
    # a point where to place the mouse when calling `simulate_start_point`.
    point: Optional[Point] = None
    # a position where to place the mouse when calling `simulate_start_point`.
    position: Position|str = None

    def __init__(self, point: Optional[Point] = None, position: Position|str = Position.POINT_CURRENT):
        self.point = point
        self.position = position

        # when the point is not provided.
        if self.point is None:
            # set the current mouse point.
            self.point = MouseGlobal.current

        # when the position is provided in string format.
        if isinstance(self.position, str):
            # set a created `Position` instance.
            self.position = Position(self.position)
        
        # when the position is not a instance of the class `Position`.
        if not isinstance(self.position, Position):
            # raise a type exception to avoid an unexpected error.
            raise TypeError(
                f"the field 'position' cannot be {self.position}."
            )
        
    @property
    def cached(self) -> Cache[Point]:
        return self.__cached
        
    def simulate_start_point(self) -> Point:
        # match cases for the position.
        match self.position:

            # when the mouse needs to be placed at the center point.
            case Position.POINT_CENTER:
                start_point = Resolution.point_center

            # when the mouse needs to be placed at current position.
            case Position.POINT_CURRENT:
                start_point = MouseGlobal.current
                
            # when the mouse needs to be placed back at the constructed point.
            case Position.POINT_CONSTRUCTED:
                start_point = self.point

        # cache the simulated start point.
        self.cached.instance = start_point

        # return the simulated start point.
        return start_point

    def simulate_points(self) -> Iterator[Point]:
        yield ...

    def simulate(self) -> Iterator[Point]:
        # simulate the start point.
        yield self.simulate_start_point()

        # simulate the points.
        for yielded in self.simulate_points():
            yield yielded

class FigureFactory(Factory[Figure]):
    ...

class Straight(Figure):
    # straight's another point
    another_point: Optional[Point] = None

    def __init__(self, point: Optional[Point] = None, position: Position|str = Position.POINT_CURRENT, another_point: Optional[Point] = None):
        # construct super class.
        super().__init__(point = point, position = position)
        # set another point.
        self.another_point = another_point

    def simulate_points(self) -> Iterator[Point]:
        if not self.another_point:
            another_point = Point(
                x = randint(0, Resolution.point_top_right.x),
                y = randint(0, Resolution.point_bottom_left.y),
            )

        else:
            another_point = self.another_point

        for point in [self.cached.instance, another_point]:
            yield point

class StraightPatrol(Straight):
    
    def simulate_points(self) -> Iterator[Point]:
        for yielded in super().simulate_points():
            yield yielded
        
        yield self.cached.instance

class Circle(Figure):
    # cicle's radius
    radius: Optional[int] = 100

    def __init__(self, point: Optional[Point] = None, position: Position|str = Position.POINT_CURRENT, radius: Optional[int] = 100):
        # construct super class.
        super().__init__(point = point, position = position)
        # set radius.
        self.radius = radius

    def simulate_points(self) -> Iterator[Point]:
        # set updatable point object.
        updatable_point = Point(x = None, y = None)

        # for each angle with 5 epoch.
        for angle in range(0, 361, 5):
            # set updated point x.
            updatable_point.x = self.cached.instance.x + self.radius * cos(radians(angle))
            # set updated point y.
            updatable_point.y = self.cached.instance.y + self.radius * sin(radians(angle))
            # yield the updated point.
            yield updatable_point