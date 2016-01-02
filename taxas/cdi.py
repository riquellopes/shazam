# recupera cdi do dia.
import os
import requests
import logging
from bs4 import BeautifulSoup

logr = logging.getLogger(os.environ.get("LOG-NAME"))


class Cdi:

    def get(self):
        logr.info("INICIANDO CHAMADA AO SERVICO DE CDI")
        try:
            response = requests.get("https://www.cetip.com.br")
            html = BeautifulSoup(response.content, 'html.parser')
            cdi = html.find(id="ctl00_Banner_lblTaxDI").text

            logr.info("CDI RECUPERA COM SUCESSO.")
            return cdi
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
