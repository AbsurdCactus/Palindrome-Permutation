
def palindrome_detector(string_one, string_two):

    string_list = [string_one, string_two]
    longest = max(string_list)
    shortest = min(string_list)

    if len(longest) - len(shortest) > 1:

        return False

    char_change_counter = 0

    for i in longest:
        
        if i not in shortest:

            char_change_counter += 1

    if char_change_counter > 1:

        print(char_change_counter)

        return False

    else:

        return True





palindrome_detector(string_one="pale", string_two="bale")
