import responses
import pytest
from taxas import Dolar


@responses.activate
def test_dolar_ok():
    responses.add(responses.GET,
                  "http://api.dolarhoje.com",
                  body="3,50", content_type='text/html')

    dolar = Dolar()
    assert dolar.get() == "R$ 3,50"


@responses.activate
def test_dolar_200_sem_resposta():
    responses.add(responses.GET,
                  "http://api.dolarhoje.com", content_type='text/html')
    dolar = Dolar()
    with pytest.raises(Exception):
        dolar.get()
