import responses
from taxas import Dolar


@responses.activate
def test_cdi_ok():
    responses.add(responses.GET,
                  "http://api.dolarhoje.com",
                  body="3,50", content_type='text/html')

    dolar = Dolar()
    assert dolar.get() == "R$ 3,50"
