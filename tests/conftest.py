
def pytest_addoption(parser):
    parser.addoption("--binary-name", action="store", help="name of earthly binary for this platform", default="earthly-linux-amd64")
