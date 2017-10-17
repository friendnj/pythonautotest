def test(num):
    if num >1:
        result =num*test(num-1)
    else:
        result=1
    return result
result=test(4)
print("result=%d"%result)
