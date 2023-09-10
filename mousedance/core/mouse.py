
from time import sleep

from core.resolution import Point
from core.utilities import Factory
from core.utilities import Singleton

from typing import Iterator

from pynput.mouse import Controller
class SingletonController(Singleton[Controller]):
    ...

class Movement(object):
    # how much time (second) to reach at destination.
    time: int|float = None
    # how many steps to update mouse position.
    steps: int = None

    def __init__(self, time: int = 0.01, steps: int = 100):
        self.time = time
        self.steps = steps

    def simulate(self, point: Point, current_point: Point = None) -> Iterator[None]:
        yield None

class MovementFactory(Factory[Movement]):
    ...

class Regular(Movement):

    def simulate(self, point: Point, current_point: Point = None) -> Iterator[Point]:
        # set updatable point object.
        updatable_point = Point(x = None, y = None)

        # set derivated x.
        derivated_x = (point.x - current_point.x) / self.steps
        # set derivated y.
        derivated_y = (point.y - current_point.y) / self.steps
        # set derivated time.
        derivated_time = self.time / self.steps

        # for each step.
        for step in range(self.steps):
            # set updated point x.
            updatable_point.x = int(current_point.x + (derivated_x * step))
            # set updated point y.
            updatable_point.y = int(current_point.y + (derivated_y * step))
            # yield the updated point.
            yield updatable_point
            # sleep the derivated time.
            sleep(derivated_time)

class Mouse(object):
    movement: Movement = None
    controller: Controller = None

    def __init__(self, movement: Movement):
        self.movement = movement
        self.controller = SingletonController()

    @property
    def current(self) -> Point:
        return Point(
            x = self.controller.position[0],
            y = self.controller.position[1]
        )

    def move(self, point: Point) -> None:
        self.controller.position = tuple(point)

    def move_with_movement(self, point: Point, current_point: Point = None) -> None:
        # when the argument is not provided.
        if not current_point:
            # set the current point.
            current_point = self.current
        
        # simulate points from the current point to the point.
        simulated_points = self.movement.simulate(
            point = point, 
            current_point = current_point
        )

        # for each simulated point.
        for simulated_point in simulated_points:
            # move mouse to the simulated point.
            self.move(point = simulated_point)
        
        return None

class MouseGlobal(object):
    controller: Controller = SingletonController()

    @classmethod
    @property
    def current(self) -> Point:
        return Point(
            x = self.controller.position[0],
            y = self.controller.position[1]
        )