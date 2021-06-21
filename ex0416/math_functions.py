
def fib(n):
    Dict={0:0, 1:1}
    if n not in Dict:
        val=fib(n-1)+fib(n-2)
        Dict[n]=val
    return Dict[n]

