from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Tests make_full_name, a real wild one this guy is"""

    assert make_full_name("","") == "; "
    assert make_full_name("","Kermit") =="Kermit; "
    assert make_full_name("Kermit","") =="; Kermit"
    assert make_full_name("Kermit2","Kermit1") == "Kermit1; Kermit2"


def test_extract_family_name():
    """Tests extract_family_name"""

    #assert extract_family_name("") == ""
    assert extract_family_name("Murray; ") == "Murray"


def test_extract_given_name():
    """Tests extract_given_name, sometimes they want it back and that causes issues"""
    assert extract_given_name("Brown; Sally") == "Sally"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

