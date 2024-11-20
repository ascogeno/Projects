from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest 


def test_water_column_height():
    """Tests water column height function, makes sure it doesn't crash and burn"""
    wat = water_column_height(0,0)
    assert isinstance(wat,float), "water_column_height must return a float (hard to do the math with just ints)"

    assert water_column_height(0,0) == 0
    assert water_column_height(0,10) == 7.5
    assert water_column_height(25,0) == 25
    assert water_column_height(48.3,12.8) == 57.9

def test_pressure_gain_from_water_height():
    """Tests pressure_gain_from_water_height, makes sure it work good"""
    wat = pressure_gain_from_water_height(0)
    assert isinstance(wat,float), "pressure_gain_from_water_height must return a float (hard to do the math with just ints)"

    assert pressure_gain_from_water_height(0) == approx(0,abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628,abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450,abs=0.001)

def test_pressure_loss_from_pipe():
    """Tests pressure_loss_from_pipe, cause it makes a fuss sometimes"""
    pressed = pressure_loss_from_pipe(0.01,0,0,0)
    assert isinstance(pressed,float), "pressure_loss_from_pipe must return a float (ints have a hard time doing decimals)"

    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462,abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576,abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884,abs=0.001)

def test_pressure_loss_from_fittings():
    """Tests presuure_loss_from_fittings, they can be a real probelm child"""
    fit = pressure_loss_from_fittings(0.01,0.01)
    assert isinstance(fit,float), "pressure_loss_from_fittings must return a float (ints dont quite do the job)"

    assert pressure_loss_from_fittings(0, 3) == approx(0,abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0,abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109,abs=0.001) #this no work with 0.001???????
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122,abs=0.001) #this one too
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306,abs=0.001)

def test_reynolds_number():
    """Tests reynolds_number, Reynold doesn't like it when I give it out"""
    reyn = reynolds_number(0.0001,0)
    assert isinstance(reyn,float), "reynolds_number should return a float, it'd be weird if it didn't"

    assert reynolds_number(0.048692,0) == approx(0,abs=1)
    assert reynolds_number(0.048692,1.65) == approx(80069,abs=1)
    assert reynolds_number(0.048692,1.75) == approx(84922,abs=1)
    assert reynolds_number(0.28687,1.65) == approx(471729,abs=1)
    assert reynolds_number(0.28687,1.75) == approx(500318,abs=1)

def test_pressure_loss_from_pipe_reduction():
    """Tests pressure_loss_from_pipe_reduction. They're usually pretty good, but every other Thurday I tell ya..."""
    red = pressure_loss_from_pipe_reduction(0.1,0.1,0.1,0.1)
    assert isinstance(red,float), "pressure_loss_from_pipe_reduction needs to return a float. Idk what its doing if it doesn't"

    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182,abs=0.001)
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
