import pytest
from app.moderation import decider
from unittest.mock import Mock
from app.moderation import decider



def test_decider_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_normal():
    modele=Mock()
    modele.predict.return_value="normal"
    resultat=decider(modele,"Bonjour")
    assert resultat=="autoriser"

def test_decider_erreur():
    modele = Mock()

    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError):
        decider(modele, "Offre miracle")