"""Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!"""


def capitalize(s):
    eves = "".join(
        s[index].upper() if index % 2 == 0 else s[index] for index in range(len(s))
    )

    odds = "".join(s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s)))

    return [eves, odds]
