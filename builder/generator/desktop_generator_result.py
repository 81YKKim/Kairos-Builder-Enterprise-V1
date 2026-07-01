from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class DesktopGeneratorResult:
    project_name: str
    project_path: Path
    generated_files: tuple[Path, ...] = field(default_factory=tuple)

    @property
    def generated_count(self) -> int:
        return len(self.generated_files)
