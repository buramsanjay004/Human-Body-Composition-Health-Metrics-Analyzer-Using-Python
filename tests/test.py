import pytest
from body import bmi,whr,wht_ratio, bmi_category, diet_suggestion
def test_bmi():
    assert(85,165) == 31.22