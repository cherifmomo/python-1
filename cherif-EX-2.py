start = 1
end = 10000
 
for n in range(start, end+1):
    sum = 0

    for i in range(1, n):
        if n%i == 0:
            sum += i
    #print(n, sum)

    if n == sum:
        print(n)
