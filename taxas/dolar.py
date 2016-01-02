# recupera cotação do dolar do dia
import os
import requests
import logging
from .taxa import Taxa

logr = logging.getLogger(os.environ.get("LOG-NAME"))


class Dolar(Taxa):

    def get(self):
        logr.info("INICIANDO CHAMADA AO SERVICO DE DOLAR")
        try:
            response = requests.get("http://api.dolarhoje.com")
            value = response.text
            if not value:
                raise Exception("Valor nao existe.")

            logr.info("DOLAR RECUPERADO COM SUCESSO R$ {0}.".format(value))
            return "R$ {0}".format(value)
        except Exception as e:
            logr.error(e, exc_info=True)
            raise e
