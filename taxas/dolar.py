# recupera cotação do dolar do dia
import os
import requests
import logging


logr = logging.getLogger(os.environ.get("LOG-NAME"))


class Dolar:

    def get(self):
        logr.info("INICIANDO CHAMADA AO SERVICO DE DOLAR")
        try:
            response = requests.get("http://api.dolarhoje.com")

            logr.info("DOLAR RECUPERADO COM SUCESSO R$ {0}.".format(response.text))
            return "R$ {0}".format(response.text)
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
