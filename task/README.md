### Задание №1 Проверка зависимостей

Для проверки недостающих и лишних зависимостей мы использовали инструмент deptry, который в автоматическом режиме проверяет все импорты и файлы типа requirements.txt/pyproject.toml

в тестовом файле service.py указаны следующие импорты:
```python
import requests
import numpy
import fastapi
```

в requirements.txt указаны следующие библиотеки
```
numpy
mypy
```
по итогу вывод команды "make check-deps" будет таким:

```
requirements.txt: DEP002 'mypy' defined as a dependency but not used in the codebase
src/service.py:1:8: DEP001 'requests' imported but missing from the dependency definitions
src/service.py:3:8: DEP001 'fastapi' imported but missing from the dependency definitions
Found 3 dependency issues.
```
deptry указывала, что mypy является лишней в requirements.txt, а requests и fastapi - наоборот, не хватает.


### Задание №3 Проверка типов 

В проект внедрён инструмент mypy для анализа аннотаций типов. Это позволяет отловить ошибки типизации на этапе сборки, не запуская само приложение. 

Создан target typecheck, который: 
запускает из виртуального окружения по пути `$(MYPY)` (`.venv/bin/mypy`). 

Target зависит от `$(INSTALLED_FLAG)`. Если окружение не развернуто, Make сначала создаст `.venv` и установит mypy, а только потом запустит проверку. 

В файле `src/calc.py` была намеренно допущена ошибка: 

```python
result: int = add(2, "3") # Ошибка: ожидается int, передана str

При запуске команды make typecheck анализатор корректно прерывает выполнение с ошибкой:

    src/calc.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
```
Это предотвращает попадание некорректного кода в основную ветку репозитория.

### Задание №4: Проверка стилей

В проект внедрен инструмент **pycodestyle**. Он работает в режиме проверки: выявляет нарушения стандартов оформления и сообщает о них, не изменяя исходный код принудительно. Это соответствует принципу осознанной разработки.

В Makefile создан абстрактный target `lint`. При его выполнении система анализирует файл `src/example.py` и выводит список диагностированных ошибок:

```text
src/example.py:1:9: E201 whitespace after '('
src/example.py:1:11: E231 missing whitespace after ','
src/example.py:1:13: E202 whitespace before ')'
src/example.py:2:2: E111 indentation is not a multiple of 4
```


### Задание №5: Цепочки

В финальном задании все проверки объединены в target `check`. Особенность реализации заключается в том, что Make выстраивает строгую последовательность выполнения. 

**Пример из практики**
При запуске `make check` первым выполняется `typecheck`.Как видно из вывода терминала, инструмент обнаружил несоответствие типов в файле src/calc.py.

Так как была обнаружена ошибка, Make немедленно прервал выполнение всей цепочки.