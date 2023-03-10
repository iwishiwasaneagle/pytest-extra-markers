# pytest-extra-markers
[![CI](https://github.com/iwishiwasaneagle/pytest-extra-markers/actions/workflows/CI.yml/badge.svg)](https://github.com/iwishiwasaneagle/pytest-extra-markers/actions/workflows/CI.yml) [![CD](https://github.com/iwishiwasaneagle/pytest-extra-markers/actions/workflows/CD.yml/badge.svg)](https://github.com/iwishiwasaneagle/pytest-extra-markers/actions/workflows/CD.yml)

A [pytest](https://docs.pytest.org) plugin to dynamically skip tests based on [marks](https://docs.pytest.org/en/latest/reference/reference.html#marks)

## Installation

```bash
pip install pytest-extra-markers
```

## Usage

Consider the following test scenario:

```python
import pytest


# A
def test_speedy_unit_test():
    ...


# B
@pytest.mark.integration
def test_integration_test():
    ...


# C
@pytest.mark.slow_integration
def test_super_slow_integration_test():
    ...
```

You want to quickly run all your quick unit tests before committing. Then, after you are happy that the changes haven't messed up any unit tests you want to run the integration tests, and then after that your *super* slow integration tests. This would look like:

```bash
pytest
pytest --only-integration
pytest --only-slow-integration
```

In theory, your quick unit tests give you feedback instantly about anything that's been
broken by your changes. After that, the slower integration tests can be run to have a
more broad check.

> **Author's note**
> My use cases is mainly for simulations, so the `--only-slow-integration` flag
> can sometimes take tens of minutes to run whereas an integration test might take
> milliseconds. Therefore, I made the distinction between the two.

## CLI Flags

| Flag                     | Description                           |
|--------------------------|---------------------------------------|
| `--with-integration`      | Run all unit + integration tests      |
| `--with-slow-integration` | Run all unit + slow integration tests |
| `--only-integration`      | Only run integration tests            |
| `--only-slow-integration` | Only run slow integration tests       |

## Todo

- [x] Publish to PyPi
