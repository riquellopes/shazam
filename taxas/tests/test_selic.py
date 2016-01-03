import responses
from taxas import Selic
from . import MockResponse


@responses.activate
def test_selic_ok():
    body = MockResponse("selic_index.html")
    responses.add(responses.GET,
                  "http://www3.bcb.gov.br/selic/consulta/taxaSelic.do?method=listarTaxaDiaria",
                  body=str(body), content_type='text/html', match_querystring=True)

    selic = Selic()
    assert selic.get() == "14,15%"
