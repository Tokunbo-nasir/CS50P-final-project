from project import userinput
from project import input_check
from project import upload
import pytest

def test_userinput():
    assert userinput() == str


def test_input_check():
    assert input_check("all", 10000, 10000, 2015) == True

def test_upload():
    with pytest.raises(TypeError):
        upload()
    