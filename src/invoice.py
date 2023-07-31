winning_number=['94899145','71143793','41055355']
# Unit test
def get_last_n_digit(ticket,n):
    #假設給定一組號碼，回傳最後n碼，
    #例如get_last_n_digit('94899145',3)會回傳'145'
    #例如get_last_n_digit('94899145',5)會回傳'99145'
    return ticket[-n:]

if __name__=='__main__':
    ticket='94899145'
    last_4_digit=get_last_n_digit(ticket,4)
    print(last_4_digit)
    assert last_4_digit=='9145'
# 主要用來檢查程式碼是否有誤，若有誤則會報錯(利用assert回報錯誤，正確則不會回報錯誤)
