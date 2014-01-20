testCases = eval(input())
output = 0

while testCases:
    testCases -= 1
    tmp = 0
    k, n = input().split()
    n = int(n)
    k = int(k)
    if n == 1:
        print("Male")
    else:
        if n == 2:
            print("Female")
        else:
            n -= 1
            while n > 1:
                if n % 2 != 0:
                    tmp += 1
                n //= 2     #truncated division
            if tmp % 2 == 0:
                print("Female")
            else:
                print("Male")