'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''

def is_pangram(s):
    counter = []

    fresh = s.replace('!' , '').replace(',' , '').replace('.' , '').replace('1' , '' ).replace('2' , '').replace('3' , '').replace('4' , '').replace('5' , '').replace('6' , '').replace('7' , '').replace('8' , '').replace('9' , '').replace('0' , '')

    alphabets = sorted('abcdefghijklmnopqrstuvwxyz')
    
    joined =  ''.join(i.lower() for i in fresh.split())

    for letters in alphabets:
        counter.append(letters)

    if counter == sorted(set(joined)):
        return True
    else:
        return False


