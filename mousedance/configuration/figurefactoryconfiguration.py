
from enum import StrEnum
from copy import deepcopy
from core.figure import FigureFactory
from configuration.baseconfiguration import BaseConfiguration

from typing import Any
from typing import List
from typing import Dict
from typing import Iterator

class FigureFactoryConfigurationConstants(StrEnum):
    FIGURE_FACTORIES: str = "figure-factories"
    FIGURE_FACTORY: str = "figure-factory"

class FigureFactoryConfiguration(BaseConfiguration[Dict[str, List[Dict[str, Any]]]]):
    
    @property
    def figure_factories(self) -> Iterator[Dict[str, Any]]:
        for container in self.get(FigureFactoryConfigurationConstants.FIGURE_FACTORIES.value):
            yield container[FigureFactoryConfigurationConstants.FIGURE_FACTORY.value]

    def create_figure_factories(self, **runtime_keyword_arguments) -> Iterator[FigureFactory]:
        for figure_factory in self.figure_factories:
            figure_factory_copied = deepcopy(figure_factory)
            figure_factory_copied.update(runtime_keyword_arguments)
            yield FigureFactory(**figure_factory_copied)