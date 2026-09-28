# Questions :---50. Pow(x, n)

"""
Problem Statements :---
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


"""

# Code :----


def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n > 0:
        if n & 1:
            result *= current_product
        current_product *= current_product

        n >>= 1

    return result


x = 2.00000
n = 10
print(myPow(x, n))
