from typing import Dict


class TestStep:

    def __init__(self, data: Dict):
        self.raw_data = data

    def pre_run(self):
        pass

    def post_run(self):
        pass

    def run(self):
        self.pre_run()
        self.run_step()
        self.post_run()

    def run_step(self):
        pass
