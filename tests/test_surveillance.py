import pytest
from unittest.mock import patch

from app.surviel import surveiller

def test_surveiller_alerte():
    with patch("app.surviel.envoyer_notification") as notifier:

        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")

def test_surveiller_ok():
    with patch("app.surviel.envoyer_notification") as notifier:

        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_surveiller_limite():
    with patch("app.surviel.envoyer_notification") as notifier:

        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_surveiller_erreur():
    with patch("app.surviel.envoyer_notification") as notifier:
        notifier.side_effect=RuntimeError("Service non configure")
        with pytest.raises(RuntimeError):
            surveiller(0.15)