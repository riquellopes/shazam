import responses
import pytest
from taxas import Cdi
from . import MockResponse


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
