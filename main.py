
def palindrome_detector(given_string):

    counter = {}
    odd = 0

    for letter in given_string:

        if letter not in counter:

            counter[letter] = 0

        counter[letter] += 1

    for i in counter.values():

        if i % 2 == 1:

            odd += 1
        
        if odd > 1:

            return False

    return True

    

    





palindrome_detector(given_string="racecar")
