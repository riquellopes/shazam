# recupera cotação do papel da bolsa de valores
import os
import logging
import requests
from bs4 import BeautifulSoup
from .taxa import Taxa

logr = logging.getLogger(os.environ.get("LOG-NAME"))

BOVESPA_QUOTE_URL = "http://www.bmfbovespa.com.br/Pregao-Online/ExecutaAcaoAjax.asp?CodigoPapel={0}"


class Bolsa(Taxa):

    def get(self, *args):
        logr.info("INICIANDO CHAMADA AO SERVICO DE BMFBOVESPA")
        try:
            response = requests.get(BOVESPA_QUOTE_URL.format(str(args[0])))
            xml = BeautifulSoup(response.content, 'html.parser')
            return """
                Abertura={0}\nMinimo={1}\nMaximo={2}\nUltimo={3}\nOscilacao={4}
            """.format(
                xml.comportamentopapeis.papel['abertura'],
                xml.comportamentopapeis.papel['minimo'],
                xml.comportamentopapeis.papel['maximo'],
                xml.comportamentopapeis.papel['ultimo'],
                xml.comportamentopapeis.papel['oscilacao']
            ).strip()
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
