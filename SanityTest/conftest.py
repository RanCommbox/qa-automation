def pytest_addoption(parser):
    parser.addoption("--is_headless", action="store_true", help="Run")


def pytest_generate_tests(metafunc):
    if 'is_headless' in metafunc.fixturenames:
        metafunc.parametrize("is_headless", [str(metafunc.config.getoption('is_headless'))])
