import pytest
from predictor import Predictor


@pytest.mark.parametrize("payload", [({"text": "Hello and Happy Trading!", "top_n": "3", "emojize": "true"})])
def test_get_parameters(payload: dict) -> None:
    """
    Tests Predictor.predict() with full payload options.
    """
    result = Predictor._get_parameters(payload)
    assert result == ("Hello and Happy Trading!", 3, True)