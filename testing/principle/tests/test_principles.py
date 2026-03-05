# import sys 
# sys.path.append("../src")

# TODO make if with pip install -e .
#in project root_dir after setuo.py defined
#[DONE]Раннее тестирование позволяет сэкономить время позднее
#[DONE] Тесты показывают наличие ошибок, а не отсутсвие

#[DONE] Тесты не должны дублировать логику тестируемого кода
#и не делать предположений о внутреннем устройстве кода

# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import (add,
                       add_with_bug)

def test_addition():
    assert add(2,2) ==4
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2,2) ==4
    assert add_with_bug(0,0) ==0
    print("Test BUGGED ADDITION PASSED")
    # finally we found data thet make test reliable
    # assert add_with_bug(7,6) ==13 #will fail here

def test_addition_duplicate():
    assert add(6,7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()