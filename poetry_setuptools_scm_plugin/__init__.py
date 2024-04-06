from setuptools_scm import ScmVersion


def no_local_scheme(_version: ScmVersion) -> str:
    return ""
