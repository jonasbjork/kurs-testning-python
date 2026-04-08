import pytest
from pytest_bdd import scenario, given, when, then, parsers
from src.cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

# Skriv @scenario för varje scenario i feature-filen
# Skriv @given, @when, @then för varje steg
# Använd parsers.parse() för att extrahera parametrar
