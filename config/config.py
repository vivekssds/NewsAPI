from grift import BaseConfig, ConfigProperty
from schematics.types import BooleanType, IntType, StringType
from schematics.types.compound import ListType
from config.settings_loader import get_settings_loaders


class NewsConfig(BaseConfig):
    CASSANDRA_HOST=ConfigProperty(property_type=ListType(StringType))
    CASSANDRA_PORT=ConfigProperty(property_type=IntType(),default=9042)
    KEY_SPACE = ConfigProperty(property_type=StringType())
    REDIS_HOST=ConfigProperty(property_type=StringType())
    REDIS_PORT=ConfigProperty(property_type=IntType(),default=6379)
    REDIS_KEY=ConfigProperty(property_type=StringType())
    NUMBER_OF_NEWS=ConfigProperty(property_type=IntType())
    CASSANDRA_QUERY=ConfigProperty(property_type=StringType())

    def __init__(self, loaders):
        """Initialize BaseConfig and metrics"""
        BaseConfig.__init__(self, loaders)


app_config = NewsConfig(get_settings_loaders())


