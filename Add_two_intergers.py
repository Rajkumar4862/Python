'''
Given two integers num1 and num2, return the sum of the two integers.
 

Example 1:

Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
Example 2:

Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.

Author : http://github.com/Rajkumary5610
'''

class Solution:
    def addtwointerger(self,num1: int, num2: int) -> int:
        return num1 + num2
    

n = input("Enter the first number \n")
m = input("Enter the second number \n")
s = Solution()
print(s.addtwointerger(int(n),int(m)))
