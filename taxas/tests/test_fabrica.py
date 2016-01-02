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
