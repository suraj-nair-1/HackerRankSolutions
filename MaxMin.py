N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
min_diff = float("inf") ## Write code here to compute the answer using (n, k, candies)
for i in range(0, len(lists) - K + 1):
    min_diff = min(min_diff, lists[i + K - 1] - lists[i])
    

print min_diff
