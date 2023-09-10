
from __future__ import annotations

from time import sleep
from core.mouse import Mouse
from core.figure import Figure

from typing import Tuple
from typing import Iterator

class Draw(object):
    mouse: Mouse = None
    figures: Tuple[Figure] = None
    figures_duration: float|int = None
    repeat: int = None
    repeat_duration: float|int = None

    def __init__(self, mouse: Mouse, figures: Tuple[Figure], figures_duration = 3, repeat: int = 10, repeat_duration: float|int = 10):
        self.mouse = mouse
        self.figures = figures
        self.figures_duration = figures_duration
        self.repeat = repeat
        self.repeat_duration = repeat_duration

    def start_figure(self, figure: Figure) -> Iterator[Draw]:
        for simulated_point in figure.simulate():
            self.mouse.move_with_movement(point = simulated_point)
        
        yield self

    def start_figures(self) -> Iterator[Draw]:
        for figure in self.figures:
            for yielded in self.start_figure(figure):
                yield yielded

    def start_with_limit(self) -> Iterator[Draw]:
        for _ in range(self.repeat):
            for yielded in self.start_figures():
                yield yielded
                sleep(self.figures_duration)
            sleep(self.repeat_duration)

    def start_without_limit(self) -> Iterator[Draw]:
        while True:
            for yielded in self.start_figures():
                yield yielded
                sleep(self.figures_duration)
            sleep(self.repeat_duration)

    def start(self) -> Iterator[Draw]:
        if self.repeat == 0:
            for yielded in self.start_without_limit():
                yield yielded

        else:
            for yielded in self.start_with_limit():
                yield yielded