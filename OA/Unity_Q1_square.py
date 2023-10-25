# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
There are two wooden sticks of lengths A and B respectively. Each of them can be cutinto shorter sticks ofinteger lengths. Our goal is to construct the largest possible square.In order to do this, we want to cut the sticks in such a way as to achieve four sticks of thesame length (note that there can be some leftover pieces). What is the longest side ofsquare that we can achieve?
Write a function:
def solution(A，B)
that, given two integers A, B, returns the side length of the largest square that we canobtain. lf it is not possible to create any square, the function should return 0
Examples:
1. Given A = 10, B = 21, the function should return 7. We can split the second stick intothree sticks of length 7 and shorten the first stick by 3.
2. Given A = 13, B = 11, the function should return 5. We can cut two sticks of length 5from each of the given sticks.
3. Given A = 2, B = 1, the function should return 0. lt is not possible to make any squarefrom the given sticks.
4. Given A = 1, B = 8, the function should return 2. We can cut stick B into four parts.Write an efficient algorithm for the following assumptions:
A and B are integers within the range [1..1,000,000,000)
'''

def solution(A, B):
    # Implement your solution here
    

    return max(min(A // 2, B // 2), min(A, B // 3), min(A//3, B), A // 4, B // 4)
