import pytest
from weather import get_weather

def test_get_weather():
    assert get_weather(21)=='hot'
    assert get_weather(10)=='hot', 'it is a corner case'
    assert get_weather(15)=='cold'

