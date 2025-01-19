import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize(
    "input_str, expected_result", [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world")
    ]
)
def test_capitalize(input_str, expected_result):
    assert utils.capitalize(input_str) == expected_result 

@pytest.mark.parametrize(
    "input_str, expected_result", [
        (" hello", "hello"),
        (" Hello", "Hello"),
        (" Hello world", "Hello world"),
    ]
)
def test_trim(input_str, expected_result):
    assert utils.trim(input_str) == expected_result 
   
@pytest.mark.parametrize(
    "input_str, result", [
        ("hello,world", ["hello", "world"]),
        
    ]
)
def test_to_list(input_str, result):
    assert utils.to_list(input_str) == result
    

@pytest.mark.parametrize(
    "input_str, delimetr, result", [
       ("657:329:521", ":", ["657", "329", "521"])
   ]
)
def test_to_list(input_str, delimetr, result):
    assert utils.to_list(input_str, delimetr) == result 

@pytest.mark.parametrize(
    "input_str, symbol, expected_result", [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False)
    ]
)
def test_contains(input_str,symbol, expected_result):
    assert utils.contains(input_str, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky")
    ]
)
def test_delete_symbol(string, symbol, expected_result):
    assert utils.delete_symbol(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False)
    ]
)
def test_starts_with(string, symbol, expected_result):
    assert utils.starts_with(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, expected_result", [
        ("", True),
        (" ", True),
        ("SkyPro", False)
    ]
)
def test_is_empty(string, expected_result):
    assert utils.is_empty(string) == expected_result

@pytest.mark.parametrize(
    "lst, expected_result", [
        ("1,2,3,4", "1, 2, 3, 4"),
        (["Sky", "Pro"], "Sky, Pro"),
    #    (["Sky", "Pro"], "-", "Sky-Pro"),
    ]
)
def test_list_to_string(lst, expected_result):
    assert utils.list_to_string(lst) == expected_result

@pytest.mark.parametrize(
    "lst, joiner, expected_result", [
        (["Sky", "Pro"], "-", "Sky-Pro"),
        (["Вол", "го", "град"],"-", "Вол-го-град")
    ]
)
def test_list_to_string(lst, joiner, expected_result):
    assert utils.list_to_string(lst, joiner) == expected_result

