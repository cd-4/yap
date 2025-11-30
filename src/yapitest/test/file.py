from typing import List
from pathlib import Path
from utils.yaml import YamlFile
from test.test import Test


class TestFile(YamlFile):

    def __init__(self, file: Path):
        super().__init__(file)

    def _is_key_test(self, key: str):
        return key.startswith("test") or key.endswith("test")

    def get_tests(self) -> List[Test]:
        tests = []
        for test_name, test_data in self.data.items():
            if not self._is_key_test(test_name.lower()):
                continue
            tests.append(Test(test_name, test_data))

        return tests
