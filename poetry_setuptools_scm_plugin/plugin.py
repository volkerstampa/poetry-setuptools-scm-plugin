from contextlib import redirect_stdout
from io import StringIO

from cleo.io.io import IO
from poetry.plugins import Plugin
from poetry.poetry import Poetry

# noinspection PyProtectedMember
from setuptools_scm._cli import main


class SetuptoolsScmPlugin(Plugin):
    def activate(self, poetry: Poetry, io: IO) -> None:
        if not self.setuptools_scm_config_exists(poetry):
            return
        setuptools_scm_output = StringIO()
        try:
            with redirect_stdout(setuptools_scm_output):
                main([])
        except SystemExit as e:
            if e.args and "no version" in e.args[0]:
                io.write_error_line("ERROR: not in a source repository supported by setuptools_scm")
            raise
        # noinspection PyProtectedMember
        poetry.package._set_version(setuptools_scm_output.getvalue())  # noqa: SLF001

    @staticmethod
    def setuptools_scm_config_exists(poetry: Poetry) -> bool:
        return poetry.pyproject.data.get("tool", {}).get("setuptools_scm") is not None
