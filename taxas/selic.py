# recupera taxa selic
import os
import requests
import logging
from bs4 import BeautifulSoup
from .taxa import Taxa

logr = logging.getLogger(os.environ.get("LOG-NAME"))


class Selic(Taxa):
    def get(self):
        logr.info("INICIANDO CHAMADA AO SERVICO DE SELIC")
        try:
            response = requests.get(
                "http://www3.bcb.gov.br/selic/consulta/taxaSelic.do?method=listarTaxaDiaria")

            html = BeautifulSoup(response.content, 'html.parser')
            selic = html.find("table", {"class": "tabelaTaxaSelic"}).findAll("td")[1].text

            logr.info("SELIC RECUPERADA COM SUCESSO {0}.".format(selic))
            return selic
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
