from builder.generator.desktop_generator import DesktopGenerator
from builder.generator.domain import DomainGenerator
from builder.generator.project_generator import ProjectGenerator
from builder.generator.repository_generator import RepositoryGenerator
from builder.generator.service import ServiceGenerator
from builder.generator.unit_test import UnitTestGenerator


class GeneratorRegistry:
    def __init__(self):
        self._generators = {}

    def register(self, name, generator_class):
        self._generators[name] = generator_class

    def create(self, name):
        if name not in self._generators:
            raise ValueError("Unknown generator")

        return self._generators[name]()

    def names(self):
        return tuple(sorted(self._generators.keys()))


def default_registry():
    registry = GeneratorRegistry()
    registry.register("desktop", DesktopGenerator)
    registry.register("domain", DomainGenerator)
    registry.register("service", ServiceGenerator)
    registry.register("unit_test", UnitTestGenerator)
    registry.register("project", ProjectGenerator)
    registry.register("repository", RepositoryGenerator)
    return registry
