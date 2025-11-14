class DictWrapper:

    VAR_PREFIX = "$vars."

    def __init__(self, data, config):
        self.data = data
        self.config = config

    def get(self, key, default=None):
        if key in self.data:
            return self[key]
        return default

    def __getitem__(self, key):
        value = self.data.__getitem__(key)
        if isinstance(value, str):
            if value.startswith(DictWrapper.VAR_PREFIX):
                var_name = value[len(DictWrapper.VAR_PREFIX) :]
                return self.config.get_variable(var_name)
        return output
