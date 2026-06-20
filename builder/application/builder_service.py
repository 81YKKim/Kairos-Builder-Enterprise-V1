from pathlib import Path

from builder.generator.project_generator import ProjectGenerator


class BuilderService:
    def __init__(self, project_generator: ProjectGenerator | None = None) -> None:
        self.project_generator = project_generator or ProjectGenerator()

    def create_project(self, name: str, output_root: str = "output/projects") -> Path:
        return self.project_generator.generate(name, output_root)
