from pathlib import Path

from builder.generator.desktop_generator_result import DesktopGeneratorResult
from builder.template.engine import TemplateEngine


class DesktopGenerator:
    def __init__(self):
        self.engine = TemplateEngine()

    def generate(self, name: str, output_root: str = "output/desktop") -> DesktopGeneratorResult:
        project_path = Path(output_root) / name
        desktop_path = project_path / "src" / "desktop"
        tests_path = project_path / "tests"

        folders = [
            desktop_path,
            desktop_path / "widgets",
            desktop_path / "services",
            desktop_path / "viewmodels",
            desktop_path / "adapters",
            desktop_path / "pages",
            tests_path,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

        context = {
            "project_name": name,
            "class_name": self._to_class_name(name),
        }

        files = {
            desktop_path / "__init__.py": '"""Generated desktop package."""\n',
            desktop_path / "app.py": self.engine.render("templates/desktop/app.tpl", context),
            desktop_path / "main_window.py": self.engine.render("templates/desktop/main_window.tpl", context),
            desktop_path / "theme.py": self.engine.render("templates/desktop/theme.tpl", context),
            desktop_path / "widgets" / "__init__.py": '"""Generated desktop widgets."""\n',
            desktop_path / "services" / "__init__.py": '"""Generated desktop services."""\n',
            desktop_path / "viewmodels" / "__init__.py": '"""Generated desktop viewmodels."""\n',
            desktop_path / "adapters" / "__init__.py": '"""Generated desktop adapters."""\n',
            desktop_path / "pages" / "__init__.py": '"""Generated desktop pages."""\n',
            tests_path / "test_desktop_foundation.py": self.engine.render(
                "templates/desktop/test_desktop_foundation.tpl",
                context,
            ),
        }

        generated_files = []

        for path, content in files.items():
            path.write_text(content, encoding="utf-8")
            generated_files.append(path)

        return DesktopGeneratorResult(
            project_name=name,
            project_path=project_path,
            generated_files=tuple(generated_files),
        )

    @staticmethod
    def _to_class_name(name: str) -> str:
        cleaned = name.replace("-", "_").replace(" ", "_")
        return "".join(part.capitalize() for part in cleaned.split("_") if part)
