
from enum import StrEnum
from copy import deepcopy
from core.draw import Draw
from configuration.baseconfiguration import BaseConfiguration

from typing import Dict
from typing import Any

class DrawConfigurationConstants(StrEnum):
    DRAW: str = "draw"

class DrawConfiguration(BaseConfiguration[Dict[str, Any]]):
    
    @property
    def draw(self) -> Dict[str, Any]:
        return self.get(DrawConfigurationConstants.DRAW.value)

    def create_draw(self, **runtime_keyword_arguments) -> Draw:
        draw_copied = deepcopy(self.draw)
        draw_copied.update(runtime_keyword_arguments)
        return Draw(**draw_copied)