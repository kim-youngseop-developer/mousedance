
from enum import StrEnum
from copy import deepcopy
from core.mouse import MovementFactory
from configuration.baseconfiguration import BaseConfiguration

from typing import Any
from typing import Dict

class MovementFactoryConfigurationConstants(StrEnum):
    MOVEMENT_FACTORY: str = "movement-factory"

class MovementFactoryConfiguration(BaseConfiguration[Dict[str, Any]]):
    
    @property
    def movement_factory(self) -> Dict[str, Any]:
        return self.get(MovementFactoryConfigurationConstants.MOVEMENT_FACTORY.value)
    
    def create_movement_factory(self, **runtime_keyword_arguments) -> MovementFactory:
        movement_factory_copied = deepcopy(self.movement_factory)
        movement_factory_copied.update(runtime_keyword_arguments)
        return MovementFactory(**movement_factory_copied)