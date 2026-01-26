'''
WRiting a function that passes a credit card number and returns a masked num
wull only return the last 4 numbers

ex:
1234 1843 9843 1234 -> **** **** **** 1234
'''

str = "1234184398231234"

string_len = len(str)
mask = string_len - 4
#print(f"String Length: {string_len}")

showstring = str[mask:]

#print("*"* mask + showstring)

# Trying witha  function approach
def masking(number, mask):
    str_msk_hlder = ''
    n = mask
    for x in number[:-n]:
        str_msk_hlder += '*'
    str_msk_hlder += number[-n:]
    return str_msk_hlder

#print(masking("1234567982374316", 4))

#Using rjust
str = '1234567982374316'
x = str[-4:].rjust(len(str), "*")
#print(x)
#print(str[:4] + '*' * 8 + str[-4:])

#print('{:*>16}'.format(str[-4:]))
#complicated masking
def masking(number, start_num = 0, end_num =0, char="@"):
    number_len = len(number)
    mask_len = number_len - start_num - end_num
    return (number[:start_num]+(char*mask_len)+number[-end_num:])

#print(masking(str, 1, 4,char="*"))

#testing with regex
import re
print(re.sub('[0-9]', '*', str[4:]) + str[-4:])



