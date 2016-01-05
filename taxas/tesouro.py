# Recuperar taxas do tesouto direto.
import os
import requests
import logging
from bs4 import BeautifulSoup
from .taxa import Taxa

logr = logging.getLogger(os.environ.get("LOG-NAME"))

TESOURO_URL = "http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos"


class Tesouro(Taxa):

    def get(self):
        try:
            response = requests.get(TESOURO_URL)
            html = BeautifulSoup(response.content, 'html.parser')
            titulos = []
            trs = html.findAll("tr", {"class": "camposTesouroDireto"})

            for tr in trs:
                td = tr.findAll("td")
                titulos.append(
                    "{0} | C:{1}% V:{2}% ".format(
                        td[0].text,
                        td[2].text,
                        td[3].text)
                )
            return "\n".join(titulos)
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
