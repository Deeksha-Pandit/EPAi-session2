import math
import random
import pytest
import os
import re
import inspect
import session5

README_CONTENT_CHECK_FOR = [
    'time_it',
    'print',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
    'math'
    'square'
    'time'
    'temperature'
    'converter'
    'speed'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_time_it_print():
    assert session5.time_it(session5.print_func, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5), "You do not even know how to print!!!"

def test_squared_power_list():
    assert session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitons=5), "Please square correctly"

def test_polygon_area():
    assert session5.time_it(session5.polygon_area, 15, sides = 3, repetitons=10), "Poor at math, please calculate it again"

def test_temp_converter():
    assert session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitons=100), "It's wither too hot or too cold"

def test_speed_converter():
    assert session5.time_it(session5.speed_converter, 100, dist='km', time='m', repetitons=200), "You are either too fast or too slow"

def test_repetitons_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.print_func, 1, 2, 3, sep='-', end= ' ***\n', repetitons=0)

def test_squared_power_list_start_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list, 2, start=-5, end=5, repetitons=5)

def test_squared_power_list():
    num = random.randint(1,10)
    first = 0#random.randint(0,5)
    last = 5#random.randint(5,10)
    list_one =[]
    for i in range(first,last+1):
        num = math.pow(num,i)
        list_one.append(num)
    assert session5.squared_power_list(num,first,last) == list_one, "Wrong square power list :("

def test_polygon_area_side_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, sides = 1, repetitons=10)

def test_polygon_area_length_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, -9, sides = 1, repetitons=10)

def test_polygon_area_square():
    len = 15
    res = session5.polygon_area(len, sides = 4)
    result = len * len
    assert int(res) == int(result), "Wrong calculation of area of a square"

def test_temp_converter_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, temp_given_in = 'e', repetitons=100)

def test_temp_converter_f():
    res1 = session5.temp_converter( 100, temp_given_in = 'f')
    f1 = ((100-32) * (5/9))
    assert (res1) == f1, "You are wrong"

def test_temp_converter_c():
    res2 = session5.temp_converter( 100, temp_given_in = 'c')
    c2 = ((100 * 9/5) + 32)
    assert res2 == c2, "You are wrong"

def test_speed_converter_error():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, -6, dist='km', time='m', repetitons=200)

def test_speed_converter_km_hr():
    res = session5.speed_converter( 100, dist='km', time='hr')
    assert res == 100, "Please calculate speed correctly"

def test_speed_converter_km_day():
    res = session5.speed_converter( 100, dist='km', time='day')
    assert res == 2400, "Please calculate speed correctly"

def test_speed_converter_m_m():
    res = session5.speed_converter( 100, dist='m', time='m')
    assert int(res) == 1666, "Please calculate speed correctly"

def test_speed_converter_ft_day():
    res = session5.speed_converter( 100, dist='ft', time='day')
    assert int(res) == 7874016, "Please calculate speed correctly"

def test_speed_converter_yrd_hr():
    res = session5.speed_converter( 100, dist='yrd', time='hr')
    assert int(res) == 109360, "Please calculate speed correctly"