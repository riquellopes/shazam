# Recuperar taxas do tesouto direto.
import os
import requests
import logging
from bs4 import BeautifulSoup
from .taxa import Taxa

logr = logging.getLogger(os.environ.get("LOG-NAME"))

TESOURO_URL = "http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos"


class TesouroDireto(Taxa):

    def get(self):
        try:
            response = requests.get(TESOURO_URL)
            html = BeautifulSoup(response.content, 'html.parser')
            titulos = []
            trs = html.findAll("tr", {"class": "camposTesouroDireto"})
            for tr in trs:
                titulos.append(
                    "{0}{1}{2}".format(
                        tr[0].find("td").text,
                        tr[1].find("td").text,
                        tr[2].find("td").text)
                )
            return "\n".join(titulos)
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
