import pytest
from prime import isPrime

@pytest.mark.parametrize("number, expected, raises",[
    (1, False,None),
    (2, True,None),
    (13,True,None),
    (20,False,None),
    (-1,None,ArithmeticError)
])
def test_is_prime(number,expected,raises):
    if raises:
        with pytest.raises(ArithmeticError,match='No Negative Number'):
            isPrime(number)
    else:   assert isPrime(number)==expected