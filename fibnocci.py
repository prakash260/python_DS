def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    parent = 1
    grandparent = 0
    
    for _ in range(2, n+1):
        curr = parent + grandparent
        grandparent = parent
        parent = curr
    
    return parent