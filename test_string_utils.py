import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize(
    "input_str, expected_result", [
        ("время", "Время"),
        ("Laptop", "Laptop"),
        ("white snow", "White snow"),
        ("12345", "12345")
    ]
)
def test_capitalize_positive(input_str, expected_result):
    assert utils.capitalize(input_str) == expected_result 

@pytest.mark.parametrize(
    "input_str, expected_result",
    [("", ""), ("    ", "    "), 
     #(None)
    ]
)
def test_capitalize_negative(input_str, expected_result):
    assert utils.capitalize(input_str) == expected_result
with pytest.raises(TypeError):
    test_capitalize_negative (None)


@pytest.mark.parametrize(
    "input_str, expected_result", [
        (" время", "время"),
        (" Laptop", "Laptop"),
        (" White snow", "White snow"),
        (" 12345", "12345")
    ]
)
def test_trim_positive(input_str, expected_result):
    assert utils.trim(input_str) == expected_result

@pytest.mark.parametrize(
    "input_str, expected_result", [
        ("", ""), ("    ", "") 
    ]
)
def test_trim_negative(input_str, expected_result):
    assert utils.trim(input_str) == expected_result 
   
@pytest.mark.parametrize(
    "input_str, result", [
        ("hello,world", ["hello", "world"]),
        ("время, Laptop", ["время", "Laptop"]),
        ("White snow", ["White", "snow"]),
        ("12345, 67889", ["12345", "67889"]),
    ]
)
def test_to_list_positive(input_str, result):
    assert utils.to_list(input_str) == result

@pytest.mark.parametrize(
    "input_str, result", [
        ("", []), ("    ", [    ]) 
    ]
)
def test_to_list_negative(input_str, result):
    assert utils.to_list(input_str) == result


@pytest.mark.parametrize(
    "input_str, delimetr, result", [
       ("657:329:521", ":", ["657", "329", "521"])
   ]
)
def test_to_list_positive(input_str, delimetr, result):
    assert utils.to_list(input_str, delimetr) == result

@pytest.mark.parametrize(
    "input_str, delimetr, result", [
        ("",":", []), ("    ",":", [    ]) 
    ]
)
def test_to_list_negative(input_str, delimetr, result):
    assert utils.to_list(input_str, delimetr) == result 

@pytest.mark.parametrize(
    "input_str, symbol, expected_result", [
        ("Laptop", "L", True),
        ("Snow", "U", False),
        ("12345", "1", True),
        ("12345", "6", False),
        ("White snow", "hit", True),
        (" Зеленая роща", "ая р", True)
    ]
)
def test_contains_positive(input_str,symbol, expected_result):
    assert utils.contains(input_str, symbol) == expected_result

@pytest.mark.parametrize(
    "input_str, symbol, expected_result", [
        ("", "", True),
        ("    ", ":", False) 
    ]
)
def test_contains_negative(input_str,symbol, expected_result):
    assert utils.contains(input_str, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("время", "р", "вемя"),
        ("Laptop", "top", "Lap"),
        ("White snow", "White", " snow"),
        ("12345", "23", "145"),
        ("2 августа 1972", "августа", "2  1972")
    ]
)
def test_delete_symbol_positive(string, symbol, expected_result):
    assert utils.delete_symbol(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("","", ""),
        ("    ","", "    ") 
    ]
)    
def test_delete_symbol_negative(string, symbol, expected_result):
    assert utils.delete_symbol(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("Laptop", "L", True),
        ("Laptop", "t", False),
        ("12345", "1", True),
        ("12345", "3", False),
        ("White snow", "White", True),
        ("White snow", "snow", False)
    ]
)
def test_starts_with_positive(string, symbol, expected_result):
    assert utils.starts_with(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, symbol, expected_result", [
        ("","", True),
        ("    ","     ", False) 
    ]
)   
def test_starts_with_negative(string, symbol, expected_result):
    assert utils.starts_with(string, symbol) == expected_result

@pytest.mark.parametrize(
    "string, expected_result", [
        ("", True),
        (" ", True),
        ("Snow", False),
        ("12345", False)
    ]
)
def test_is_empty(string, expected_result):
    assert utils.is_empty(string) == expected_result


@pytest.mark.parametrize(
    "lst, expected_result", [
        ("1234", "1, 2, 3, 4"),
        ("1,2,3,4", "1, ,, 2, ,, 3, ,, 4"),
        (["Lap", "Top"], "Lap, Top"),
        ("White snow", "W, h, i, t, e,  , s, n, o, w")
    ]
)
def test_list_to_string_positive(lst, expected_result):
    assert utils.list_to_string(lst) == expected_result

@pytest.mark.parametrize(
    "lst, expected_result", [
               ("", ""),
        ("    ", " ,  ,  ,  ") 
    ]
)
def test_list_to_string_negative(lst, expected_result):
    assert utils.list_to_string(lst) == expected_result

@pytest.mark.parametrize(
    "lst, joiner, expected_result", [
        (["Lap", "Top"], "-", "Lap-Top"),
        (["Вол", "го", "град"],"-", "Вол-го-град"),
        
    ]
)
def test_list_to_string_positive(lst, joiner, expected_result):
    assert utils.list_to_string(lst, joiner) == expected_result

