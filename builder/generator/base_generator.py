from pathlib import Path

from builder.template.engine import TemplateEngine


class BaseGenerator:
    category = "base"

    def __init__(self, template_engine: TemplateEngine | None = None):
        self.engine = template_engine or TemplateEngine()

    def ensure_directory(self, path: str | Path) -> Path:
        target = Path(path)
        target.mkdir(parents=True, exist_ok=True)
        return target

    def write_file(self, path: str | Path, content: str) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def render_template(self, template_path: str, context: dict) -> str:
        return self.engine.render(template_path, context)

    def to_class_name(self, name: str) -> str:
        cleaned = name.replace("-", "_").replace(" ", "_")
        return "".join(part.capitalize() for part in cleaned.split("_") if part)
