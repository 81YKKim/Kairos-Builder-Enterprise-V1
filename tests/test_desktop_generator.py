from pathlib import Path

from builder.generator.desktop_generator import DesktopGenerator
from builder.generator.registry import default_registry


def test_desktop_generator_creates_enterprise_desktop_foundation(tmp_path: Path):
    result = DesktopGenerator().generate("KairosDesktop", str(tmp_path))

    assert result.project_name == "KairosDesktop"
    assert result.generated_count == 10
    assert (result.project_path / "src" / "desktop" / "app.py").exists()
    assert (result.project_path / "src" / "desktop" / "main_window.py").exists()
    assert (result.project_path / "src" / "desktop" / "theme.py").exists()
    assert (result.project_path / "src" / "desktop" / "widgets" / "__init__.py").exists()
    assert (result.project_path / "src" / "desktop" / "services" / "__init__.py").exists()
    assert (result.project_path / "src" / "desktop" / "viewmodels" / "__init__.py").exists()
    assert (result.project_path / "src" / "desktop" / "adapters" / "__init__.py").exists()
    assert (result.project_path / "tests" / "test_desktop_foundation.py").exists()


def test_default_registry_supports_desktop_generator():
    registry = default_registry()

    assert "desktop" in registry.names()
    assert isinstance(registry.create("desktop"), DesktopGenerator)
