# Recuperar taxas do tesouto direto.
from .taxa import Taxa


class TesouroDireto(Taxa):

    def get(self):
        super(TesouroDireto, self).get()
