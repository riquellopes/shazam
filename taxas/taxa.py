# classe base na qual todos os tipos taxas implementadas devem herdar.
class Taxa:

    def get():
        raise Exception("Metodo não foi implementado.")


class Fabrica:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.build(kwargs.get("taxa"))
        return cls._instance

    @classmethod
    def destroy(cls):
        cls._instance = None

    @classmethod
    def build(cls, taxa):
        module = __import__("taxas.{0}".format(taxa))
        return getattr(module, taxa.title())()
