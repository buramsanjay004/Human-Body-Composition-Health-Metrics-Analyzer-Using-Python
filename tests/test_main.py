import pytest
from body import bmi, whr, wht_ratio, bmi_category, diet_suggestion

def test_bmi():
    assert bmi(85, 165) == 31.22

def test_whr():
    assert whr(80, 100) == 0.8

def test_bmi_category():
    assert bmi_category(22) == "Normal Weight"