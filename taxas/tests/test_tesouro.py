import responses
from taxas import Tesouro
from . import MockResponse


@responses.activate
def test_tesouro_ok():
    body = MockResponse("tesouro_index.html")
    responses.add(responses.GET,
                  "http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos",
                  body=str(body), content_type='text/html')

    tesouro = Tesouro()
    assert tesouro.get()[:61] == 'Tesouro IPCA+ com Juros Semestrais 2017 (NTNB) | C:-% V:6,65%'
