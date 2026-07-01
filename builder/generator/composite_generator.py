from pathlib import Path

from builder.generator.base_generator import BaseGenerator


class CompositeGenerator(BaseGenerator):
    category = "composite"

    def create_project_root(self, output_root: str | Path, name: str) -> Path:
        project_root = Path(output_root) / name
        project_root.mkdir(parents=True, exist_ok=True)
        return project_root

    def create_folders(self, folders: list[str | Path]) -> tuple[Path, ...]:
        created = []

        for folder in folders:
            created.append(self.ensure_directory(folder))

        return tuple(created)
