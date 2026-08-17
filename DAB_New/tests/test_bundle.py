from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


def test_databricks_yml_exists():
    assert (PROJECT_ROOT / "databricks.yml").is_file()


def test_resources_directory_exists():
    assert (PROJECT_ROOT / "resources").is_dir()


def test_src_directory_exists():
    assert (PROJECT_ROOT / "src").is_dir()


def test_required_project_files_exist():
    for filename in ["databricks.yml", "pyproject.toml", "README.md"]:
        assert (PROJECT_ROOT / filename).is_file(), f"Missing {filename}"
