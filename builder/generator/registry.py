from builder.generator.adapter_generator import AdapterGenerator
from builder.generator.desktop_generator import DesktopGenerator
from builder.generator.domain import DomainGenerator
from builder.generator.page_generator import PageGenerator
from builder.generator.project_generator import ProjectGenerator
from builder.generator.repository_generator import RepositoryGenerator
from builder.generator.service import ServiceGenerator
from builder.generator.unit_test import UnitTestGenerator
from builder.generator.viewmodel_generator import ViewModelGenerator
from builder.generator.widget_generator import WidgetGenerator


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
    registry.register("adapter", AdapterGenerator)
    registry.register("desktop", DesktopGenerator)
    registry.register("domain", DomainGenerator)
    registry.register("page", PageGenerator)
    registry.register("project", ProjectGenerator)
    registry.register("repository", RepositoryGenerator)
    registry.register("service", ServiceGenerator)
    registry.register("unit_test", UnitTestGenerator)
    registry.register("viewmodel", ViewModelGenerator)
    registry.register("widget", WidgetGenerator)
    return registry
