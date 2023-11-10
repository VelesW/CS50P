from seasons import convert
import pytest

def test_convert():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(99) == "One hundred forty-two thousand, five hundred sixty minutes"

    with pytest.raises(ValueError):
        convert("2000:01:01")
    with pytest.raises(ValueError):
        convert("January, 1 2000")
