from extras.plugins import PluginConfig


class aisPluginConfig(PluginConfig):
    name = "aisPlugin"
    verbose_name = "AIS Plugin"
    description = ""
    version = "0.1"
    author = "Adam Jarvis"
    author_email = "ajarvis"
    base_url = "ais"
    required_settings = []
    default_settings = {}


config = aisPluginConfig
