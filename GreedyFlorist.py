
N, K = raw_input().split()
N = int(N)
K = int(K)

numbers = map(int, raw_input().split())

numbers = sorted(numbers, reverse = True)
total = 0
const = 1
while len(numbers) > K:
    total += const * sum(numbers[:K])
    numbers = numbers[K:]
    const += 1
total += const * sum(numbers)
    
    
print total
