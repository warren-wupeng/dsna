"""
题目：输入2个int型(32位)整数，它们进行除法计算并返回商，要求不得使用乘号'*'、除号'/'及求余符号'%'。
当发生溢出时，返回最大的整数值。假设除数不为0。例如，输入15和2，输出15/2的结果，即7
"""
import unittest


def divide(dividend: int, divisor: int):
    """
    由于是整数的除法并且除数不等于0，因此商的绝对值一定小于或等于被除数的绝对值。
    因此，int型整数的除法只有一种情况会导致溢出，即（-2^31）/（-1）。这是因为最大的正数为
    2^31-1，2^31 超出了正数的范围。
    """
    if dividend == 0x80000000 and divisor == -1:
        return 0xffffffff
    """
    将负数转换成正数存在一个小问题。对于32位的整数而言，最小的整数是-2^31，最大的整数是2^31-1。
    因此，如果将-2^31,转换为正数则会导致溢出。由于将任意正数转换为负数都不会溢出，
    因此可以先将正数都转换成负数，用前面优化之后的减法计算两个负数的除法，
    然后根据需要调整商的正负号。
    """
    negatives = int(dividend > 0) + int(divisor > 0)
    if dividend > 0:
        dividend = -dividend

    if divisor > 0:
        divisor = -divisor
    result = divide_core(dividend, divisor)
    if negatives == 1:
        result = -result
    return result


def divide_core(dividend: int, divisor: int):
    dd = dividend
    dr = divisor
    result = 0
    while dd <= dr:
        m = 0
        while dr*2**(m+1) >= dd:
            m += 1
        dd -= dr*2**m
        result += 2**m

    return result


class TestDivideCore(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(9, divide(18, 2))
        self.assertEqual(-9, divide(18, -2))
        self.assertEqual(7, divide(-15, -2))
        self.assertEqual(0xffffffff, divide(0x80000000, -1))


