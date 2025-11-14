import requests


class InvalidTestException:

    def __init__(self, test, message):
        super.__init__(f"Invalid Test: {test} " + message)


class ApiTestStep:

    def __init__(self, data, test):
        self.raw_data = data
        self.api_test = test
        # Optional
        self.id = data.get("id")
        # Mandatory
        self.path = data.get("path")
        if self.path is None:
            msg = f"Steps must contain `path` (step id:{self.id})"
            raise InvalidTestException(self.api_test, msg)

        self.url = data.get("url")
        if self.url is None:
            self.url = self.config.urls.get("base")
        if self.url is None:
            msg = f"Steps must contain `url` or it must be defined in yap-config.yaml (step id:{self.id})"
            raise InvalidTestException(self.api_test, msg)
        # Default to GET
        self.method = data.get("method", "GET").lower()
        # If None, don't send any data
        self.data = data.get("data", None)
        # If None, don't send any headers
        self.headers = data.get("headers", {})
        # If None, don't check anything
        self.assertions = data.get("assert", None)

    @property
    def config(self):
        return self.api_test.config

    def run(self):
        method = getattr(requests, self.method)
        response = method(self.url + self.path, json=self.data, headers=self.headers)
        print(response)
        self.perform_assertions(response)

    def perform_assertions(self, response):
        if "status-code" in self.assertions:
            desired_rc = self.assertions["status-code"]
            assert response.status_code == desired_rc


class ApiTest:

    def __init__(self, testfile, name, data, config):
        self.name = name
        self.testfile = testfile
        self.data = data
        self.config = config

    def __repr__(self) -> str:
        file_path = self.testfile._get_readable_path()
        return "ApiTest: " + file_path + ":" + self.name

    def __str__(self) -> str:
        return self.__repr__()

    def generate_steps(self) -> None:
        if "steps" not in self.data:
            raise InvalidTestException(test, "`steps` not defined")
        self.test_steps = []
        self.steps_by_id = {}
        for step_data in self.data["steps"]:
            step = ApiTestStep(step_data, self)
            self.steps_by_id[step.id] = step
            self.test_steps.append(step)
            print(step)

    def run(self):
        self.generate_steps()

        for step in self.test_steps:
            step.run()
