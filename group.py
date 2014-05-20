def group(seq, size):  
    """
    Returns an iterator over a series of lists of length size from iterable.
        
        >>> list(group([1,2,3,4], 2))
        [[1, 2], [3, 4]]
        >>> list(group([1,2,3,4,5], 2))
        [[1, 2], [3, 4], [5]]
    """
    def take(seq, n):
        for i in xrange(n):
            yield seq.next()

    if not hasattr(seq, 'next'):
        seq = iter(seq)
    while True: 
        x = list(take(seq, size))
        if x:
            yield x
        else:
            break
