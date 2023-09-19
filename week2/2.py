def factorial(n):
    if n == 0:
        return [1]
    
    nums = [1 for i in range(n)]
    for i in range(1, n):
        nums[i] *= nums[i-1]*(i+1)
    
    return nums
        
def calculate(N):
    arr = [1 for i in range(N+1)]
    fact_nums = factorial(N)
    for n in range(1, N+1):
        arr[n] = 2*n*fact_nums[n-1]
    print(*arr, sep=" + ")
    return sum(arr)

print(calculate(int(input())))