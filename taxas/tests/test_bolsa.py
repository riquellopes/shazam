import responses
import pytest
from taxas import Bolsa
from . import MockResponse


@responses.activate
def test_cdi_ok():
    body = MockResponse("bbpo11.xml")
    responses.add(responses.GET,
                  "http://www.bmfbovespa.com.br/Pregao-Online/ExecutaAcaoAjax.asp?CodigoPapel=BBPO11",
                  body=str(body), content_type='text/xml', match_querystring=True)

    bolsa = Bolsa()
    assert bolsa.get("BBPO11") == 'Abertura=\nMinimo=96,53\nMaximo=96,98\nUltimo=96,98\nOscilacao=0,49'


@responses.activate
def test_cdi_notok():
    responses.add(responses.GET,
                  "http://www.bmfbovespa.com.br/Pregao-Online/ExecutaAcaoAjax.asp?CodigoPapel=BBPO11",
                  content_type='text/xml', status=500, match_querystring=True)
    bolsa = Bolsa()
    with pytest.raises(Exception):
        bolsa.get("BBPO11")
