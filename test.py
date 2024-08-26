import pytest
import myfile

def test_num1():
    assert myfile.sum1(10,5) == 15
def test_num2():
    assert myfile.sum1(10,4) == 14
