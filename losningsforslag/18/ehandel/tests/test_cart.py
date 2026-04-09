import pytest
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from src.cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

scenarios("../features/cart.feature")

# Skriv @scenario för varje scenario i feature-filen
# Skriv @given, @when, @then för varje steg
# Använd parsers.parse() för att extrahera parametrar

@given("att kundvagnen är tom")
def empty_cart(cart):
    assert cart.get_item_count() == 0

@when(parsers.parse('jag lägger till "{name}" med pris {price} kr'))
def add_item(cart, name, price):
    cart.add_item(name, float(price))

@then(parsers.parse('ska kundvagnen innehålla {count} vara'))
def check_item_count(cart, count):
    assert cart.get_item_count() == int(count)

@then(parsers.parse('ska kundvagnen innehålla {count} varor'))
def check_item_count(cart, count):
    assert cart.get_item_count() == int(count)

@then(parsers.parse('totalsumman ska vara {total} kr'))
def check_total(cart, total):
    assert cart.get_total() == float(total)


@given(parsers.parse('att kundvagnen innehåller "{name}" med pris {price} kr'))
def cart_with_item(cart, name, price):
    cart.add_item(name, float(price))

@when(parsers.parse('jag tar bort "{name}"'))
def remove_item(cart, name):
    cart.remove_item(name)

@when(parsers.parse('jag tillämpar rabattkoden "{code}"'))
def apply_discount(cart, code):
    cart.apply_discount(code)

@then(parsers.parse('ska totalsumman vara {total} kr'))
def check_total(cart, total):
    assert cart.get_total() == float(total)