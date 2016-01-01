# recupera cotação do dolar do dia
import requests


class Dolar(object):

    def get(self):
        response = requests.get("http://api.dolarhoje.com/")
        return "R$ ".format(response.text)
