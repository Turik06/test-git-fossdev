# import sys 
# sys.path.append("../src")

# TODO make if with pip install -e .
#in project root_dir after setuo.py defined
from math_demo import add

def test_addition():
    assert 2+2 ==4
    print("Test ADDITION PASSED")

if __name__ == "__main__":
    test_addition()