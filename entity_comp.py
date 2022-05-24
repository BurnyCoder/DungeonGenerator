class Entity:
    def __init__(self, *components):
        self.components = {}

        for component in components:
            self.set(component)

    def set(self, component):
        key = type(component)
        self.components[key] = component

    def get(self, clazz):
        return self.components[clazz]

    def has(self, clazz):
        return self.get(clazz) is not None