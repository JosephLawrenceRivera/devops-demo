# test_calc.py
git config --global user.name "JosephLawrenceRivera"
git config --global user.email "josephlawrence.rivera@my.jru.edu"
from calc import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
