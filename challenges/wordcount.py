

def word_count(string):
    # create an empty dictionary
    word_dict = {}
    
    # set the string(arg) to lowercase
    string = string.lower()

    # the method split() returns a *list* of all the words in the string
    word_list = string.split()

    # use a loop to get inside the list
    for word in word_list:
        count = 0

        # use a loop to check each word
        for single_word in word_list:
            
            if single_word == word:
                count += 1

        word_dict[word] = count

    return word_dict    

word_count("I do not like it Sam I Am")