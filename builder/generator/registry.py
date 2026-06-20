from builder.generator.domain import DomainGenerator
from builder.generator.project_generator import ProjectGenerator


class GeneratorRegistry:
    def __init__(self):
        self._generators = {}

    def register(self, name, generator_class):
        self._generators[name] = generator_class

    def create(self, name):
        if name not in self._generators:
            raise Exception("Unknown generator")

        return self._generators[name]()


def default_registry():
    registry = GeneratorRegistry()
    registry.register("domain", DomainGenerator)
    registry.register("project", ProjectGenerator)
    return registry
