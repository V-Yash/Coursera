n = int(input())
count = 0
for i in [10, 5, 1]:
    if n>=i:
        q = n//i
        print("first",q)
        count += q
        n = n%i
        print("second",n)
        if n==0:
            print(count)
            quit()