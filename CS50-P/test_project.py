from project import userinput
from project import input_check

def test_userinput():
    assert userinput() == str


def test_input_check():
    assert input_check("all", 10000, 10000, 2015) == True
