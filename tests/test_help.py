import pytest
from extra_markers.markers import O_INT_CLI_FLAG
from extra_markers.markers import O_S_INT_CLI_FLAG
from extra_markers.markers import W_INT_CLI_FLAG
from extra_markers.markers import W_S_INT_CLI_FLAG


@pytest.mark.parametrize(
    "flag", [W_INT_CLI_FLAG, O_INT_CLI_FLAG, W_S_INT_CLI_FLAG, O_S_INT_CLI_FLAG]
)
def test_help_message(pytester, flag):
    result = pytester.runpytest(
        "--help",
    )
    result.stdout.fnmatch_lines(
        [
            "pytest-extra-markers:",
            f"*{flag}*",
        ]
    )
