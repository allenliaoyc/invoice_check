winning_number=['94899145','71143793','41055355']
# Unit test
def get_last_n_digits(ticket,n):
    #假設給定一組號碼，回傳最後n碼，
    #例如get_last_n_digit('94899145',3)會回傳'145'
    #例如get_last_n_digit('94899145',5)會回傳'99145'
    return ticket[-n:]

def get_max_match_for_win_mun(ticket,win_num):
    match_count = 0 #最大相同數字個數
    for i in range(3,9):
        t = get_last_n_digits(ticket,i)
        w = get_last_n_digits(win_num,i)
        if t==w:
            match_count=i
        else:
            break
    return match_count
