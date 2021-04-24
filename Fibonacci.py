# 1. using recurrsion

def fib(n):
    f1 = 0;
    f2 = 1;
    if(n<0):
        print("incorrect input");
    if n==1:
        return f1
    elif n==2:
        return f2
    else:
        return fib(n-1) + fib(n-2)

print(fib(5));

# 2. Dynamic programming

def fib2(n):
    f = [0,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    print(f[n-1])
    return f

fib2(5)