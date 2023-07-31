from src.invoice import get_last_n_digit

def test_get_last_3_digit():
    ticket='94899145'
    last_3_digit=get_last_n_digit(ticket,3)
    assert last_3_digit=='145'

def test_get_last_8_digit():
    ticket='94899145'
    last_8_digit=get_last_n_digit(ticket,8)
    assert last_8_digit=='94899145'