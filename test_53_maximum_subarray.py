import code_53_maximum_subarray as c

def test_example_1():
    s = c.Solution()
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_example_2():
    s = c.Solution()
    assert s.maxSubArray([1]) == 1

def test_example_3():
    s=c.Solution()
    assert s.maxSubArray([5,4,-1,7,8]) == 23