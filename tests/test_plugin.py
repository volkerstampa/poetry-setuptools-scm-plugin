from pathlib import Path
from subprocess import CompletedProcess, run
from typing import Any

from tomli_w import dump


def test_build_on_fresh_git(tmp_path: Path) -> None:
    _create_poetry_project_with_scm_plugin_in(tmp_path)
    _git_init(tmp_path, initial_commit=False)

    result = _poetry_build_in(tmp_path)

    result.check_returncode()
    assert "0.1.dev0" in result.stdout


def test_build_without_git(tmp_path: Path) -> None:
    _create_poetry_project_with_scm_plugin_in(tmp_path)

    result = _poetry_build_in(tmp_path)

    assert result.returncode != 0
    assert "no version" in result.stderr
    assert "not in a source repository supported by setuptools_scm" in result.stderr


def test_build_with_git_tag(tmp_path: Path) -> None:
    version = "1.2.3"
    _create_poetry_project_with_scm_plugin_in(tmp_path)
    _git_init(tmp_path, tag=version)

    result = _poetry_build_in(tmp_path)

    result.check_returncode()
    assert f"{version}.tar" in result.stdout


def test_build_with_commit_following_tag(tmp_path: Path) -> None:
    version = "1.2.3"
    next_version = "1.2.4"
    commits_after_tag = 2
    _create_poetry_project_with_scm_plugin_in(tmp_path)
    _git_init(tmp_path, tag=version, commits_after_tag=commits_after_tag)

    result = _poetry_build_in(tmp_path)

    result.check_returncode()
    assert f"{next_version}.dev{commits_after_tag}" in result.stdout


def test_build_without_setuptools_scm_section(tmp_path: Path) -> None:
    version = "2.3.4"
    _create_plain_poetry_project_in(tmp_path, version)
    _git_init(tmp_path)

    result = _poetry_build_in(tmp_path)

    result.check_returncode()
    assert f"{version}.tar" in result.stdout


_user_name = "test test"
_user_email = "test.test@test.test"


def _poetry_build_in(project_root: Path) -> CompletedProcess:
    return run(["poetry", "build"],  # noqa: S603,S607
               cwd=project_root,
               capture_output=True,
               check=False,
               timeout=5,
               text=True)


def _create_plain_poetry_project_in(project_root: Path, version: str) -> None:
    project_name = "test"
    pyproject = {"tool": _poetry_section(project_name, version)}
    _create_pyproject_toml(project_root, project_name, pyproject)


def _create_poetry_project_with_scm_plugin_in(project_root: Path) -> None:
    project_name = "test"
    poetry_section = _poetry_section(project_name, version="0")
    plugin_section = _setuptools_scm_section()
    pyproject = {"tool": poetry_section | plugin_section}
    _create_pyproject_toml(project_root, project_name, pyproject)


def _create_pyproject_toml(
        project_root: Path, package_name: str, pyproject: dict[str, Any]
) -> None:
    with (project_root / "pyproject.toml").open("wb") as f:
        dump(pyproject, f)
    source_dir = (project_root / package_name)
    source_dir.mkdir()
    (source_dir / "__init__.py").touch()


def _poetry_section(project_name: str, version: str) -> dict[str, Any]:
    return {
        "poetry": {
            "name": project_name,
            "version": version,
            "description": "test project created in unit test",
            "authors": [f"{_user_name} <{_user_email}>"],
        }
    }


def _setuptools_scm_section() -> dict[str, Any]:
    return {
        "setuptools_scm": {}
    }


def _git_init(
        project_root: Path,
        initial_commit: bool = True,
        tag: str | None = None,
        commits_after_tag: int = 0
) -> None:
    _git(project_root, "init")
    _git(project_root, "config", "--local", "user.name", _user_name)
    _git(project_root, "config", "--local", "user.email", _user_email)
    if initial_commit:
        _git_commit_all(project_root)
    if tag:
        _git(project_root, "tag", tag)
    for i in range(commits_after_tag):
        (project_root / f"empty{i}.py").touch()
        _git_commit_all(project_root)


def _git_commit_all(project_root: Path) -> None:
    _git(project_root, "add", ".")
    _git(project_root, "commit", "-m", "commit-msg")


def _git(cwd: Path, *args: str) -> CompletedProcess:
    return run(["git", *args], cwd=cwd, check=True, capture_output=True, timeout=5)  # noqa: S603,S607
