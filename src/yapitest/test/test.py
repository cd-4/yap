from typing import Dict, List
from test.config import ConfigFile


class Test:

    def __init__(self, name: str, data: Dict):
        self.configs = []
        self.name = name
        self.data = data

    def set_configs(self, configs: List[ConfigFile]):
        self.configs = configs
