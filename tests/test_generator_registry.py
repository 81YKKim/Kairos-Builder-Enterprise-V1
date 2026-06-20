from builder.generator.domain import DomainGenerator
from builder.generator.project import ProjectGenerator
from builder.generator.registry import GeneratorRegistry, default_registry


def test_generator_registry_registers_and_creates_generator():
    registry = GeneratorRegistry()

    registry.register("domain", DomainGenerator)

    generator = registry.create("domain")

    assert isinstance(generator, DomainGenerator)


def test_default_registry_creates_project_generator():
    registry = default_registry()

    generator = registry.create("project")

    assert isinstance(generator, ProjectGenerator)
