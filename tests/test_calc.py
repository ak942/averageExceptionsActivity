import pytest 

from average_calculator.calc import rounded_average

# @pytest.mark.skip
def test_average_of_two_numbers_is_properly_computed():
    #act
    average = 5

    #arrange
    actual = rounded_average([4, 6])
    
    #assert
    assert average == actual    



# @pytest.mark.skip
def test_average_of_empty_list_raises_ValueError():
    # Delete the skip and write the test here!
    # Hint: use pytest.raises
    with pytest.raises(ValueError):
        rounded_average([])
    
