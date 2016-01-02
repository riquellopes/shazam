from os import path
PROJECT_ROOT = path.abspath(path.dirname(__file__))

import responses
import pytest
from taxas import Cdi


class MockResponse:

    def __init__(self, file_test):
        self.file_test = path.join(PROJECT_ROOT, file_test)

    def __str__(self):
        handle = open(self.file_test)
        html = "".join(handle)
        return html


@responses.activate
def test_cdi_ok():
    body = MockResponse("cdi_index.html")
    responses.add(responses.GET,
                  "https://www.cetip.com.br",
                  body=str(body), content_type='text/html')

    cdi = Cdi()
    assert cdi.get() == "14,14%"


@responses.activate
def test_cdi_notok():
    responses.add(responses.GET,
                  "https://www.cetip.com.br", content_type='text/html', status=500)
    cdi = Cdi()
    with pytest.raises(Exception):
        cdi.get()
