
from configuration.drawconfiguration import DrawConfiguration
from configuration.drawconfiguration import DrawConfigurationConstants
from configuration.figurefactoryconfiguration import FigureFactoryConfiguration
from configuration.figurefactoryconfiguration import FigureFactoryConfigurationConstants
from configuration.movementfactoryconfiguration import MovementFactoryConfiguration
from configuration.movementfactoryconfiguration import MovementFactoryConfigurationConstants

class Configuration(
    DrawConfiguration,
    FigureFactoryConfiguration,
    MovementFactoryConfiguration
    ):
    ...

