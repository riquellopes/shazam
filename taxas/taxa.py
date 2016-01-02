# classe base na qual todos os tipos taxas implementadas devem herdar.
import os
import logging
logr = logging.getLogger(os.environ.get("LOG-NAME"))


class Taxa:

    def get(self):
        raise Exception("Metodo não foi implementado.")


class Fabrica:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            logr.info("INICIANDO BUILD")
            cls._instance = cls.build(kwargs.get("taxa"))
        return cls._instance

    @classmethod
    def destroy(cls):
        logr.info("DESTRUINDO BUILD")
        cls._instance = None

    @classmethod
    def build(cls, taxa):
        module = __import__("taxas.{0}".format(taxa))
        klass = getattr(module, taxa.title())
        cls.validate(klass)
        return klass()

    @classmethod
    def validate(cls, klass):
        if not issubclass(klass, Taxa):
            raise Exception("Classe não é valida.")
