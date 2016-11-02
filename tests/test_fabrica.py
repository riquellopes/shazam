import pytest
from taxas import Fabrica, Selic, Dolar


def test_carrega_selic():
    fabrica = Fabrica(taxa="selic")
    assert isinstance(fabrica, Selic)


def test_carrega_dolar():
    Fabrica.destroy()
    fabrica = Fabrica(taxa="dolar")
    assert isinstance(fabrica, Dolar)


def test_erro_taxa_merda():
    Fabrica.destroy()
    with pytest.raises(Exception):
        (Fabrica(taxa="merda"))


def test_classe_nao_valida():
    class Qualquer:
        pass
    with pytest.raises(Exception) as e:
        Fabrica.validate(Qualquer)
    assert str(e.value) == "Classe não é valida."
