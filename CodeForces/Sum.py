'''A. Sum
time limit per test1 second
memory limit per test256 megabytes
You are given three integers a
, b
, and c
. Determine if one of them is the sum of the other two.

Input
The first line contains a single integer t
 (1≤t≤9261
) — the number of test cases.

The description of each test case consists of three integers a
, b
, c
 (0≤a,b,c≤20
).

Output
For each test case, output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example
input
7
1 4 3
2 5 8
9 11 20
0 0 0
20 20 20
4 12 3
15 7 8
output
YES
NO
YES
YES
NO
NO
YES
Note
In the first test case, 1+3=4
.

In the second test case, none of the numbers is the sum of the other two.

In the third test case, 9+11=20
.'''

def num(arg):

    numbers = [int(i) for i in arg.split() if i.isnumeric()]
    
    if not numbers:
        return "NO"
    
    max_num = max(numbers)
    others_sum = sum(numbers) - max_num

    return "YES" if max_num == others_sum else "NO"


test_cases = int(input())

for i in range(test_cases):
    digits = input()

    print(num(digits))