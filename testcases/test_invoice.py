from src.invoice import get_last_n_digits,get_max_match_for_win_mun

def test_get_last_3_digit():
    ticket='94899145'
    last_3_digit=get_last_n_digits(ticket,3)
    assert last_3_digit=='145'

def test_get_last_8_digit():
    ticket='94899145'
    last_8_digit=get_last_n_digits(ticket,8)
    assert last_8_digit=='94899145'

def test_max_3_match():
    ticket = '94899145'
    win_num = '94898145'
    max_match = get_max_match_for_win_mun(ticket,win_num)
    assert max_match == 3

def test_no_match():
    ticket = '94899045'
    win_num = '94898145'
    max_match = get_max_match_for_win_mun(ticket,win_num)
    assert max_match == 0

def test_max_8_match():
    ticket = '94898145'
    win_num = '94898145'
    max_match = get_max_match_for_win_mun(ticket,win_num)
    assert max_match == 8  