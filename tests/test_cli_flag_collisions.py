import pytest
from extra_markers import O_INT_CLI_FLAG
from extra_markers import O_S_INT_CLI_FLAG


@pytest.mark.parametrize("args", [(O_INT_CLI_FLAG, O_S_INT_CLI_FLAG)])
def test_cli_collisions(pytester, args):
    pytester.makepyfile(
        """
    def test_always_pass():
        assert True
    """
    )

    result = pytester.runpytest(*args)
    result.stdout.fnmatch_lines(
        ["*Cannot have both*" + "".join([f"*{flag}*" for flag in args])]
    )
