"""
* Name: sentiwords.py
* Description: BIA-660-WS Homework 1
* Authors: Group 8
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

"""
Accepts a list of reviews and a Lexicon of positive words
and returns the word that appears most frequently right after a positive word. 
"""


#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#The function returns the word that appears most frequently right after a positive word.
def run( reviews_file, positive_words_file  ):
    # Dictionary where
    #   Key = Word that appears after a positive word
    #   Value = The Number of times that word appears right after a positive word
    words_and_counts_dict = {} 
    
    #load the positive lexicons
    posLex=loadLexicon(positive_words_file)
    
    fin=open(reviews_file)  # Open text file
    for line in fin: # for every line in the file (1 review per line)
        
        line=line.lower().strip()
        
        words=line.split(' ') # slit on the space to get list of words
   
        last_word_was_pos_flag = False  # Keeps track of if the previous word is in the positive words lexicon
        for word in words: #for every word in the review
            if last_word_was_pos_flag:  # If the last word is in the positive lexicon, then add the current word to the dictionary
                if word not in words_and_counts_dict.keys():    # If the word is not yet in the dictionary, create a new entry for it
                    words_and_counts_dict[word] = 1
                else:   # If the word is already in the dictionary, increment its count
                    words_and_counts_dict[word] = words_and_counts_dict[word] + 1

            if word in posLex: # if the word is in the positive lexicon, then set the last_word_was_pos flag to True
                last_word_was_pos_flag = True
            else:   #   If the word is not in the positive lexicon, then set the last_word_was_pos flag to False
                last_word_was_pos_flag = False

    fin.close()

    # print(words_and_counts_dict)

    max_count = -1  # Keeps track of the current max times a word has appeared
    most_frequent_word = "" # Keeps track of the word that has appeared the most
    for (word_after_pos, count) in words_and_counts_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word_after_pos
        
    return most_frequent_word   # Return the word that appears most frequently right after a positive word


if __name__ == "__main__": 
    most_frequent_word = run('textfile2', 'positive-words.txt')
    print(most_frequent_word)
       





