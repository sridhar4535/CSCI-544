def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
 return memo[arg]

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

fibm = memoize(fib,3)
print fibm