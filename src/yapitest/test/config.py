from pathlib import Path
from utils.yaml import YamlFile


class ConfigFile(YamlFile):

    def __init__(self, file: Path):
        super().__init__(file)
