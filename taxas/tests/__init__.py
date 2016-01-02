from os import path
PROJECT_ROOT = path.abspath(path.dirname(__file__))


class MockResponse:

    def __init__(self, file_test):
        self.file_test = path.join(PROJECT_ROOT, file_test)

    def __str__(self):
        handle = open(self.file_test)
        html = "".join(handle)
        return html
