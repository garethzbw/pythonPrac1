def function_default(a, times=11):
    if a == 1:
        print 'a times b equals {}'.format(a * times)
        return a
    else:
        print '1'

if __name__ == '__main__':
    b = function_default(10)

