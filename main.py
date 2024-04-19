def sum_str(str1, str2):
    if not str1.isnumeric() or not str2.isnumeric():
        raise Exception("Can't use sum_str because there is a non numeric char")
    if len(str2)== 0 or len(str1) == 0:
        return '0'
    if len(str2) > len(str1):  # I want to keep len(str1)> len(str2)
        str1,str2 = str2,str1
        # In cpp I just could do it with temp varf

    carry = 0
    diff = len(str1) - len(str2)
    str_output = []
    for i in range(len(str2) - 1, -1, -1):
        char_sum = int(str1[i+diff]) + int(str2[i]) + carry # len(str1) > len(str2)
        str_output.insert(0,str(char_sum%10)) # For example: 15 % 10 = 5, 1 for carry
        carry = char_sum // 10
    for i in range(diff - 1,-1,-1):
        # now I will deal with the remaining carry if it exist
        char_sum = int(str1[i]) + carry
        # yay its actually working. when we insert to the list, we actually adding 1 more bit as needed.
        str_output.insert(0, str(char_sum % 10))  # For example: 15 % 10 = 5, 1 for carry
        carry = char_sum // 10
    if carry != 0:
        str_output.insert(0,str(carry))  # For example: 15 % 10 = 5, 1 for carry
    return ''.join(str_output)


sum1 = sum_str("999999999999999999999999999999999999999", "999999999999999999999999999999999999999")

print(sum_str(sum1,"999999999999999999999999999999999999999"))

num = 999999999999999999999999999999999999999 + 999999999999999999999999999999999999999 + 999999999999999999999999999999999999999
print(num)