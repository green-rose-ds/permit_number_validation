from permit_number_checker import permit_number_format

def test_py():
    assert 1+1 == 2

def test_permit_number_is_given_unhappy():
    assert permit_number_format("") == False   

def test_permit_number_is_8_characters_unhappy():
    assert permit_number_format("1234567") == False
    assert permit_number_format("123456789") == False 

def test_permit_number_is_alphanumerical_format_unhappy():
    assert permit_number_format("ab12345c") == False

def test_permit_number_is_accepted_happy():
    assert permit_number_format("ab1234cd") == True