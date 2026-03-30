# tests/test_ndfl.py

import pytest
from ndfl import calculate_ndfl

def test_ndfl_tier_1_basic():
    assert calculate_ndfl(2_000_000) == 260_000

def test_ndfl_tier_2_basic():
    assert calculate_ndfl(4_000_000) == 552_000

def test_ndfl_tier_3_basic():
    assert calculate_ndfl(10_000_000) == 1_602_000

def test_ndfl_tier_4_basic():
    assert calculate_ndfl(30_000_000) == 5_402_000

def test_ndfl_tier_5_basic():
    assert calculate_ndfl(60_000_000) == 11_602_000

@pytest.mark.xfail
def test_ndfl_fails_negative_income():
    calculate_ndfl(-1_000)