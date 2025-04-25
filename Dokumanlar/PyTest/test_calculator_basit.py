# Pytest ile basit test örneği

from calculator import topla, cikar, carp, bol

# Test fonksiyonları 'test_' öneki ile başlamalıdır

def test_topla():
    assert topla(3, 5) == 8
    assert topla(-1, 1) == 0
    assert topla(-1, -1) == -2

def test_cikar():
    assert cikar(5, 3) == 2
    assert cikar(1, 5) == -4

def test_carp():
    assert carp(3, 5) == 15
    assert carp(-1, 5) == -5
    assert carp(-1, -1) == 1

def test_bol():
    assert bol(10, 2) == 5
    assert bol(5, 2) == 2.5