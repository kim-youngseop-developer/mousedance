
from dataclasses import dataclass
from argparse import ArgumentParser

argument_parser = ArgumentParser(
    prog = "mouse-dance",
    description = "let the mouse dance!",
)

argument_parser.add_argument(
    "-p", # short term
    "--path", # long term
    type = str,
    default = "configuration.yaml",
    help = "a configuration path for the program.",
    required = True
)

@dataclass
class Arguments(object):
    path: str

arguments = Arguments(
    **vars(argument_parser.parse_args())
)

if __name__ == "__main__":
    from os import getlogin
    from core.mouse import Mouse
    from configuration.configuration import Configuration

    configuration = \
        Configuration(path = arguments.path)

    movement_factory = \
        configuration.create_movement_factory()
    
    mouse = Mouse(
        movement = movement_factory
    )

    figure_factories = \
        configuration.create_figure_factories()
    
    figure_factories_tuple = tuple(
        figure_factories
    )

    draw = configuration.create_draw(
        mouse = mouse,
        figures = figure_factories_tuple,
    )
    
    input(
         "\n"
        f"hello, {getlogin()}!\n"
         "\n"
         "we totally understand what you need.\n"
         "sometimes you juse want to have a great show by the famous mouse dancer.\n"
         "how about a cup of coffee during the show? :)\n"
         "\n"
        f"  1. the mouse dancer will dance with the following tempo.\n"
        f"      - time: {mouse.movement.time} seconds\n"
        f"      - steps: {mouse.movement.steps} steps\n"
         "\n"
         "  2. the mouse dancer prepared the follow sequence for you.\n"
        f"      - the show time: {draw.repeat} times\n"
        f"      - the show sequences: {' > '.join(map(lambda x: x.__class__.__name__, figure_factories_tuple))}\n"
        f"      - taking a break after finishing each dance: {draw.figures_duration} seconds\n"
        f"      - taking a break after finishing each sequence: {draw.repeat_duration} seconds\n"
        "\n"
        "press any key to watch the show!\n"
        "(to stop the show, then press ctrl + c.)"
    )

    for instance_draw in draw.start():
        ...