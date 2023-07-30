fibonacciCache = {}


def fibonacci(nthNumber, indent=0):
    global fibonacciCache
    # indentaion = '.' * indent
    # print(indentaion + 'fibonacci(%s) called.' % (nthNumber))
    if nthNumber in fibonacciCache:
        # print(indentaion + 'Returning memoized result: %s' % \
        #       (fibonacciCache[nthNumber]))
        return fibonacciCache[nthNumber]

    if nthNumber == 1 or nthNumber == 2:
        # print(indentaion + 'Bas case fibonacci(%s) \
        #     returning 1.' % (nthNumber))
        fibonacciCache[nthNumber] = 1
        return 1

    else:
        # print(indentaion + 'Calling fibonacci(%s) \
        #     (nthNumber-1).' % (nthNumber - 1))
        # result = fibonacci(nthNumber - 1, indent + 1)

        # print(indentaion + 'Calling fibonacci(%s) \
        #             (nthNumber-2).' % (nthNumber - 2))
        result = fibonacci(nthNumber - 1, indent + 1) + \
                 fibonacci(nthNumber - 2, indent + 1)

        # print('Call to fibonacci(%s) returning %s.' \
        #       % (nthNumber, result))
        fibonacciCache[nthNumber] = result
        return result

print(fibonacci(10))
