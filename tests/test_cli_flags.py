import pytest
from extra_markers import INT_MARKER
from extra_markers import O_INT_CLI_FLAG
from extra_markers import O_S_INT_CLI_FLAG
from extra_markers import S_INT_MARKER
from extra_markers import W_INT_CLI_FLAG
from extra_markers import W_S_INT_CLI_FLAG


@pytest.fixture
def outcomes(request):
    passed, failed, skipped = request.param
    return dict(passed=passed, failed=failed, skipped=skipped)


@pytest.mark.parametrize(
    "marker,second_test,args,outcomes",
    [
        [INT_MARKER, True, None, (1, 0, 1)],
        [INT_MARKER, False, None, (0, 0, 1)],
        [INT_MARKER, True, [W_INT_CLI_FLAG], (2, 0, 0)],
        [INT_MARKER, False, [O_INT_CLI_FLAG], (1, 0, 0)],
        [INT_MARKER, True, [O_INT_CLI_FLAG], (1, 0, 1)],
        [S_INT_MARKER, True, None, (1, 0, 1)],
        [S_INT_MARKER, False, None, (0, 0, 1)],
        [S_INT_MARKER, True, [W_S_INT_CLI_FLAG], (2, 0, 0)],
        [S_INT_MARKER, False, [O_S_INT_CLI_FLAG], (1, 0, 0)],
        [S_INT_MARKER, True, [O_S_INT_CLI_FLAG], (1, 0, 1)],
        [INT_MARKER, False, [W_S_INT_CLI_FLAG], (0, 0, 1)],
        [S_INT_MARKER, False, [W_INT_CLI_FLAG], (0, 0, 1)],
    ],
    indirect=["outcomes"],
)
def test_integration_markers(pytester, second_test, marker, args, outcomes):
    custom_test = f"""
        import pytest
        @pytest.mark.{marker}
        def test_always_pass_a():
            assert True
        """
    if second_test:
        custom_test += """
        def test_always_pass_b():
            assert True
        """

    pytester.makepyfile(custom_test)
    if args is None:
        result = pytester.runpytest()
    else:
        result = pytester.runpytest(*args)
    result.assert_outcomes(**outcomes)


def test_w_all_integration_markers(pytester):
    custom_test = """
        import pytest
        @pytest.mark.integration
        def test_always_pass_a():
            assert True
        @pytest.mark.slow_integration
        def test_always_pass_b():
            assert True
        def test_always_pass_c():
            assert True
        """

    pytester.makepyfile(custom_test)
    result = pytester.runpytest(W_INT_CLI_FLAG, W_S_INT_CLI_FLAG)
    result.assert_outcomes(passed=3)
