import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def SnakeCase(col):
    if col[0].isupper():
        is_upper = True
    else: is_upper = False

    result = []
    # Aa
    for char in col:
        # aA -> a + _A
        if char.isupper() and not is_upper:
            result.extend(["_", char.lower()])
            is_upper = True
        # Aa -> a+_ +a
        elif char.islower() and is_upper:
            last_char = result.pop()
            result.extend(["_" ,last_char ,char.lower()])
            is_upper = False
        else:
            result.append(char.lower())

    if result[0] == '_':
        result = result[1:]

    return "".join(result)

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    data=data[(data['passenger_count']!=0) & (data['trip_distance']!=0)]
    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data.lpep_pickup_datetime = pd.to_datetime(data.lpep_pickup_datetime)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    data.columns=[SnakeCase(col)for col in data.columns]  
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_passenger(output, *arg) -> None:
    """
    Add three assertions:passenger_count is greater than 0
    """
    assert len(output[output['passenger_count'] == 0]) == 0, 'passenger_count = 0'

@test
def test_distance(output, *arg) -> None:
    """
    Add three assertions:trip_distance is greater than 0

    """
    assert len(output[output['trip_distance'] == 0]) == 0, "trip_distance = 0"
