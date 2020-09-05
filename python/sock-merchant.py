"""
Complete the sockMerchant function in the editor below.
It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
"""
import pytest
import os
def sockMerchant(n, ar):
    pairs = 0
    socks = dict()
    for sock_col in ar:
        if sock_col in socks:
            socks.pop(sock_col)
            pairs += 1
        else:
            socks.update({sock_col: 1})
    return pairs

def testFunction1():
    assert sockMerchant(5, [1,1,2,2,3]) == 2
def testFunction2():
    assert sockMerchant(5, [1,2,3,4,5]) == 0
def testFunction3():
    assert sockMerchant(5, [1,1,1,1,1]) == 2

if __name__ == '__main__':

    testFunction1()
    testFunction2()
    testFunction3()
