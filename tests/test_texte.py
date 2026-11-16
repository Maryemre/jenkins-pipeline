import pytest
from app.texte import nettoyer_texte

@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("PYTHON", "python"),
])

def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

def test_texte_nombre():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)

def test_nettoyer_texte_idempotent():
    texte = "  BONJOUR   monde  "

    resultat1 = nettoyer_texte(texte)
    resultat2 = nettoyer_texte(resultat1)

    assert resultat1 == resultat2
    