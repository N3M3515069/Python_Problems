'''DESCRIPTION:
Write a function that always returns 5

Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

Good luck :)'''

def unusual_five():
    counter = []
    val = str(ord('i'))

    for i in val:
        counter.append(i)
    value = list(reversed(counter))
    valuex = value.pop()
    valuex = value.pop()
    valuex = value.pop()
    for i in valuex:
        return int(i
