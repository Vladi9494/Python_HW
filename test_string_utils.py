from typing import Literal
import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("123456", "123456"),    
    ("04 апреля 2025", "04 апреля 2025")
])
def test_capitalize_positive(input_str: Literal['skypro']
                             | Literal['hello world'] | Literal['python']
                             | Literal['тест'] | Literal['123456']                             
                             | Literal['04 апреля 2025'],
                             expected: Literal['Skypro']
                             | Literal['Hello world'] | Literal['Python']
                             | Literal['Тест'] | Literal['123456']
                             | Literal['04 апреля 2025']):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # цифры вместе с буквами на латинице
    (123456, 123456),  # Цифровое значение.
    "sky"123, "Sky"123),  # Строка и цифры.
    ("эюя456", "Эюя456"),  # буквы на кириллице вместе с цифрами
    ("", ""),  # пустая строка
    ("   ", "   "),  # строка с пробелами
    ("[]", "[]")  # пустой список
])
def test_capitalize_negative(input_str: Literal['123abc']
                             | Literal[123456] | Literal['Sky123']
                             | Literal[''] | Literal['   '],
                             expected: Literal['123abc']
                             | Literal[123456]
                             | Literal[''] | Literal['   ']):
    assert string_utils.capitalize(input_str) == expected

########################


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),  # Строка в нижнем регистре.
    ("    SKYPRO", "SKYPRO"),  # Строка в верхнем регистре.
    ("  123", "123"),  # Число как строка.
    ("   Тест", "Тест"),  # Не пустая срока.
    ("    4 апреля 2023", "4 апреля 2023"),  # Строка с пробелами, цифры и
                                             # буквы на кириллице.
    ("       07_november_1917", "07_november_1917"),  # Далее - очень длинная
                                                      # строка с пробелами ↓
    ("                                                            456", "456"),
    ("                      🫡🙂☺️🤔", "🫡🙂☺️🤔"),  # Строка со знаками эмодзи.
    ("   (❁´◡`❁)¥©←ヾ(≧▽≦*)o", "(❁´◡`❁)¥©←ヾ(≧▽≦*)o")  # Строка с символами.
])
def test_trim_positive(input_str: Literal[' skypro'] | Literal['    SKYPRO']
                       | Literal['  123'] | Literal['   Тест']
                       | Literal['    4 апреля 2023']
                       | Literal['       07_november_1917']
                       | Literal['                        🫡🙂☺️🤔']
                       | Literal['      (❁´◡`❁)¥©←🚲🚂ヾ(≧▽≦*)o'],
                       expected: Literal['skypro'] | Literal['SKYPRO']
                       | Literal['123'] | Literal['Тест']
                       | Literal['4 апреля 2023']
                       | Literal['07_november_1917']
                       | Literal['456'] | Literal['🫡🙂☺️🤔']
                       | Literal['(❁´◡`❁)¥©←🚲🚂ヾ(≧▽≦*)o']):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [ 
    ("  123abc", "123abc"),  # Цифры вместе с латинскими буквами.
    (  123456, 123456),  # Цифровые значения.
      "АБВ"123, "АБВ"123),  # Буквы и цифры вместе.
    ("   ", ""),  # Пустая строка.
    ("   []", "[]")  # Пустой список.  
])
def test_trim_negative (input_str: Literal['  123abc']
                       | Literal[  123456] | Literal[  "АБВ"123],
                       expected: Literal['123abc'] | Literal[123456]
                       | Literal["АБВ"123] | Literal['']
                       | Literal['[]']):
    assert string_utils.trim(input_str) == expected

########################
# | Literal['   '] | Literal['   []'],
#("" + None, None), Ошибка: Нельзя склеить строку "" и значение None
#    ("  None", "None") или ("" + "None", "None"):
                        # None превращается просто в слово "None",
                        # а не в значение None???
    # ("", "") или ("" + "", "")  Строка с пробелом
    # (ошибка:для осуществления данной функции, нужно
    # применять дополнительное экранирование с помощью repr())???

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("SkyPro", "P", True),
    ("SkyPro", "p", False),  # Искомый символ не в том регистре.
    ("SkyPro", "U", False),  # Не верный искомый символ.
    ("skypro", "pro", True)  # Слитный символ идущий
                             # в том порядке как написан.
])
def test_contains_positive(string, symbol, result):
    lokal_string_utils = StringUtils()
    res = lokal_string_utils.contains(string, symbol)
    assert res == result


@pytest.fixture
@pytest.mark.negative
@pytest.mark.paramerize("string, symbol, result", [
    ("огород", "огород", True),
    ("машина", " ", False),
    (123456, 123456, True),  # Цифровое значение.
    (20"SkyPro"25, 20"SkyPro"25, True),  # Цифры и буквы вместе.
    ("огород", "дорого", False),  # Слитные символы не распознаются как
                                  # присутствующие, если идут не в том порядке
                                  # как написаны изначально.
#   ("огород", "ооо", False),      Слитный символ распознается как
                                  # присутствующий, только если написан, в том
                                  # порядке в котором написан изначально.
    ("Машина", " М", False),   # Символ не распознается как ↓
    ("машина", "м а", False),  # присутствующий, если написан с пробелом.
    ("машина", "машинаа", False)  # Слитный символ с ошибкой
                                  # в одну букву по длине.
])
def test_contains_negative(string, symbol, result):
    lokal_string_utils = StringUtils()
    res = lokal_string_utils.contains(string, symbol)
    assert res == result

########################


@pytest.fixture
@pytest.mark.positive
@pytest.mark.parametrize("input_string, input_symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Один символ на латинице внутри строки
    ("SkyPro", "Sky", "Pro"),  # Символ состоящий из трех букв в конце строки
    ("Hello world", "Hello", "world"),  # Слитный символ в начале строки
    ("Python ", "Python", " "),  # Строка с пробелом в конце строки
    ("Тест", "Тест", ""),  # Символ на кириллице равен строке
    ("123456", "2345", "16"),  # Строка состоящая из цифр
    ("04 апреля 2025", "апреля", "04  2025")  # Строка включающая пробелы
    ])
def test_delete_symbol_positive(input_str: Literal['SkyPro']
                                | Literal['Hello world'] | Literal['Python ']
                                | Literal['Тест'] | Literal['123456']
                                | Literal['04 апреля 2025'],
                                input_symbol: Literal['k'] | Literal['Sky']
                                | Literal['Hello'] | Literal['Python']
                                | Literal['Тест'] | Literal['2345']
                                | Literal['апреля'],
                                expected: Literal['SyPro'] | Literal['Pro']
                                | Literal['world'] | Literal[' ']
                                | Literal[''] | Literal['16']
                                | Literal['04  2025']):
    assert string_utils.delete_symbol(input_str) == expected
#   return fixture_marker(fixture_function)


@pytest.fixture
@pytest.mark.negative
@pytest.mark.parametrize("input_string, in put_symbol, expected", [
    ("Sky123", "y1", "Sk23"),  # буквы вместе с цифрами, как строка
    (201"SkyPro"125, 1"SkyPro"1, 2025),  # Цифры и буквы вместе.
    ("      ", "  ", "    "),  # строка и символ состоящие из одних пробелов
    ("", "", ""),  # пустая строка
    (None, None, None),  # проверка на пустое значение "None"
    (123456, 2345, 16),  # только цифровые значения
    # (😊😒🤣🤔😕🙃, 😒🤣🤔😕🙃, 😊), строка и символ состоящие
                                           # из эмодзи не как строка
                                           # (без кавычек)
    ("✍️: 👌 или конечно лучше: 👍",  "✍️: 👌 или конечно лучше:", "👍")
])
def test_delete_symbol_negative(input_str: Literal['Sky123']
                                | Literal[201'SkyPro'125]
                                | Literal['      '] | Literal['']
                                | Literal[None] | Literal[123456]
                                | Literal[😊😒🤣🤔😕🙃]
                                | Literal['✍️: 👌 или конечно лучше: 👍'],
                                input_symbol: Literal['y1']
                                | Literal [1'SkyPro'1]
                                | Literal['  '] | Literal['']
                                | Literal[None] | Literal[2345]
                                | Literal[😒🤣🤔😕🙃]
                                | Literal['✍️: 👌 или конечно лучше:'],
                                expected: Literal['Sk23'] | Literal[2025]
                                | Literal['    '] | Literal['']
                                | Literal[None] | Literal[16]
                                | Literal[😊]
                                | Literal['👍']):
    assert string_utils.delete_symbol(input_str) == expected
#   return fixture_marker(fixture_function)